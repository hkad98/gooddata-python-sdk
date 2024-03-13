# (C) 2024 GoodData Corporation
import sys
import time
from functools import wraps
from typing import Any

from gooddata_sdk import CatalogDeclarativeDataSources, CatalogDeclarativeWorkspaces

_SUPPORTED = ("data_sources", "user_groups", "users", "workspaces_data_filters", "workspaces")


# https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal
class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def measure_clone(step: str) -> Any:
    def decorate(func: Any) -> Any:
        @wraps(func)
        def timeit_wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            print(f"Clone '{step}' finished. It took {total_time:.4f} seconds")
            return result

        return timeit_wrapper

    return decorate


def measure_deploy(step: str) -> Any:
    def decorate(func: Any) -> Any:
        @wraps(func)
        def timeit_wrapper(*args: Any, **kwargs: Any) -> Any:
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            total_time = end_time - start_time
            print(f"Deploy '{step}' finished. It took {total_time:.4f} seconds")
            return result

        return timeit_wrapper

    return decorate


def workspace_not_found(workspace_id: str) -> None:
    print(f"{bcolors.WARNING}Requested workspace_id {workspace_id} not found.{bcolors.ENDC}")
    sys.exit(1)


def filter_workspaces(
    workspaces: CatalogDeclarativeWorkspaces, workspace_ids: list[str]
) -> CatalogDeclarativeWorkspaces:
    """
    Note:
        Workspace data filters are copied 1:1
    """
    all_workspace_ids = {workspace.id: workspace for workspace in workspaces.workspaces}
    selected_workspaces = []
    for workspace_id in workspace_ids:
        if workspace_id not in all_workspace_ids:
            workspace_not_found(workspace_id)
        else:
            selected_workspaces.append(all_workspace_ids[workspace_id])
    return CatalogDeclarativeWorkspaces(
        workspaces=selected_workspaces, workspace_data_filters=workspaces.workspace_data_filters
    )


def filter_data_sources(
    data_sources: CatalogDeclarativeDataSources, data_source_ids: list[str]
) -> CatalogDeclarativeDataSources:
    print(f"Processing the following data source ids: {','.join(data_source_ids)}")
    all_data_source_ids = {data_source.id: data_source for data_source in data_sources.data_sources}
    selected_data_sources = []
    for data_source_id in data_source_ids:
        if data_source_id not in all_data_source_ids:
            print(f"Requested data source id {data_source_id} not found.")
        else:
            selected_data_sources.append(all_data_source_ids[data_source_id])
    return CatalogDeclarativeDataSources(data_sources=selected_data_sources)
