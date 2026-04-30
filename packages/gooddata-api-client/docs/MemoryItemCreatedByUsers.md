# MemoryItemCreatedByUsers


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reasoning** | **str** | Reasoning for error states | 
**users** | [**List[MemoryItemUser]**](MemoryItemUser.md) | Users who created memory item | 

## Example

```python
from gooddata_api_client.models.memory_item_created_by_users import MemoryItemCreatedByUsers

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryItemCreatedByUsers from a JSON string
memory_item_created_by_users_instance = MemoryItemCreatedByUsers.from_json(json)
# print the JSON string representation of the object
print(MemoryItemCreatedByUsers.to_json())

# convert the object into a dict
memory_item_created_by_users_dict = memory_item_created_by_users_instance.to_dict()
# create an instance of MemoryItemCreatedByUsers from a dict
memory_item_created_by_users_from_dict = MemoryItemCreatedByUsers.from_dict(memory_item_created_by_users_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


