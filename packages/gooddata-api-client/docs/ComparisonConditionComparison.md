# ComparisonConditionComparison


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operator** | **str** |  | 
**value** | **float** |  | 

## Example

```python
from gooddata_api_client.models.comparison_condition_comparison import ComparisonConditionComparison

# TODO update the JSON string below
json = "{}"
# create an instance of ComparisonConditionComparison from a JSON string
comparison_condition_comparison_instance = ComparisonConditionComparison.from_json(json)
# print the JSON string representation of the object
print(ComparisonConditionComparison.to_json())

# convert the object into a dict
comparison_condition_comparison_dict = comparison_condition_comparison_instance.to_dict()
# create an instance of ComparisonConditionComparison from a dict
comparison_condition_comparison_from_dict = ComparisonConditionComparison.from_dict(comparison_condition_comparison_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


