# MeasureValueCondition

A condition for filtering by measure value. Can be either a comparison or a range condition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison** | [**ComparisonConditionComparison**](ComparisonConditionComparison.md) |  | 
**range** | [**RangeConditionRange**](RangeConditionRange.md) |  | 

## Example

```python
from gooddata_api_client.models.measure_value_condition import MeasureValueCondition

# TODO update the JSON string below
json = "{}"
# create an instance of MeasureValueCondition from a JSON string
measure_value_condition_instance = MeasureValueCondition.from_json(json)
# print the JSON string representation of the object
print(MeasureValueCondition.to_json())

# convert the object into a dict
measure_value_condition_dict = measure_value_condition_instance.to_dict()
# create an instance of MeasureValueCondition from a dict
measure_value_condition_from_dict = MeasureValueCondition.from_dict(measure_value_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


