# CompoundMeasureValueFilterCompoundMeasureValueFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_on_result** | **bool** |  | [optional] 
**conditions** | [**List[MeasureValueCondition]**](MeasureValueCondition.md) | List of conditions to apply. Conditions are combined with OR logic. Each condition can be either a comparison (e.g., &gt; 100) or a range (e.g., BETWEEN 10 AND 50). If empty, no filtering is applied and all rows are returned. | 
**dimensionality** | [**List[AfmIdentifier]**](AfmIdentifier.md) | References to the attributes to be used when filtering. | [optional] 
**local_identifier** | **str** |  | [optional] 
**measure** | [**AfmIdentifier**](AfmIdentifier.md) |  | 
**treat_null_values_as** | **float** | A value that will be substituted for null values in the metric for the comparisons. | [optional] 

## Example

```python
from gooddata_api_client.models.compound_measure_value_filter_compound_measure_value_filter import CompoundMeasureValueFilterCompoundMeasureValueFilter

# TODO update the JSON string below
json = "{}"
# create an instance of CompoundMeasureValueFilterCompoundMeasureValueFilter from a JSON string
compound_measure_value_filter_compound_measure_value_filter_instance = CompoundMeasureValueFilterCompoundMeasureValueFilter.from_json(json)
# print the JSON string representation of the object
print(CompoundMeasureValueFilterCompoundMeasureValueFilter.to_json())

# convert the object into a dict
compound_measure_value_filter_compound_measure_value_filter_dict = compound_measure_value_filter_compound_measure_value_filter_instance.to_dict()
# create an instance of CompoundMeasureValueFilterCompoundMeasureValueFilter from a dict
compound_measure_value_filter_compound_measure_value_filter_from_dict = CompoundMeasureValueFilterCompoundMeasureValueFilter.from_dict(compound_measure_value_filter_compound_measure_value_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


