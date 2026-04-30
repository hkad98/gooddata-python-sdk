# AacWorkspaceDataFilter

Workspace data filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | Data type of the column. | 
**filter_id** | **str** | Filter identifier. | 
**source_column** | **str** | Source column name. | 

## Example

```python
from gooddata_api_client.models.aac_workspace_data_filter import AacWorkspaceDataFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AacWorkspaceDataFilter from a JSON string
aac_workspace_data_filter_instance = AacWorkspaceDataFilter.from_json(json)
# print the JSON string representation of the object
print(AacWorkspaceDataFilter.to_json())

# convert the object into a dict
aac_workspace_data_filter_dict = aac_workspace_data_filter_instance.to_dict()
# create an instance of AacWorkspaceDataFilter from a dict
aac_workspace_data_filter_from_dict = AacWorkspaceDataFilter.from_dict(aac_workspace_data_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


