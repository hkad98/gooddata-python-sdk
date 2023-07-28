# (C) 2023 GoodData Corporation
from pathlib import Path
from typing import List, Type

import attr

from gooddata_api_client.model.declarative_dataset_extension import DeclarativeDatasetExtension
from gooddata_sdk.catalog.base import Base
from gooddata_sdk.catalog.workspace.declarative_model.workspace.logical_model.dataset.data_filter_references import (
    CatalogDeclarativeWorkspaceDataFilterReferences,
)
from gooddata_sdk.utils import read_layout_from_file, write_layout_to_file

LAYOUT_DATASET_EXTENSIONS_DIR = "dataset_extensions"


@attr.s(auto_attribs=True, kw_only=True)
class CatalogDeclarativeDatasetExtension(Base):
    id: str
    workspace_data_filter_references: List[CatalogDeclarativeWorkspaceDataFilterReferences] = attr.field(factory=list)

    @staticmethod
    def client_class() -> Type[DeclarativeDatasetExtension]:
        return DeclarativeDatasetExtension

    def store_to_disk(self, dataset_instances_folder: Path) -> None:
        dataset_instance_file = dataset_instances_folder / f"{self.id}.yaml"
        write_layout_to_file(dataset_instance_file, self.to_api().to_dict(camel_case=True))

    @classmethod
    def load_from_disk(cls, dataset_instances_folder: Path) -> "CatalogDeclarativeDatasetExtension":
        dataset_instance_layout = read_layout_from_file(dataset_instances_folder)
        return cls.from_dict(dataset_instance_layout, camel_case=True)
