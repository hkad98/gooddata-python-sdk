# WidgetDescriptor

Descriptor for a widget on the dashboard.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[ChangeAnalysisParamsFiltersInner]**](ChangeAnalysisParamsFiltersInner.md) |  | [optional] 
**title** | **str** |  | 
**widget_id** | **str** |  | 
**widget_type** | **str** |  | 

## Example

```python
from gooddata_api_client.models.widget_descriptor import WidgetDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetDescriptor from a JSON string
widget_descriptor_instance = WidgetDescriptor.from_json(json)
# print the JSON string representation of the object
print(WidgetDescriptor.to_json())

# convert the object into a dict
widget_descriptor_dict = widget_descriptor_instance.to_dict()
# create an instance of WidgetDescriptor from a dict
widget_descriptor_from_dict = WidgetDescriptor.from_dict(widget_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


