# MemoryItemUser

Users who created memory item

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firstname** | **str** | First name of the user who created memory item | 
**lastname** | **str** | Last name of the user who created memory item | 
**user_id** | **str** | User ID of the user who created memory item | 

## Example

```python
from gooddata_api_client.models.memory_item_user import MemoryItemUser

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryItemUser from a JSON string
memory_item_user_instance = MemoryItemUser.from_json(json)
# print the JSON string representation of the object
print(MemoryItemUser.to_json())

# convert the object into a dict
memory_item_user_dict = memory_item_user_instance.to_dict()
# create an instance of MemoryItemUser from a dict
memory_item_user_from_dict = MemoryItemUser.from_dict(memory_item_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


