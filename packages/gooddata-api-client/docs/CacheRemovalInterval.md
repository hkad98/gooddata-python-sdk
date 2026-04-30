# CacheRemovalInterval

Information about a period in time and how much cached data was removed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_from** | **datetime** | Start timestamp of the removal interval. | 
**removed** | **int** | Bytes removed during this interval. | 
**to** | **datetime** | End timestamp of the removal interval. | 

## Example

```python
from gooddata_api_client.models.cache_removal_interval import CacheRemovalInterval

# TODO update the JSON string below
json = "{}"
# create an instance of CacheRemovalInterval from a JSON string
cache_removal_interval_instance = CacheRemovalInterval.from_json(json)
# print the JSON string representation of the object
print(CacheRemovalInterval.to_json())

# convert the object into a dict
cache_removal_interval_dict = cache_removal_interval_instance.to_dict()
# create an instance of CacheRemovalInterval from a dict
cache_removal_interval_from_dict = CacheRemovalInterval.from_dict(cache_removal_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


