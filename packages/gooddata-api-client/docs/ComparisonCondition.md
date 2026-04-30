# ComparisonCondition

Condition that compares the metric value to a given constant value using a comparison operator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison** | [**ComparisonConditionComparison**](ComparisonConditionComparison.md) |  | 

## Example

```python
from gooddata_api_client.models.comparison_condition import ComparisonCondition

# TODO update the JSON string below
json = "{}"
# create an instance of ComparisonCondition from a JSON string
comparison_condition_instance = ComparisonCondition.from_json(json)
# print the JSON string representation of the object
print(ComparisonCondition.to_json())

# convert the object into a dict
comparison_condition_dict = comparison_condition_instance.to_dict()
# create an instance of ComparisonCondition from a dict
comparison_condition_from_dict = ComparisonCondition.from_dict(comparison_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


