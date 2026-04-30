# RichTextWidgetDescriptor

Rich text widget displaying static content. Has no execution result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[FilterDefinition]**](FilterDefinition.md) | Filters currently applied to the dashboard. | [optional] 
**title** | **str** | Widget title as displayed on the dashboard. | 
**widget_id** | **str** | Widget object ID. | 

## Example

```python
from gooddata_api_client.models.rich_text_widget_descriptor import RichTextWidgetDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of RichTextWidgetDescriptor from a JSON string
rich_text_widget_descriptor_instance = RichTextWidgetDescriptor.from_json(json)
# print the JSON string representation of the object
print(RichTextWidgetDescriptor.to_json())

# convert the object into a dict
rich_text_widget_descriptor_dict = rich_text_widget_descriptor_instance.to_dict()
# create an instance of RichTextWidgetDescriptor from a dict
rich_text_widget_descriptor_from_dict = RichTextWidgetDescriptor.from_dict(rich_text_widget_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


