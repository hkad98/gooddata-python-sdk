# CompoundMeasureValueFilter

Filter the result by applying multiple comparison and/or range conditions combined with OR logic. If conditions list is empty, no filtering is applied (all rows are returned).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compound_measure_value_filter** | [**CompoundMeasureValueFilterCompoundMeasureValueFilter**](CompoundMeasureValueFilterCompoundMeasureValueFilter.md) |  | 

## Example

```python
from gooddata_api_client.models.compound_measure_value_filter import CompoundMeasureValueFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CompoundMeasureValueFilter from a JSON string
compound_measure_value_filter_instance = CompoundMeasureValueFilter.from_json(json)
# print the JSON string representation of the object
print(CompoundMeasureValueFilter.to_json())

# convert the object into a dict
compound_measure_value_filter_dict = compound_measure_value_filter_instance.to_dict()
# create an instance of CompoundMeasureValueFilter from a dict
compound_measure_value_filter_from_dict = CompoundMeasureValueFilter.from_dict(compound_measure_value_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


