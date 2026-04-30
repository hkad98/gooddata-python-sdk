# AacMetric

AAC metric definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Metric description. | [optional] 
**format** | **str** | Default format for metric values. | [optional] 
**id** | **str** | Unique identifier of the metric. | 
**is_hidden** | **bool** | Deprecated. Use showInAiResults instead. | [optional] 
**is_hidden_from_kda** | **bool** | Whether to hide from key driver analysis. | [optional] 
**maql** | **str** | MAQL expression defining the metric. | 
**show_in_ai_results** | **bool** | Whether to show in AI results. | [optional] 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**type** | **str** | Metric type discriminator. | 

## Example

```python
from gooddata_api_client.models.aac_metric import AacMetric

# TODO update the JSON string below
json = "{}"
# create an instance of AacMetric from a JSON string
aac_metric_instance = AacMetric.from_json(json)
# print the JSON string representation of the object
print(AacMetric.to_json())

# convert the object into a dict
aac_metric_dict = aac_metric_instance.to_dict()
# create an instance of AacMetric from a dict
aac_metric_from_dict = AacMetric.from_dict(aac_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


