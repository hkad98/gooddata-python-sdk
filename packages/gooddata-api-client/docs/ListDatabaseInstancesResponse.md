# ListDatabaseInstancesResponse

Paged response for listing AI Lake database instances

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**databases** | [**List[DatabaseInstance]**](DatabaseInstance.md) | List of database instances | 
**total_count** | **int** | Total count of items (only set when metaInclude&#x3D;page) | [optional] 

## Example

```python
from gooddata_api_client.models.list_database_instances_response import ListDatabaseInstancesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatabaseInstancesResponse from a JSON string
list_database_instances_response_instance = ListDatabaseInstancesResponse.from_json(json)
# print the JSON string representation of the object
print(ListDatabaseInstancesResponse.to_json())

# convert the object into a dict
list_database_instances_response_dict = list_database_instances_response_instance.to_dict()
# create an instance of ListDatabaseInstancesResponse from a dict
list_database_instances_response_from_dict = ListDatabaseInstancesResponse.from_dict(list_database_instances_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


