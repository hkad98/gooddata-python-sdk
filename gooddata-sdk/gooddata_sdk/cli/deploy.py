# (C) 2024 GoodData Corporation
import json
import subprocess
from pathlib import Path
from typing import Any

from gooddata_sdk import (
    CatalogDeclarativeDataSources,
    CatalogDeclarativeUserGroups,
    CatalogDeclarativeUsers,
    CatalogDeclarativeWorkspace,
    CatalogDeclarativeWorkspaceDataFilters,
    CatalogDeclarativeWorkspaces,
    GoodDataSdk,
)
from gooddata_sdk.cli.utils import _SUPPORTED, filter_data_sources, measure_deploy, workspace_not_found


def _call_gd_cli(path: Path) -> dict[str, Any]:
    assert (path / "gooddata.yaml").exists() and (path / "analytics").exists()
    p = subprocess.Popen(
        ["gd", "stream-out", "--no-validate"],
        cwd=path,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    output, err = p.communicate()
    if err:
        print(f"Deploy workspaces failed with the following error {err=}.")
    data = json.loads(output.decode())
    if "workspaces" not in data:
        raise ValueError("No workspaces found in the output.")
    return data


@measure_deploy(step="workspace")
def _deploy_single_workspace(sdk: GoodDataSdk, path: Path, workspace_id: str, patch: bool) -> None:
    data = _call_gd_cli(path)
    workspaces = [
        CatalogDeclarativeWorkspace.from_dict(workspace_dict)
        for workspace_dict in data["workspaces"]
        if workspace_dict["id"] == workspace_id
    ]
    if len(workspaces) == 0:
        workspace_not_found(workspace_id)
    workspace = workspaces[0]
    if patch:
        workspaces_o = sdk.catalog_workspace.get_declarative_workspaces()
        workspaces_mapping = {workspace.id: workspace for workspace in workspaces_o.workspaces}
        workspaces_mapping[workspace_id] = workspace
        workspaces_o.workspaces = list(workspaces_mapping.values())
    else:
        # what to do with workspace_data_filters?
        # workspace_data_filters = sdk.catalog_workspace.get_declarative_workspace_data_filters().workspace_data_filters
        workspaces_o = CatalogDeclarativeWorkspaces(workspaces=[workspace], workspace_data_filters=[])
    sdk.catalog_workspace.put_declarative_workspaces(workspaces_o)


@measure_deploy(step="workspaces")
def _deploy_workspaces(sdk: GoodDataSdk, path: Path) -> None:
    data = _call_gd_cli(path)
    workspaces = [CatalogDeclarativeWorkspace.from_dict(workspace_dict) for workspace_dict in data["workspaces"]]
    # fetch this information first, so we do not lose them
    workspace_data_filters = sdk.catalog_workspace.get_declarative_workspace_data_filters().workspace_data_filters
    workspaces_o = CatalogDeclarativeWorkspaces(workspaces=workspaces, workspace_data_filters=workspace_data_filters)
    sdk.catalog_workspace.put_declarative_workspaces(workspaces_o)


@measure_deploy(step="data sources")
def _deploy_data_sources(sdk: GoodDataSdk, analytics_root_dir: Path, data_source_ids: list) -> None:
    data_source_credentials = analytics_root_dir.parent / "ds_creds.yaml"
    if not data_source_credentials.exists():
        raise ValueError(
            f"When deploying '{analytics_root_dir.stem}' "
            f"credentials have to be provided in '{data_source_credentials}'."
        )
    data_sources = CatalogDeclarativeDataSources.load_from_disk(analytics_root_dir)
    if len(data_source_ids) == 0:
        sdk.catalog_data_source.put_declarative_data_sources(data_sources, data_source_credentials)
    else:
        """
        TODO: Monkey patching the data sources to deploy only the ones specified in the settings.
        """
        filtered_data_sources = filter_data_sources(data_sources, data_source_ids)
        sdk.catalog_data_source.put_declarative_data_sources(filtered_data_sources, data_source_credentials)


@measure_deploy(step="user groups")
def _deploy_user_groups(sdk: GoodDataSdk, analytics_root_dir: Path) -> None:
    user_groups = CatalogDeclarativeUserGroups.load_from_disk(analytics_root_dir)
    sdk.catalog_user.put_declarative_user_groups(user_groups)


@measure_deploy(step="users")
def _deploy_users(sdk: GoodDataSdk, analytics_root_dir: Path) -> None:
    users = CatalogDeclarativeUsers.load_from_disk(analytics_root_dir)
    sdk.catalog_user.put_declarative_users(users)


@measure_deploy(step="workspace data filters")
def _deploy_workspace_data_filters(sdk: GoodDataSdk, analytics_root_dir: Path) -> None:
    workspace_data_filters = CatalogDeclarativeWorkspaceDataFilters.load_from_disk(analytics_root_dir)
    sdk.catalog_workspace.put_declarative_workspace_data_filters(workspace_data_filters)


def deploy_all(path: Path, settings: dict[str, Any]) -> None:
    init_file = path / "gooddata.yaml"
    # this does not work with .env file yet
    sdk = GoodDataSdk.create_from_aac_profile(profiles_path=init_file)

    analytics_root_dir = path / "analytics"

    workspaces = settings["workspace"]
    patch = settings["patch"]
    if len(workspaces) == 0:
        print("Deploying the whole organization... ⏲️⏲️⏲️")
        _deploy_data_sources(sdk, analytics_root_dir, settings.get("data_source", []))
        _deploy_user_groups(sdk, analytics_root_dir)
        _deploy_users(sdk, analytics_root_dir)
        _deploy_workspace_data_filters(sdk, analytics_root_dir)
        _deploy_workspaces(sdk, path)
        print("Deployed 🚀🚀🚀")
    else:
        selected_workspace = workspaces[0]
        print(f"Deploying only {selected_workspace}... ⏲️⏲️⏲️")
        _deploy_single_workspace(sdk, path, selected_workspace, patch)
        print(f"Deployed {selected_workspace} 🚀🚀🚀")


def deploy_granular(path: Path, settings: dict[str, Any]) -> None:
    analytics_root_dir = path.parent
    init_file = analytics_root_dir.parent / "gooddata.yaml"
    if analytics_root_dir.stem == "analytics" and init_file.exists() and path.stem in _SUPPORTED:
        sdk = GoodDataSdk.create_from_aac_profile(profiles_path=init_file)
        print(f"Deploying '{path.stem}' from '{analytics_root_dir}'...")
        if path.stem == "data_sources":
            _deploy_data_sources(sdk, analytics_root_dir, settings.get("data_source", []))
        elif path.stem == "user_groups":
            _deploy_user_groups(sdk, analytics_root_dir)
        elif path.stem == "users":
            _deploy_users(sdk, analytics_root_dir)
        elif path.stem == "workspaces_data_filters":
            _deploy_workspace_data_filters(sdk, analytics_root_dir)
        elif path.stem == "workspaces":
            _deploy_workspaces(sdk, analytics_root_dir.parent, settings.get("workspace", []))
        print(f"Deployed '{path.stem}' from '{analytics_root_dir}'.")
    else:
        raise ValueError(f"Path {path} is not supported.")
