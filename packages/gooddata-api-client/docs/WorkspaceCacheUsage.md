# WorkspaceCacheUsage

Data about a particular workspace cache usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**WorkspaceCurrentCacheUsage**](WorkspaceCurrentCacheUsage.md) |  | 
**removal_intervals** | [**List[CacheRemovalInterval]**](CacheRemovalInterval.md) | List of cache removal intervals for workspace. | 
**settings** | [**WorkspaceCacheSettings**](WorkspaceCacheSettings.md) |  | 

## Example

```python
from gooddata_api_client.models.workspace_cache_usage import WorkspaceCacheUsage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCacheUsage from a JSON string
workspace_cache_usage_instance = WorkspaceCacheUsage.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCacheUsage.to_json())

# convert the object into a dict
workspace_cache_usage_dict = workspace_cache_usage_instance.to_dict()
# create an instance of WorkspaceCacheUsage from a dict
workspace_cache_usage_from_dict = WorkspaceCacheUsage.from_dict(workspace_cache_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


