# WorkspaceCurrentCacheUsage

Current cache usage of the workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_available** | **int** | Cache available for the workspace. | 
**cache_used** | **int** | Cache used by the workspace. | 
**removal_period_start** | **datetime** | Start timestamp of removal period for the workspace. | 
**removed_since_start** | **int** | Bytes removed since start due to insufficient cache for the workspace. | 

## Example

```python
from gooddata_api_client.models.workspace_current_cache_usage import WorkspaceCurrentCacheUsage

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCurrentCacheUsage from a JSON string
workspace_current_cache_usage_instance = WorkspaceCurrentCacheUsage.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCurrentCacheUsage.to_json())

# convert the object into a dict
workspace_current_cache_usage_dict = workspace_current_cache_usage_instance.to_dict()
# create an instance of WorkspaceCurrentCacheUsage from a dict
workspace_current_cache_usage_from_dict = WorkspaceCurrentCacheUsage.from_dict(workspace_current_cache_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


