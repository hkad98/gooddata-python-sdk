# CacheUsageData

Result of scan of data source physical model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_cache_usage** | [**OrganizationCacheUsage**](OrganizationCacheUsage.md) |  | 
**workspace_cache_usages** | [**Dict[str, WorkspaceCacheUsage]**](WorkspaceCacheUsage.md) | Map of data about the cache usage of the individual workspaces. | 

## Example

```python
from gooddata_api_client.models.cache_usage_data import CacheUsageData

# TODO update the JSON string below
json = "{}"
# create an instance of CacheUsageData from a JSON string
cache_usage_data_instance = CacheUsageData.from_json(json)
# print the JSON string representation of the object
print(CacheUsageData.to_json())

# convert the object into a dict
cache_usage_data_dict = cache_usage_data_instance.to_dict()
# create an instance of CacheUsageData from a dict
cache_usage_data_from_dict = CacheUsageData.from_dict(cache_usage_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


