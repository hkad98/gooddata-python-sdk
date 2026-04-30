# (C) 2022 GoodData Corporation
from __future__ import annotations

import ast
import builtins
import functools
import inspect
import re
from typing import Any, TypeVar

from attrs import Attribute, asdict, define, field
from cattrs import structure
from pydantic import BaseModel as _ApiModel

from gooddata_sdk.utils import AllPagedEntities, camel_to_snake, change_case, snake_to_camel

_ONEOF_WRAPPER_KEYS = {"actual_instance", "one_of_schemas"}


def _unwrap_oneof_dicts(value: Any) -> Any:
    """Recursively flatten oneOf wrapper envelopes inside an already-dumped dict.

    The v7 generator emits oneOf wrappers as pydantic models that hold the
    chosen variant in ``actual_instance``. ``model_dump()`` on the parent dumps
    them as ``{"actual_instance": {...inner...}, "one_of_schemas": {...},
    "oneof_schema_1_validator": None, ...}``. cattrs expects the inner
    variant's shape directly, so we strip the envelope wherever we find one.
    """
    if isinstance(value, dict):
        if _ONEOF_WRAPPER_KEYS.issubset(value.keys()):
            inner = value.get("actual_instance")
            return _unwrap_oneof_dicts(inner) if inner is not None else None
        return {k: _unwrap_oneof_dicts(v) for k, v in value.items()}
    if isinstance(value, list):
        return [_unwrap_oneof_dicts(v) for v in value]
    return value


def _camelize_to_snake(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            camel_to_snake(k): _camelize_to_snake(v)
            for k, v in value.items()
            if k != "additional_properties" and v is not None
        }
    if isinstance(value, list):
        return [_camelize_to_snake(v) for v in value]
    return value


def _is_dict_str_keyed(annotation: Any) -> bool:
    """Return True when ``annotation`` is ``Dict[str, X]`` / ``Optional[Dict[str, X]]``.

    Free-form mappings keyed by user-supplied strings must not have their keys
    camelCased — those keys are *data*, not OpenAPI fields.
    """
    import typing as _t

    origin = _t.get_origin(annotation)
    args = _t.get_args(annotation)
    if origin is _t.Union:
        return any(_is_dict_str_keyed(a) for a in args if a is not type(None))
    return origin in (dict,)


def _camelize_keys_by_schema(snake_dict: Any, cls: Any) -> Any:
    """Camelize *only* schema-defined keys; leave user-supplied dict keys alone.

    ``Base.to_api`` feeds the v7 generator's ``from_dict`` which expects keys
    in alias (camelCase) form. Naive recursive ``snake_to_camel`` would also
    rewrite keys inside ``Dict[str, X]`` free-form mappings (e.g. an export
    request's ``metrics={'order_amount': ...}``), which corrupts user data.
    Walk ``model_fields`` instead so the conversion follows the schema.
    """
    import typing as _t

    from pydantic import BaseModel as _ApiModel  # noqa: F811 (local for clarity)

    if not isinstance(snake_dict, dict) or not isinstance(cls, type) or not issubclass(cls, _ApiModel):
        return snake_dict
    # oneOf wrapper: the input dict carries the variant's fields, not the
    # wrapper's. Try each variant; pick the one whose fields cover the most
    # input keys.
    if "actual_instance" in cls.model_fields:
        variants: list[Any] = []
        for fname, finfo in cls.model_fields.items():
            if not fname.startswith("oneof_schema_"):
                continue
            ann = finfo.annotation
            origin = _t.get_origin(ann)
            args = _t.get_args(ann)
            if origin is _t.Union:
                variants.extend(a for a in args if isinstance(a, type) and issubclass(a, _ApiModel))
            elif isinstance(ann, type) and issubclass(ann, _ApiModel):
                variants.append(ann)
        # Score each variant by how many of its field names are present in
        # the input.
        best = None
        best_score = -1
        for v in variants:
            score = sum(1 for k in snake_dict if k in v.model_fields)
            if score > best_score:
                best = v
                best_score = score
        if best is not None and best_score > 0:
            return _camelize_keys_by_schema(snake_dict, best)
        # Fallback: leave keys alone.
        return snake_dict
    out: dict[str, Any] = {}
    for snake_key, value in snake_dict.items():
        # Find the field whose name matches this snake key.
        field_info = cls.model_fields.get(snake_key)
        wire_key = field_info.alias if field_info and field_info.alias else snake_key
        if field_info is None:
            # No matching field; leave as-is. Likely an extension key.
            out[wire_key] = value
            continue
        annotation = field_info.annotation
        # Strip Optional[...] wrapper
        origin = _t.get_origin(annotation)
        args = _t.get_args(annotation)
        candidates: list[Any] = []
        if origin is _t.Union:
            candidates.extend(a for a in args if a is not type(None))
        else:
            candidates.append(annotation)
        # Detect Dict[str, X] — keys are user data, do not camelize.
        is_dict_keyed = any(_is_dict_str_keyed(c) for c in candidates)
        if is_dict_keyed and isinstance(value, dict):
            inner_value_type = None
            for c in candidates:
                if _t.get_origin(c) in (dict,):
                    a = _t.get_args(c)
                    if len(a) >= 2:
                        inner_value_type = a[1]
                        break
            converted: dict[str, Any] = {}
            for user_key, user_val in value.items():
                if (
                    isinstance(inner_value_type, type)
                    and issubclass(inner_value_type, _ApiModel)
                    and isinstance(user_val, dict)
                ):
                    converted[user_key] = _camelize_keys_by_schema(user_val, inner_value_type)
                else:
                    converted[user_key] = user_val
            out[wire_key] = converted
            continue
        # Walk nested model / list-of-model fields.
        for c in candidates:
            sub_origin = _t.get_origin(c)
            if sub_origin in (list,):
                sub_args = _t.get_args(c)
                inner = sub_args[0] if sub_args else None
                if isinstance(inner, type) and issubclass(inner, _ApiModel) and isinstance(value, list):
                    out[wire_key] = [_camelize_keys_by_schema(v, inner) if isinstance(v, dict) else v for v in value]
                    break
            elif isinstance(c, type) and issubclass(c, _ApiModel) and isinstance(value, dict):
                out[wire_key] = _camelize_keys_by_schema(value, c)
                break
        else:
            out[wire_key] = value
    return out


def _backfill_type_constants(camel_dict: Any, cls: Any) -> None:
    """Inject single-value enum constants for ``type`` where the SDK omits them.

    JSON:API "In" schemas pin ``type`` to a literal (e.g. ``"dataSource"``)
    via a v7 ``@field_validator``. SDK-side dataclasses rarely model that
    redundant constant, so traverse ``model_fields`` and inject the literal
    on every nested dict that targets a generated model whose ``type`` field
    has exactly one allowed value.
    """
    import typing as _t

    if not isinstance(camel_dict, dict) or not isinstance(cls, type) or not issubclass(cls, _ApiModel):
        return
    if "type" in cls.model_fields and "type" not in camel_dict and "actual_instance" not in cls.model_fields:
        allowed = allowed_values_for(cls, "type")
        if allowed and len(allowed) == 1:
            camel_dict["type"] = allowed[0]
    for field_name, field_info in cls.model_fields.items():
        alias = field_info.alias or field_name
        key = alias if alias in camel_dict else field_name if field_name in camel_dict else None
        if key is None:
            continue
        value = camel_dict[key]
        annotation = field_info.annotation
        # unwrap Optional[X] / Union[X, None]
        origin = _t.get_origin(annotation)
        args = _t.get_args(annotation)
        candidate_types: list[Any] = []
        if origin is _t.Union:
            candidate_types.extend(a for a in args if a is not type(None))
        else:
            candidate_types.append(annotation)
        for candidate in list(candidate_types):
            sub_origin = _t.get_origin(candidate)
            sub_args = _t.get_args(candidate)
            if sub_origin in (list, list):
                candidate_types.append(sub_args[0] if sub_args else None)
        for candidate in candidate_types:
            if not isinstance(candidate, type):
                continue
            if not issubclass(candidate, _ApiModel):
                continue
            if isinstance(value, dict):
                _backfill_type_constants(value, candidate)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        _backfill_type_constants(item, candidate)


def _restrict_fields_set_to_input(instance: Any, input_dict: Any) -> None:
    """Recursively mark only those fields as "set" that appeared in the input.

    The v7 generator's ``from_dict`` enthusiastically assigns every declared
    property — including pydantic defaults like ``False`` — even when the
    caller never passed the key. ``model_dump(exclude_unset=True)`` then keeps
    those defaults on the wire and breaks cassettes recorded against the v6
    generator. This walker maps each generated model back to the keys the
    caller supplied (via aliases or attribute names) and clears the rest from
    ``model_fields_set``, plus recurses into nested generated models / lists.

    oneOf wrappers (``actual_instance`` envelopes) get special treatment:
    we keep the wrapper's own ``actual_instance`` marker as set and recurse
    into the variant with the original — un-enveloped — input dict.
    """
    if not isinstance(instance, _ApiModel) or not isinstance(input_dict, dict):
        return
    cls = type(instance)
    if "actual_instance" in cls.model_fields:
        instance.__pydantic_fields_set__ = {"actual_instance"}
        actual = getattr(instance, "actual_instance", None)
        if isinstance(actual, _ApiModel):
            _restrict_fields_set_to_input(actual, input_dict)
        return
    keep: set[str] = set()
    for field_name, field_info in cls.model_fields.items():
        alias = field_info.alias or field_name
        if alias in input_dict or field_name in input_dict:
            keep.add(field_name)
            child_input = input_dict.get(alias, input_dict.get(field_name))
            child_value = getattr(instance, field_name, None)
            if isinstance(child_value, _ApiModel) and isinstance(child_input, dict):
                _restrict_fields_set_to_input(child_value, child_input)
            elif isinstance(child_value, list) and isinstance(child_input, list):
                for sub_value, sub_input in zip(child_value, child_input):
                    if isinstance(sub_value, _ApiModel) and isinstance(sub_input, dict):
                        _restrict_fields_set_to_input(sub_value, sub_input)
    instance.__pydantic_fields_set__ = keep


def _api_to_dict(entity: Any) -> Any:
    """Coerce a v7 generated pydantic model instance to its snake_case dict form.

    The legacy ``python-prior`` generator returned dict-like models; v7 returns
    proper ``pydantic.BaseModel`` instances. cattrs ``structure`` only accepts
    dicts/lists/scalars, so unwrap the model here and let cattrs do the rest.

    Implementation notes:

    * Dump via ``by_alias=True`` so reserved-keyword fields (the v7 generator
      emits e.g. ``var_schema`` with ``alias="schema"`` to dodge ``BaseModel``
      collisions) come out under their wire name. ``camel_to_snake`` then
      maps the wire keys back to the snake_case names cattrs expects on the
      SDK side.
    * Strip the generator's ``additional_properties`` bookkeeping field —
      it's an SDK-side artifact, never on the wire.
    * oneOf wrappers (``actual_instance`` + ``one_of_schemas`` + numbered
      validators) are flattened both at the top level and recursively inside
      nested fields so cattrs sees the union-member shape it expects.
    """
    if isinstance(entity, _ApiModel):
        if "actual_instance" in type(entity).model_fields and getattr(entity, "actual_instance", None) is not None:
            return _api_to_dict(entity.actual_instance)
        dumped = entity.model_dump(by_alias=True, exclude_none=False)
        dumped = _unwrap_oneof_dicts(dumped)
        return _camelize_to_snake(dumped)
    return entity


T = TypeVar("T", bound="Base")
U = TypeVar("U", bound="JsonApiEntityBase")

_ENUM_LITERAL_RE = re.compile(r"set\(\[([^\]]*)\]\)")


@functools.cache
def allowed_values_for(client_class: Any, field_name: str) -> tuple[str, ...] | None:
    """Return the enum values declared for a field on a generated v7 model.

    The pydantic-v2 generator emits per-field ``@field_validator`` methods
    whose body contains a literal ``set([...])`` of allowed values. We extract
    that set rather than maintain a duplicate enum registry. Returns ``None``
    when the field has no enum constraint.
    """
    decorators = getattr(client_class, "__pydantic_decorators__", None)
    if decorators is None:
        return None
    for fv in decorators.field_validators.values():
        if field_name not in fv.info.fields:
            continue
        try:
            src = inspect.getsource(fv.func)
        except (OSError, TypeError):
            continue
        match = _ENUM_LITERAL_RE.search(src)
        if not match:
            continue
        try:
            values = ast.literal_eval(f"[{match.group(1)}]")
        except (SyntaxError, ValueError):
            continue
        return tuple(values)
    return None


def value_in_allowed(instance: type[Base], attribute: Attribute, value: str, client_class: Any | None = None) -> None:
    """attrs-style validator that enforces enum constraints from the generated client.

    Resolves the allowed values from the v7 pydantic ``@field_validator`` source
    so SDK-level fail-fast behavior matches the prior ``python-prior`` generator
    that exposed the same data via ``client_class.allowed_values``.
    """
    if client_class is None:
        client_class = instance.client_class()
    allowed = allowed_values_for(client_class, attribute.name)
    if allowed is None:
        return
    if value not in allowed:
        raise ValueError(
            f"Allowed values for attribute {attribute.name} are: {', '.join(allowed)}. But value {value} was passed."
        )


@define
class Base:
    @classmethod
    def from_api(cls: type[T], entity: Any) -> T:
        """
        Creates object from entity passed by client class, which represents it as dictionary
        or — under the pydantic-v2 generator — as a generated model instance.
        """
        return structure(_api_to_dict(entity), cls)

    @classmethod
    def from_dict(cls: type[T], data: Any, camel_case: bool = True) -> T:
        """
        Creates object from dictionary. It needs to be specified if the dictionary is in camelCase or snake_case.
        """
        data = _api_to_dict(data)
        if camel_case:
            # Round-trip through the v7 generated model so its validators and
            # oneOf discriminators run, then re-emit in the snake_case shape
            # cattrs expects on the SDK side. The input dict may contain
            # either alias-cased (camelCase / wire) or attribute-named
            # (snake_case) keys depending on whether it came from disk YAML
            # or a hand-written fixture, so always camelize first — the v7
            # ``from_dict`` exclusively reads alias keys. Re-using
            # ``_api_to_dict`` afterwards keeps alias handling (e.g.
            # ``var_schema`` → wire ``schema``) and ``additional_properties``
            # stripping consistent with ``from_api``.
            if isinstance(data, dict):
                data = change_case(data, snake_to_camel)
            api_obj = cls.client_class().from_dict(data)
            data = _api_to_dict(api_obj)
        return structure(data, cls)

    def to_dict(self, camel_case: bool = True) -> dict[str, Any]:
        """
        Converts object into dictionary. Optional argument if the dictionary should be camelCase or snake_case can be
        specified.
        """
        if not camel_case:
            return self._get_snake_dict()
        return self.to_api().to_dict()

    @staticmethod
    def _is_attribute_private(attribute: Attribute) -> bool:
        return attribute.name.startswith("_")

    def _get_snake_dict(self) -> dict[str, Any]:
        return asdict(
            self, filter=lambda attribute, value: value is not None and not self._is_attribute_private(attribute)
        )

    @staticmethod
    def client_class() -> Any:
        return NotImplemented

    def to_api(self) -> Any:
        # Build the wire-format dict (camelCase, JSON:API ``type`` constants
        # back-filled from the v7 ``@field_validator`` source) and feed it to
        # the generated ``from_dict``. ``from_dict`` is the only path that
        # understands oneOf wrappers and per-model alias quirks, but it
        # over-eagerly stamps every declared property — including hard-coded
        # defaults like ``generateLongIds=False`` — onto the model. We compare
        # ``model_fields_set`` against the keys we actually passed in and
        # discard the rest, so a downstream ``model_dump(exclude_unset=True)``
        # matches the v6 wire format exactly.
        cls = self.client_class()
        # Use a schema-aware camelizer so user-supplied keys inside
        # ``Dict[str, X]`` fields (e.g. export ``metrics={"order_amount": ...}``)
        # survive the round-trip unchanged.
        camel_dict = _camelize_keys_by_schema(self._get_snake_dict(), cls)
        if not isinstance(camel_dict, dict):
            camel_dict = change_case(self._get_snake_dict(), snake_to_camel)
        _backfill_type_constants(camel_dict, cls)
        instance = cls.from_dict(camel_dict)
        _restrict_fields_set_to_input(instance, camel_dict)
        return instance


@define
class JsonApiEntityBase:
    id: str
    type: str
    attributes: dict[str, Any] = field(repr=False)
    relationships: dict[str, Any] | None = field(repr=False, default=None)
    meta: dict[str, Any] | None = field(repr=False, default=None)
    links: dict[str, Any] | None = field(repr=False, default=None)
    related_entities_data: list[dict[str, Any]] = field(repr=False, factory=list)
    related_entities_side_loads: list[dict[str, Any]] = field(repr=False, factory=list)
    side_loads: list[dict[str, Any]] = field(repr=False, factory=list)

    @classmethod
    def from_api(
        cls,
        entity: Any,
        side_loads: list[Any] | None = None,
        related_entities: AllPagedEntities | None = None,
    ) -> JsonApiEntityBase:
        """
        Creates object from entity passed by client class, which represents it as a dictionary
        or — under the pydantic-v2 generator — as a generated model instance.
        """
        entity = _api_to_dict(entity)
        # ``side_loads`` and the ``related_entities`` payloads are lists of
        # generated pydantic models in v7; coerce each element so cattrs sees
        # plain dicts.
        entity["side_loads"] = [_api_to_dict(s) for s in (side_loads or [])]
        entity["related_entities_data"] = [_api_to_dict(d) for d in (related_entities.data if related_entities else [])]
        entity["related_entities_side_loads"] = [
            _api_to_dict(s) for s in (related_entities.included if related_entities else [])
        ]
        return structure(entity, cls)

    @classmethod
    def from_dict(cls: builtins.type[U], data: dict[str, Any]) -> U:
        return NotImplemented

    @staticmethod
    def to_dict() -> dict[str, Any]:
        return NotImplemented

    @staticmethod
    def to_api() -> Any:
        return NotImplemented

    @staticmethod
    def client_class() -> Any:
        return NotImplemented
