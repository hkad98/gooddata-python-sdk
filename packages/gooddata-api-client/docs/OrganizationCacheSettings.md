# OrganizationCacheSettings

Settings for organization cache.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_cache_budget** | **int** | Extra cache budget the organization can allocate among its workspaces, in bytes. | 

## Example

```python
from gooddata_api_client.models.organization_cache_settings import OrganizationCacheSettings

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCacheSettings from a JSON string
organization_cache_settings_instance = OrganizationCacheSettings.from_json(json)
# print the JSON string representation of the object
print(OrganizationCacheSettings.to_json())

# convert the object into a dict
organization_cache_settings_dict = organization_cache_settings_instance.to_dict()
# create an instance of OrganizationCacheSettings from a dict
organization_cache_settings_from_dict = OrganizationCacheSettings.from_dict(organization_cache_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


