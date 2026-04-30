# AllTimeDateFilter

An all-time date filter that does not restrict by date range. Controls how rows with empty (null/missing) date values are handled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all_time_date_filter** | [**AllTimeDateFilterAllTimeDateFilter**](AllTimeDateFilterAllTimeDateFilter.md) |  | 

## Example

```python
from gooddata_api_client.models.all_time_date_filter import AllTimeDateFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AllTimeDateFilter from a JSON string
all_time_date_filter_instance = AllTimeDateFilter.from_json(json)
# print the JSON string representation of the object
print(AllTimeDateFilter.to_json())

# convert the object into a dict
all_time_date_filter_dict = all_time_date_filter_instance.to_dict()
# create an instance of AllTimeDateFilter from a dict
all_time_date_filter_from_dict = AllTimeDateFilter.from_dict(all_time_date_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


