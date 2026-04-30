# RangeConditionRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **float** |  | 
**operator** | **str** |  | 
**to** | **float** |  | 

## Example

```python
from gooddata_api_client.models.range_condition_range import RangeConditionRange

# TODO update the JSON string below
json = "{}"
# create an instance of RangeConditionRange from a JSON string
range_condition_range_instance = RangeConditionRange.from_json(json)
# print the JSON string representation of the object
print(RangeConditionRange.to_json())

# convert the object into a dict
range_condition_range_dict = range_condition_range_instance.to_dict()
# create an instance of RangeConditionRange from a dict
range_condition_range_from_dict = RangeConditionRange.from_dict(range_condition_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


