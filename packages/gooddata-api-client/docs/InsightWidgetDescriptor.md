# InsightWidgetDescriptor

Insight widget displaying a visualization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**List[FilterDefinition]**](FilterDefinition.md) | Filters currently applied to the dashboard. | [optional] 
**result_id** | **str** | Signed result ID for this widget&#39;s cached execution result. | [optional] 
**title** | **str** | Widget title as displayed on the dashboard. | 
**visualization_id** | **str** | Visualization object ID referenced by this insight widget. | 
**widget_id** | **str** | Widget object ID. | 

## Example

```python
from gooddata_api_client.models.insight_widget_descriptor import InsightWidgetDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of InsightWidgetDescriptor from a JSON string
insight_widget_descriptor_instance = InsightWidgetDescriptor.from_json(json)
# print the JSON string representation of the object
print(InsightWidgetDescriptor.to_json())

# convert the object into a dict
insight_widget_descriptor_dict = insight_widget_descriptor_instance.to_dict()
# create an instance of InsightWidgetDescriptor from a dict
insight_widget_descriptor_from_dict = InsightWidgetDescriptor.from_dict(insight_widget_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


