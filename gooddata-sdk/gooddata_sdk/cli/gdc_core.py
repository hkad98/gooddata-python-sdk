# (C) 2024 GoodData Corporation
import argparse
import sys
from pathlib import Path
from typing import Any, List

from gooddata_sdk.cli.clone import clone_all, clone_granular
from gooddata_sdk.cli.deploy import deploy_all, deploy_granular


def _is_root(path: Path) -> bool:
    init_file = path / "gooddata.yaml"
    return init_file.exists()


def _validate_input(args: argparse.Namespace) -> None:
    if args.patch and not args.workspace:
        print("Error: --patch is only valid when --workspace is specified.")
        sys.exit(1)
    if args.patch and args.action == "clone":
        print("Error: --patch is only valid for 'clone'.")
        sys.exit(1)


def _deploy(path: Path, settings: dict[str, Any]) -> None:
    """
    Limitations: orgId still the same
    :param sdk:
    :param path:
    :return:
    """
    if not path.is_dir():
        raise ValueError(f"Path {path} is not a directory.")
    if _is_root(path):
        deploy_all(path, settings)
    else:
        deploy_granular(path, settings)


def _clone(path: Path, settings: dict[str, Any]) -> None:
    if _is_root(path):
        clone_all(path, settings)
    else:
        clone_granular(path, settings)


def main(cli_args: List[str]) -> None:
    """
    gdc deploy – replaces everything
    gdc deploy --workspace my_ws – remove all workspaces and deploy only my_ws
    gdc deploy --workspace my_ws --patch – deploy only my_ws and keep the rest
    """
    parser = argparse.ArgumentParser(prog="gdc", description="Process GoodData as code file structure.")
    parser.add_argument("action", help="Specify if you want to deploy or clone project.", choices=("deploy", "clone"))
    parser.add_argument("--workspace", help="Specify workspace to deploy or clone.", nargs=1, required=False)
    parser.add_argument(
        "--patch",
        help="Specify patch to apply. Only valid when --workspace is specified.",
        action="store_true",
        required=False,
    )
    args = parser.parse_args(cli_args)
    _validate_input(args)
    current_path = Path().resolve()

    """
    Add specification for workspace and data source.
    e.g.: gdc clone --workspace workspace_id clones only specific workspace
    """
    settings = {"patch": args.patch, "workspace": args.workspace or []}
    if args.action == "deploy":
        _deploy(current_path, settings)
    else:
        _clone(current_path, settings)


if __name__ == "__main__":
    main(sys.argv[1:])
