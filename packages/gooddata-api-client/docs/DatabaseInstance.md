# DatabaseInstance

A single AI Lake Database instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the AI Lake Database instance | 
**name** | **str** | Name of the AI Lake Database instance | 
**storage_ids** | **List[str]** | Set of ids of the storage instances this database instance should access. | 

## Example

```python
from gooddata_api_client.models.database_instance import DatabaseInstance

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseInstance from a JSON string
database_instance_instance = DatabaseInstance.from_json(json)
# print the JSON string representation of the object
print(DatabaseInstance.to_json())

# convert the object into a dict
database_instance_dict = database_instance_instance.to_dict()
# create an instance of DatabaseInstance from a dict
database_instance_from_dict = DatabaseInstance.from_dict(database_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


