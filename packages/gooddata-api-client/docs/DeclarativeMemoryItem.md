# DeclarativeMemoryItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **str** | Time of the entity creation. | [optional] 
**created_by** | [**DeclarativeUserIdentifier**](DeclarativeUserIdentifier.md) |  | [optional] 
**description** | **str** | Memory item description. | [optional] 
**id** | **str** | Memory item ID. | 
**instruction** | **str** | The text that will be injected into the system prompt. | 
**is_disabled** | **bool** | Whether memory item is disabled. | [optional] 
**keywords** | **List[str]** | Set of unique strings used for semantic similarity filtering. | [optional] 
**modified_at** | **str** | Time of the last entity modification. | [optional] 
**modified_by** | [**DeclarativeUserIdentifier**](DeclarativeUserIdentifier.md) |  | [optional] 
**strategy** | **str** | Strategy defining when the memory item should be applied | 
**tags** | **List[str]** | A list of tags. | [optional] 
**title** | **str** | Memory item title. | 

## Example

```python
from gooddata_api_client.models.declarative_memory_item import DeclarativeMemoryItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeclarativeMemoryItem from a JSON string
declarative_memory_item_instance = DeclarativeMemoryItem.from_json(json)
# print the JSON string representation of the object
print(DeclarativeMemoryItem.to_json())

# convert the object into a dict
declarative_memory_item_dict = declarative_memory_item_instance.to_dict()
# create an instance of DeclarativeMemoryItem from a dict
declarative_memory_item_from_dict = DeclarativeMemoryItem.from_dict(declarative_memory_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


