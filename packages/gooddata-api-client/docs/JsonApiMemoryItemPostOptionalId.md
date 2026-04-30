# JsonApiMemoryItemPostOptionalId

JSON:API representation of memoryItem entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**JsonApiMemoryItemInAttributes**](JsonApiMemoryItemInAttributes.md) |  | 
**id** | **str** | API identifier of an object | [optional] 
**type** | **str** | Object type | 

## Example

```python
from gooddata_api_client.models.json_api_memory_item_post_optional_id import JsonApiMemoryItemPostOptionalId

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiMemoryItemPostOptionalId from a JSON string
json_api_memory_item_post_optional_id_instance = JsonApiMemoryItemPostOptionalId.from_json(json)
# print the JSON string representation of the object
print(JsonApiMemoryItemPostOptionalId.to_json())

# convert the object into a dict
json_api_memory_item_post_optional_id_dict = json_api_memory_item_post_optional_id_instance.to_dict()
# create an instance of JsonApiMemoryItemPostOptionalId from a dict
json_api_memory_item_post_optional_id_from_dict = JsonApiMemoryItemPostOptionalId.from_dict(json_api_memory_item_post_optional_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


