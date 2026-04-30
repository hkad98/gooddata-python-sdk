# (C) 2026 GoodData Corporation
"""Post-generation patches for the openapi-generator v7 ``python`` output.

Two patches are applied:

1. ``api_client.sanitize_for_serialization`` — replace the per-model
   ``to_dict()`` (which strips OpenAPI ``readOnly`` fields and any field a
   template marked ``excluded_fields``) with a plain ``model_dump`` so request
   bodies match the wire format that the v6 ``python-prior`` generator
   produced. Keeps existing VCR cassettes byte-compatible.

2. ``models/<oneof_wrapper>.py`` — the v7 generator emits oneOf wrappers
   whose ``from_json`` tries each variant in turn and raises "Multiple
   matches" if more than one validates. When all variants have only optional
   top-level fields (common for OpenAPI schemas with no ``required:``),
   every input matches every variant and the wrapper becomes unusable. We
   patch ``from_json`` to dispatch on the variant's *unique* top-level key
   (each variant's ``__properties`` list — when the keys are mutually
   exclusive between variants, the first-matching one wins).

Both patches are idempotent.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

LEGACY_LINE = "        if hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):\n            obj_dict = obj.to_dict()\n        else:\n            obj_dict = obj.__dict__\n"

PATCHED_LINE = (
    "        # PATCHED by scripts/postgen_api_client.py:\n"
    "        #   Use ``model_dump`` instead of the model's own ``to_dict`` so\n"
    "        #   ``readOnly`` fields stay on the wire (matches the legacy\n"
    "        #   ``python-prior`` generator and existing VCR cassettes). On\n"
    "        #   the way out we (a) flatten oneOf wrappers — the v7 generator\n"
    "        #   models them as ``{actual_instance, one_of_schemas, ...}``\n"
    "        #   envelopes that were never on the wire — and (b) strip the\n"
    "        #   ``additional_properties`` bookkeeping field recursively.\n"
    "        from pydantic import BaseModel as _PydBaseModel\n"
    "\n"
    "        def _normalize_for_wire(value):\n"
    "            if isinstance(value, dict):\n"
    "                # Wrapper-only envelopes lose their ``one_of_schemas`` /\n"
    "                # ``oneof_schema_*_validator`` siblings under\n"
    "                # ``exclude_unset``, so flatten any dict that carries an\n"
    "                # ``actual_instance`` payload.\n"
    "                if 'actual_instance' in value and value.get('actual_instance') is not None:\n"
    "                    return _normalize_for_wire(value['actual_instance'])\n"
    "                extras = value.get('additional_properties')\n"
    "                base = {\n"
    "                    k: _normalize_for_wire(v)\n"
    "                    for k, v in value.items()\n"
    "                    if k != 'additional_properties'\n"
    "                }\n"
    "                # Spread the v7 ``additional_properties`` bookkeeping field\n"
    "                # back onto the top level so OpenAPI ``additionalProperties:\n"
    "                # true`` extension keys survive round-tripping.\n"
    "                if isinstance(extras, dict):\n"
    "                    for ek, ev in extras.items():\n"
    "                        if ek not in base:\n"
    "                            base[ek] = _normalize_for_wire(ev)\n"
    "                return base\n"
    "            if isinstance(value, list):\n"
    "                return [_normalize_for_wire(v) for v in value]\n"
    "            if isinstance(value, set):\n"
    "                return [_normalize_for_wire(v) for v in value]\n"
    "            return value\n"
    "\n"
    "        if isinstance(obj, _PydBaseModel):\n"
    "            obj_dict = _normalize_for_wire(\n"
    "                obj.model_dump(by_alias=True, exclude_unset=True, exclude_none=True)\n"
    "            )\n"
    "        elif hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):\n"
    "            obj_dict = obj.to_dict()\n"
    "        else:\n"
    "            obj_dict = obj.__dict__\n"
)


# --- oneOf wrapper key-dispatch patch -----------------------------------
#
# For each oneOf wrapper (file that defines ``<NAME>_ONE_OF_SCHEMAS``) we
# generate a small dispatcher: look at the top-level keys of the input dict
# and pick the variant whose ``__properties`` includes one of those keys
# (preferring exact alias match). Each variant's ``__properties`` has the
# form ``["alias1", "alias2", ...]`` — the wire-format keys.

_ONEOF_FROM_JSON_RE = re.compile(
    r"    @classmethod\n    def from_json\(cls, json_str: str\) -> Self:\n"
    r".+?"
    r'            raise ValueError\("Multiple matches found when deserializing the JSON string into '
    r"(?P<wrapper>\w+) with oneOf schemas: (?P<schemas>[^\"]+?)\..+?"
    r"            return instance\n",
    re.DOTALL,
)


_ONEOF_MODEL_CONFIG_RE = re.compile(
    r"(    model_config = ConfigDict\(\n(?:.+?\n)*?    \)\n)",
    re.DOTALL,
)


def _inject_oneof_model_serializer(text: str) -> str:
    """Add a ``@model_serializer(mode='wrap')`` that flattens the wrapper.

    Without this, ``model.model_dump()`` on a oneOf wrapper returns an
    envelope (``{actual_instance, one_of_schemas, ...}``) rather than the
    inner variant payload. Downstream SDK code that walks the dump (e.g.
    response deserialization in ``ExecutionResult``) expects the inner shape.
    """
    if "_PATCHED_ONEOF_SERIALIZER" in text:
        return text
    if "from pydantic import" not in text:
        return text
    # add the import for model_serializer
    text = re.sub(
        r"(from pydantic import .*?\n)",
        lambda m: m.group(1) if "model_serializer" in m.group(1) else m.group(1).rstrip("\n") + ", model_serializer\n",
        text,
        count=1,
    )
    serializer = (
        "    # _PATCHED_ONEOF_SERIALIZER by scripts/postgen_api_client.py: dump\n"
        "    # the inner variant directly so SDK code that walks model_dump\n"
        "    # output sees the wire-format payload, not the envelope. The\n"
        "    # serializer respects the parent dump's ``exclude_none`` /\n"
        "    # ``exclude_unset`` flags by passing through ``info``.\n"
        "    @model_serializer(mode='wrap')\n"
        "    def _serialize_oneof(self, handler, info):\n"
        "        if self.actual_instance is None:\n"
        "            return None\n"
        "        if hasattr(self.actual_instance, 'model_dump'):\n"
        "            return self.actual_instance.model_dump(\n"
        "                by_alias=info.by_alias if info.by_alias is not None else True,\n"
        "                exclude_none=info.exclude_none,\n"
        "                exclude_unset=info.exclude_unset,\n"
        "            )\n"
        "        return self.actual_instance\n"
    )
    return _ONEOF_MODEL_CONFIG_RE.sub(lambda m: m.group(1) + "\n" + serializer + "\n", text, count=1)


def _patch_oneof_from_json(model_path: Path) -> bool:
    """Replace a oneOf wrapper's ``from_json`` with a key-dispatch version.

    Returns True if the file was rewritten.
    """
    text = model_path.read_text()
    if "ONE_OF_SCHEMAS" not in text:
        return False
    changed = False
    if "_PATCHED_ONEOF_SERIALIZER" not in text:
        new_text = _inject_oneof_model_serializer(text)
        if new_text != text:
            text = new_text
            changed = True
    if "# PATCHED-ONEOF-FROM-JSON" in text:
        if changed:
            model_path.write_text(text)
        return changed
    m = _ONEOF_FROM_JSON_RE.search(text)
    if not m:
        if changed:
            model_path.write_text(text)
        return changed
    schemas = [s.strip() for s in m.group("schemas").split(",")]
    # Build a list of `(variant_class, marker_keys_alias)` pairs by parsing
    # the file for each variant's import + later checking its __properties at
    # runtime (we generate the dispatcher to do the lookup lazily so this
    # script doesn't have to import the partially-generated package).
    new_block = (
        "    @classmethod\n"
        "    def from_json(cls, json_str: str) -> Self:\n"
        "        # PATCHED-ONEOF-FROM-JSON by scripts/postgen_api_client.py:\n"
        "        #   The default v7 dispatcher tries every variant and raises\n"
        "        #   'Multiple matches' when more than one validates — common\n"
        "        #   when no variant marks a discriminator field as required.\n"
        "        #   Pick the variant whose *unique* alias key is present in\n"
        "        #   the input; fall back to first-validates-wins.\n"
        "        instance = cls.model_construct()\n"
        "        try:\n"
        "            obj = json.loads(json_str)\n"
        "        except (TypeError, ValueError):\n"
        "            obj = None\n"
        "\n"
        "        variant_classes = [\n"
        "            v for v in (\n"
        + "".join(f"                {s},\n" for s in schemas)
        + "            ) if v is not None\n"
        "        ]\n"
        "\n"
        "        def _alias_keys(variant):\n"
        "            keys = set()\n"
        "            for fname, finfo in getattr(variant, 'model_fields', {}).items():\n"
        "                if fname == 'additional_properties':\n"
        "                    continue\n"
        "                keys.add(finfo.alias or fname)\n"
        "            return keys\n"
        "\n"
        "        variant_aliases = [_alias_keys(v) for v in variant_classes]\n"
        "        # A key is a discriminator when it is unique to a single variant.\n"
        "        union = set().union(*variant_aliases) if variant_aliases else set()\n"
        "        shared = set()\n"
        "        for ks in variant_aliases:\n"
        "            for k in ks:\n"
        "                if sum(k in other for other in variant_aliases) > 1:\n"
        "                    shared.add(k)\n"
        "        unique_per_variant = [ks - shared for ks in variant_aliases]\n"
        "\n"
        "        if isinstance(obj, dict):\n"
        "            input_keys = set(obj.keys())\n"
        "            for variant, unique in zip(variant_classes, unique_per_variant):\n"
        "                if unique and any(k in input_keys for k in unique):\n"
        "                    instance.actual_instance = variant.from_json(json_str)\n"
        "                    return instance\n"
        "\n"
        "        # Fallback: try each variant in turn; first successful parse\n"
        "        # wins (matches the legacy ``python-prior`` permissive behaviour).\n"
        "        for variant in variant_classes:\n"
        "            try:\n"
        "                instance.actual_instance = variant.from_json(json_str)\n"
        "                return instance\n"
        "            except (ValidationError, ValueError):\n"
        "                continue\n"
        "        raise ValueError(\n"
        f'            "No match found when deserializing the JSON string into {m.group("wrapper")}"\n'
        f'            " with oneOf schemas: {m.group("schemas")}"\n'
        "        )\n"
    )
    model_path.write_text(text[: m.start()] + new_block + text[m.end() :])
    return True


def _patch_execution_result_data(models_dir: Path) -> int:
    """Relax ``data: List[Dict]`` field types in execution-result models.

    The OpenAPI schema declares ``data.items.type == "object"`` for both
    ``ExecutionResult`` and ``ExecutionResultGrandTotal`` but the server
    returns ``List[Double|null]`` (matching the schema's own description /
    example but not its declared item type). Strict pydantic validation
    rejects valid responses; widen to ``List[Any]`` on our side.

    Returns the number of files patched.
    """
    patched = 0
    for model_filename in ("execution_result.py", "execution_result_grand_total.py"):
        p = models_dir / model_filename
        if not p.exists():
            continue
        text = p.read_text()
        if "_PATCHED_EXEC_RESULT_DATA" in text:
            continue
        new = text.replace(
            "    data: List[Dict[str, Any]] = Field(",
            "    # _PATCHED_EXEC_RESULT_DATA by scripts/postgen_api_client.py:\n"
            "    #   widen ``data`` from ``List[Dict]`` to ``List[Any]`` because the\n"
            "    #   server actually sends ``List[Double|null]`` (matching the schema's\n"
            "    #   own description / example, but not its declared item type).\n"
            "    data: List[Any] = Field(",
            1,
        )
        if new != text:
            p.write_text(new)
            patched += 1
    return patched


def patch(client_root: Path) -> int:
    api_client = client_root / "api_client.py"
    text = api_client.read_text()
    if PATCHED_LINE.split("\n", 2)[0] in text:
        api_client_changed = False
    else:
        if LEGACY_LINE not in text:
            sys.stderr.write(
                f"postgen_api_client: legacy block not found in {api_client}; "
                "the generator output has changed shape — review manually.\n"
            )
            return 1
        api_client.write_text(text.replace(LEGACY_LINE, PATCHED_LINE))
        api_client_changed = True

    # Patch every oneOf wrapper whose default ``from_json`` would raise
    # "Multiple matches" when fed a dict that satisfies several variants
    # because none of the variants mark their distinguishing key as
    # ``required:`` in the schema.
    models_dir = client_root / "models"
    patched = 0
    for model_path in sorted(models_dir.glob("*.py")):
        if _patch_oneof_from_json(model_path):
            patched += 1
    exec_result_patched = _patch_execution_result_data(models_dir)
    print(
        f"postgen_api_client: api_client.py changed={api_client_changed}, "
        f"oneOf wrappers patched={patched}, exec result data widened={exec_result_patched}"
    )
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("usage: postgen_api_client.py <gooddata_api_client_dir>\n")
        sys.exit(2)
    sys.exit(patch(Path(sys.argv[1])))
