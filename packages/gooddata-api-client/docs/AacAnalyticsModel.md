# AacAnalyticsModel

AAC analytics model representation compatible with Analytics-as-Code YAML format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_hierarchies** | [**List[AacAttributeHierarchy]**](AacAttributeHierarchy.md) | An array of attribute hierarchies. | [optional] 
**dashboards** | [**List[AacDashboard]**](AacDashboard.md) | An array of dashboards. | [optional] 
**metrics** | [**List[AacMetric]**](AacMetric.md) | An array of metrics. | [optional] 
**plugins** | [**List[AacPlugin]**](AacPlugin.md) | An array of dashboard plugins. | [optional] 
**visualizations** | [**List[AacVisualization]**](AacVisualization.md) | An array of visualizations. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_analytics_model import AacAnalyticsModel

# TODO update the JSON string below
json = "{}"
# create an instance of AacAnalyticsModel from a JSON string
aac_analytics_model_instance = AacAnalyticsModel.from_json(json)
# print the JSON string representation of the object
print(AacAnalyticsModel.to_json())

# convert the object into a dict
aac_analytics_model_dict = aac_analytics_model_instance.to_dict()
# create an instance of AacAnalyticsModel from a dict
aac_analytics_model_from_dict = AacAnalyticsModel.from_dict(aac_analytics_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


