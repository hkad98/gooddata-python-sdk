# WorkspaceCacheSettings

Cache settings for the workspace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**extra_cache** | **int** | Extra cache for the workspace, in bytes. | 

## Example

```python
from gooddata_api_client.models.workspace_cache_settings import WorkspaceCacheSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WorkspaceCacheSettings from a JSON string
workspace_cache_settings_instance = WorkspaceCacheSettings.from_json(json)
# print the JSON string representation of the object
print(WorkspaceCacheSettings.to_json())

# convert the object into a dict
workspace_cache_settings_dict = workspace_cache_settings_instance.to_dict()
# create an instance of WorkspaceCacheSettings from a dict
workspace_cache_settings_from_dict = WorkspaceCacheSettings.from_dict(workspace_cache_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


