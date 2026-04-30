# TrendingObjectsResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[TrendingObjectItem]**](TrendingObjectItem.md) |  | 

## Example

```python
from gooddata_api_client.models.trending_objects_result import TrendingObjectsResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingObjectsResult from a JSON string
trending_objects_result_instance = TrendingObjectsResult.from_json(json)
# print the JSON string representation of the object
print(TrendingObjectsResult.to_json())

# convert the object into a dict
trending_objects_result_dict = trending_objects_result_instance.to_dict()
# create an instance of TrendingObjectsResult from a dict
trending_objects_result_from_dict = TrendingObjectsResult.from_dict(trending_objects_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


