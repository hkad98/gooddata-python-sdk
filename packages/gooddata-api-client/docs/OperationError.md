# OperationError

Error information for a failed operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**detail** | **str** | Human-readable error details | 
**status** | **int** | HTTP status code | 
**title** | **str** | Human-readable error name | 

## Example

```python
from gooddata_api_client.models.operation_error import OperationError

# TODO update the JSON string below
json = "{}"
# create an instance of OperationError from a JSON string
operation_error_instance = OperationError.from_json(json)
# print the JSON string representation of the object
print(OperationError.to_json())

# convert the object into a dict
operation_error_dict = operation_error_instance.to_dict()
# create an instance of OperationError from a dict
operation_error_from_dict = OperationError.from_dict(operation_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


