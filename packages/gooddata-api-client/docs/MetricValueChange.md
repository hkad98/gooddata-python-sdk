# MetricValueChange

Individual change analysis data item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute_name** | **str** | The name of the attribute being analyzed | 
**attribute_value** | **str** | The value of the attribute being analyzed | 
**attribute_values_change_mean** | **float** | The mean of attribute value changes for the attribute being analyzed | 
**attribute_values_change_std** | **float** | The standard deviation of attribute value changes for the attribute being analyzed | 
**is_significant_change** | **bool** | Whether the change is statistically significant | 
**metric_value_delta** | **float** | The delta between analyzed and reference periods | 
**metric_value_delta_abs** | **float** | The absolute delta between analyzed and reference periods | 
**metric_value_in_analyzed_period** | **float** | The metric value in the analyzed period | 
**metric_value_in_reference_period** | **float** | The metric value in the reference period | 
**overall_metric_value_in_analyzed_period** | **float** | The overall metric value in the analyzed period | 
**overall_metric_value_in_reference_period** | **float** | The overall metric value in the reference period | 

## Example

```python
from gooddata_api_client.models.metric_value_change import MetricValueChange

# TODO update the JSON string below
json = "{}"
# create an instance of MetricValueChange from a JSON string
metric_value_change_instance = MetricValueChange.from_json(json)
# print the JSON string representation of the object
print(MetricValueChange.to_json())

# convert the object into a dict
metric_value_change_dict = metric_value_change_instance.to_dict()
# create an instance of MetricValueChange from a dict
metric_value_change_from_dict = MetricValueChange.from_dict(metric_value_change_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


