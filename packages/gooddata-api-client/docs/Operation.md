# Operation

Represents a Long-Running Operation: a process that takes some time to complete.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the operation | 
**kind** | **str** | Type of the long-running operation. * &#x60;provision-database&#x60; — Provisioning of an AI Lake database. * &#x60;deprovision-database&#x60; — Deprovisioning (deletion) of an AI Lake database. * &#x60;run-service-command&#x60; — Running a command in a particular AI Lake service.  | 
**status** | **str** |  | 

## Example

```python
from gooddata_api_client.models.operation import Operation

# TODO update the JSON string below
json = "{}"
# create an instance of Operation from a JSON string
operation_instance = Operation.from_json(json)
# print the JSON string representation of the object
print(Operation.to_json())

# convert the object into a dict
operation_dict = operation_instance.to_dict()
# create an instance of Operation from a dict
operation_from_dict = Operation.from_dict(operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


