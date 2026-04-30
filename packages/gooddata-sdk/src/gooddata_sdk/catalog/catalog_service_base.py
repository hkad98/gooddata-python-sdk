# (C) 2022 GoodData Corporation
from __future__ import annotations

import json
from pathlib import Path

from gooddata_api_client.api.actions_api import ActionsApi
from gooddata_api_client.api.entities_api import EntitiesApi
from gooddata_api_client.api.layout_api import LayoutApi
from gooddata_api_client.api.user_management_api import UserManagementApi
from gooddata_api_client.models.json_api_organization_out_document import JsonApiOrganizationOutDocument

from gooddata_sdk.catalog.organization.entity_model.organization import CatalogOrganization
from gooddata_sdk.client import GoodDataApiClient

LAYOUT_ROOT_FOLDER = "gooddata_layouts"


class CatalogServiceBase:
    def __init__(self, api_client: GoodDataApiClient) -> None:
        self._client = api_client
        self._entities_api: EntitiesApi = api_client.entities_api
        self._layout_api: LayoutApi = api_client.layout_api
        self._actions_api: ActionsApi = api_client.actions_api
        self._user_management_api: UserManagementApi = api_client.user_management_api

    def get_organization(self) -> CatalogOrganization:
        # ``get_organization`` is a redirecting endpoint whose OpenAPI spec only
        # documents the 302 status, so the v7 generator emits a typed return of
        # ``None``. We bypass the typed wrapper, fetch the raw response, and
        # parse the body as :class:`JsonApiOrganizationOutDocument` ourselves.
        # In the legacy ``python-prior`` generator this was achieved by mutating
        # the endpoint's ``response_type`` setting; that hook no longer exists.
        raw = self._entities_api.get_organization_without_preload_content()
        body = raw.data.decode("utf-8") if isinstance(raw.data, (bytes, bytearray)) else raw.data
        document = JsonApiOrganizationOutDocument.from_dict(json.loads(body))
        return CatalogOrganization.from_api(document.data)

    @property
    def organization_id(self) -> str:
        return self.get_organization().id

    def layout_organization_folder(self, layout_root_path: Path) -> Path:
        return layout_root_path / LAYOUT_ROOT_FOLDER / self.organization_id
