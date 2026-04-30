# SucceededOperation

Operation that has succeeded

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **object** | Operation-specific result payload, can be missing for operations like delete | [optional] 

## Example

```python
from gooddata_api_client.models.succeeded_operation import SucceededOperation

# TODO update the JSON string below
json = "{}"
# create an instance of SucceededOperation from a JSON string
succeeded_operation_instance = SucceededOperation.from_json(json)
# print the JSON string representation of the object
print(SucceededOperation.to_json())

# convert the object into a dict
succeeded_operation_dict = succeeded_operation_instance.to_dict()
# create an instance of SucceededOperation from a dict
succeeded_operation_from_dict = SucceededOperation.from_dict(succeeded_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


