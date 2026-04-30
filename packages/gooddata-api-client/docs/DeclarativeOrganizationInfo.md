# DeclarativeOrganizationInfo

Information available about an organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_origins** | **List[str]** |  | [optional] 
**color_palettes** | [**List[DeclarativeColorPalette]**](DeclarativeColorPalette.md) | A list of color palettes. | [optional] 
**csp_directives** | [**List[DeclarativeCspDirective]**](DeclarativeCspDirective.md) | A list of CSP directives. | [optional] 
**early_access** | **str** | Early access defined on level Organization | [optional] 
**early_access_values** | **List[str]** | Early access defined on level Organization | [optional] 
**hostname** | **str** | Formal hostname used in deployment. | 
**id** | **str** | Identifier of the organization. | 
**identity_provider** | [**DeclarativeIdentityProviderIdentifier**](DeclarativeIdentityProviderIdentifier.md) |  | [optional] 
**name** | **str** | Formal name of the organization. | 
**permissions** | [**List[DeclarativeOrganizationPermission]**](DeclarativeOrganizationPermission.md) |  | 
**settings** | [**List[DeclarativeSetting]**](DeclarativeSetting.md) | A list of organization settings. | [optional] 
**themes** | [**List[DeclarativeTheme]**](DeclarativeTheme.md) | A list of themes. | [optional] 

## Example

```python
from gooddata_api_client.models.declarative_organization_info import DeclarativeOrganizationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeclarativeOrganizationInfo from a JSON string
declarative_organization_info_instance = DeclarativeOrganizationInfo.from_json(json)
# print the JSON string representation of the object
print(DeclarativeOrganizationInfo.to_json())

# convert the object into a dict
declarative_organization_info_dict = declarative_organization_info_instance.to_dict()
# create an instance of DeclarativeOrganizationInfo from a dict
declarative_organization_info_from_dict = DeclarativeOrganizationInfo.from_dict(declarative_organization_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


