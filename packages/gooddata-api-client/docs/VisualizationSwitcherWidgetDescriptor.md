# VisualizationSwitcherWidgetDescriptor

Visualization switcher widget allowing users to toggle between multiple visualizations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_visualization_id** | **str** | ID of the currently active visualization in the switcher. | 
**filters** | [**List[FilterDefinition]**](FilterDefinition.md) | Filters currently applied to the dashboard. | [optional] 
**result_id** | **str** | Signed result ID for the currently active visualization&#39;s execution result. | [optional] 
**title** | **str** | Widget title as displayed on the dashboard. | 
**visualization_ids** | **List[str]** | IDs of all visualizations available in the switcher. | 
**widget_id** | **str** | Widget object ID. | 

## Example

```python
from gooddata_api_client.models.visualization_switcher_widget_descriptor import VisualizationSwitcherWidgetDescriptor

# TODO update the JSON string below
json = "{}"
# create an instance of VisualizationSwitcherWidgetDescriptor from a JSON string
visualization_switcher_widget_descriptor_instance = VisualizationSwitcherWidgetDescriptor.from_json(json)
# print the JSON string representation of the object
print(VisualizationSwitcherWidgetDescriptor.to_json())

# convert the object into a dict
visualization_switcher_widget_descriptor_dict = visualization_switcher_widget_descriptor_instance.to_dict()
# create an instance of VisualizationSwitcherWidgetDescriptor from a dict
visualization_switcher_widget_descriptor_from_dict = VisualizationSwitcherWidgetDescriptor.from_dict(visualization_switcher_widget_descriptor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


