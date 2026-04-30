# JsonApiMemoryItemPatch

JSON:API representation of patching memoryItem entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**JsonApiMemoryItemPatchAttributes**](JsonApiMemoryItemPatchAttributes.md) |  | 
**id** | **str** | API identifier of an object | 
**type** | **str** | Object type | 

## Example

```python
from gooddata_api_client.models.json_api_memory_item_patch import JsonApiMemoryItemPatch

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiMemoryItemPatch from a JSON string
json_api_memory_item_patch_instance = JsonApiMemoryItemPatch.from_json(json)
# print the JSON string representation of the object
print(JsonApiMemoryItemPatch.to_json())

# convert the object into a dict
json_api_memory_item_patch_dict = json_api_memory_item_patch_instance.to_dict()
# create an instance of JsonApiMemoryItemPatch from a dict
json_api_memory_item_patch_from_dict = JsonApiMemoryItemPatch.from_dict(json_api_memory_item_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


