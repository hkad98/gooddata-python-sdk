# JsonApiMemoryItemOutAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**are_relations_valid** | **bool** |  | [optional] 
**created_at** | **datetime** | Time of the entity creation. | [optional] 
**description** | **str** |  | [optional] 
**instruction** | **str** | The text that will be injected into the system prompt | 
**is_disabled** | **bool** | Whether memory item is disabled | [optional] 
**keywords** | **List[str]** | Set of unique strings used for semantic similarity filtering | [optional] 
**modified_at** | **datetime** | Time of the last entity modification. | [optional] 
**strategy** | **str** | Strategy defining when the memory item should be applied | 
**tags** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_memory_item_out_attributes import JsonApiMemoryItemOutAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiMemoryItemOutAttributes from a JSON string
json_api_memory_item_out_attributes_instance = JsonApiMemoryItemOutAttributes.from_json(json)
# print the JSON string representation of the object
print(JsonApiMemoryItemOutAttributes.to_json())

# convert the object into a dict
json_api_memory_item_out_attributes_dict = json_api_memory_item_out_attributes_instance.to_dict()
# create an instance of JsonApiMemoryItemOutAttributes from a dict
json_api_memory_item_out_attributes_from_dict = JsonApiMemoryItemOutAttributes.from_dict(json_api_memory_item_out_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


