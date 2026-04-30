# ProvisionDatabaseInstanceRequest

Request to provision a new AILake Database instance

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the database instance | 
**storage_ids** | **List[str]** | Set of ids of the storage instances this database instance should access. | 

## Example

```python
from gooddata_api_client.models.provision_database_instance_request import ProvisionDatabaseInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProvisionDatabaseInstanceRequest from a JSON string
provision_database_instance_request_instance = ProvisionDatabaseInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(ProvisionDatabaseInstanceRequest.to_json())

# convert the object into a dict
provision_database_instance_request_dict = provision_database_instance_request_instance.to_dict()
# create an instance of ProvisionDatabaseInstanceRequest from a dict
provision_database_instance_request_from_dict = ProvisionDatabaseInstanceRequest.from_dict(provision_database_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


