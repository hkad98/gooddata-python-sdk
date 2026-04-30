# JsonApiMemoryItemIn

JSON:API representation of memoryItem entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**JsonApiMemoryItemInAttributes**](JsonApiMemoryItemInAttributes.md) |  | 
**id** | **str** | API identifier of an object | 
**type** | **str** | Object type | 

## Example

```python
from gooddata_api_client.models.json_api_memory_item_in import JsonApiMemoryItemIn

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiMemoryItemIn from a JSON string
json_api_memory_item_in_instance = JsonApiMemoryItemIn.from_json(json)
# print the JSON string representation of the object
print(JsonApiMemoryItemIn.to_json())

# convert the object into a dict
json_api_memory_item_in_dict = json_api_memory_item_in_instance.to_dict()
# create an instance of JsonApiMemoryItemIn from a dict
json_api_memory_item_in_from_dict = JsonApiMemoryItemIn.from_dict(json_api_memory_item_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


