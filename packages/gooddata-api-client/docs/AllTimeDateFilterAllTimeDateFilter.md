# AllTimeDateFilterAllTimeDateFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_on_result** | **bool** |  | [optional] 
**dataset** | [**AfmObjectIdentifierDataset**](AfmObjectIdentifierDataset.md) |  | 
**empty_value_handling** | **str** | Specifies how rows with empty (null/missing) date values should be handled. INCLUDE means no filtering effect (default), EXCLUDE removes rows with null dates, ONLY keeps only rows with null dates. | [optional] [default to 'INCLUDE']
**granularity** | **str** | Date granularity used to resolve the date attribute label for null value checks. Defaults to DAY if not specified. | [optional] [default to 'DAY']
**local_identifier** | **str** |  | [optional] 

## Example

```python
from gooddata_api_client.models.all_time_date_filter_all_time_date_filter import AllTimeDateFilterAllTimeDateFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AllTimeDateFilterAllTimeDateFilter from a JSON string
all_time_date_filter_all_time_date_filter_instance = AllTimeDateFilterAllTimeDateFilter.from_json(json)
# print the JSON string representation of the object
print(AllTimeDateFilterAllTimeDateFilter.to_json())

# convert the object into a dict
all_time_date_filter_all_time_date_filter_dict = all_time_date_filter_all_time_date_filter_instance.to_dict()
# create an instance of AllTimeDateFilterAllTimeDateFilter from a dict
all_time_date_filter_all_time_date_filter_from_dict = AllTimeDateFilterAllTimeDateFilter.from_dict(all_time_date_filter_all_time_date_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


