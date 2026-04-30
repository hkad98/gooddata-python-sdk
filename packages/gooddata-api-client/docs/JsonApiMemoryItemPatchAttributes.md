# JsonApiMemoryItemPatchAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**are_relations_valid** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**instruction** | **str** | The text that will be injected into the system prompt | [optional] 
**is_disabled** | **bool** | Whether memory item is disabled | [optional] 
**keywords** | **List[str]** | Set of unique strings used for semantic similarity filtering | [optional] 
**strategy** | **str** | Strategy defining when the memory item should be applied | [optional] 
**tags** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_memory_item_patch_attributes import JsonApiMemoryItemPatchAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiMemoryItemPatchAttributes from a JSON string
json_api_memory_item_patch_attributes_instance = JsonApiMemoryItemPatchAttributes.from_json(json)
# print the JSON string representation of the object
print(JsonApiMemoryItemPatchAttributes.to_json())

# convert the object into a dict
json_api_memory_item_patch_attributes_dict = json_api_memory_item_patch_attributes_instance.to_dict()
# create an instance of JsonApiMemoryItemPatchAttributes from a dict
json_api_memory_item_patch_attributes_from_dict = JsonApiMemoryItemPatchAttributes.from_dict(json_api_memory_item_patch_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


