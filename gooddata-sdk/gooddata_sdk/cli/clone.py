# (C) 2024 GoodData Corporation
import json
import shutil
import subprocess
from pathlib import Path
from typing import Any

from gooddata_sdk import CatalogDeclarativeWorkspaces, GoodDataSdk
from gooddata_sdk.cli.utils import _SUPPORTED, filter_workspaces, measure_clone


def _call_gd_cli(workspace_objects: CatalogDeclarativeWorkspaces, path: Path) -> None:
    workspaces = json.dumps({"workspaces": workspace_objects.to_dict()["workspaces"]})
    p = subprocess.Popen(
        ["gd", "stream-in"], cwd=path, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    _, err = p.communicate(input=workspaces.encode())
    if err:
        print(f"Clone workspaces failed with the following error {err=}.")


@measure_clone(step="workspace")
def _clone_specific_workspace(sdk: GoodDataSdk, path: Path, workspace_id: str) -> None:
    assert (path / "gooddata.yaml").exists() and (path / "analytics").exists()
    workspace_objects = sdk.catalog_workspace.get_declarative_workspaces()
    workspace_objects = filter_workspaces(workspace_objects, list(workspace_id))
    _call_gd_cli(workspace_objects, path)


@measure_clone(step="workspaces")
def _clone_workspaces(sdk: GoodDataSdk, path: Path) -> None:
    assert (path / "gooddata.yaml").exists() and (path / "analytics").exists()
    workspace_objects = sdk.catalog_workspace.get_declarative_workspaces()
    _call_gd_cli(workspace_objects, path)


@measure_clone(step="data sources")
def _clone_data_sources(sdk: GoodDataSdk, analytics_root_dir: Path) -> None:
    data_sources = sdk.catalog_data_source.get_declarative_data_sources()
    data_sources.store_to_disk(analytics_root_dir)


@measure_clone(step="user groups")
def _clone_user_groups(sdk: GoodDataSdk, analytics_root_dir: Path) -> None:
    user_groups = sdk.catalog_user.get_declarative_user_groups()
    user_groups.store_to_disk(analytics_root_dir)


@measure_clone(step="users")
def _clone_users(sdk: GoodDataSdk, analytics_root_dir: Path) -> None:
    users = sdk.catalog_user.get_declarative_users()
    users.store_to_disk(analytics_root_dir)


@measure_clone(step="workspace data filters")
def _clone_workspace_data_filters(sdk: GoodDataSdk, analytics_root_dir: Path) -> None:
    workspace_data_filters = sdk.catalog_workspace.get_declarative_workspace_data_filters()
    workspace_data_filters.store_to_disk(analytics_root_dir)


def clone_all(path: Path, settings: dict[str, Any]) -> None:
    if not path.is_dir():
        raise ValueError(f"Path {path} is not a directory.")
    init_file = path / "gooddata.yaml"
    if not init_file.exists():
        raise ValueError(f"Path {path} does not contain gooddata.yaml file.")
    # this does not work with .env file yet
    sdk = GoodDataSdk.create_from_aac_profile(profiles_path=init_file)
    analytics_root_dir = path / "analytics"

    # clean the directory
    if analytics_root_dir.exists():
        shutil.rmtree(analytics_root_dir)
    # create directory
    analytics_root_dir.mkdir()

    selected_workspace = settings["workspace"]
    if len(selected_workspace) == 0:
        print("Cloning the whole organization... ⏲️⏲️️⏲️️")
        _clone_data_sources(sdk, analytics_root_dir)
        _clone_user_groups(sdk, analytics_root_dir)
        _clone_users(sdk, analytics_root_dir)
        _clone_workspace_data_filters(sdk, analytics_root_dir)
        _clone_workspaces(sdk, path)
        print("Cloning finished 🚀🚀🚀")
    else:
        print(f"Cloning workspace {selected_workspace[0]} ⏲️⏲️️⏲️️")
        _clone_specific_workspace(sdk, path, selected_workspace)
        print("Cloning finished 🚀🚀🚀")


def clone_granular(path: Path, settings: dict[str, Any], clear: bool = True) -> None:
    init_file = path.parent.parent / "gooddata.yaml"
    analytics_root_dir = path.parent
    if analytics_root_dir.stem == "analytics" and init_file.exists() and path.stem in _SUPPORTED:
        sdk = GoodDataSdk.create_from_aac_profile(profiles_path=init_file)
        if path.exists() and clear:
            shutil.rmtree(path)
        if path.stem == "data_sources":
            _clone_data_sources(sdk, analytics_root_dir)
        elif path.stem == "user_groups":
            _clone_user_groups(sdk, analytics_root_dir)
        elif path.stem == "users":
            _clone_users(sdk, analytics_root_dir)
        elif path.stem == "workspaces_data_filters":
            _clone_workspace_data_filters(sdk, analytics_root_dir)
        elif path.stem == "workspaces":
            if settings["workspace"]:
                _clone_specific_workspace(sdk, analytics_root_dir, settings["workspace"][0])
            else:
                _clone_workspaces(sdk, analytics_root_dir.parent)
    else:
        raise ValueError(f"Path {path} is not supported.")
