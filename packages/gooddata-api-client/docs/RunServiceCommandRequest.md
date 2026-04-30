# RunServiceCommandRequest

Request to run an AI Lake Service Command

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **Dict[str, Optional[str]]** | The context to pass to the command | [optional] 
**payload** | **object** | Free-form JSON object | [optional] 

## Example

```python
from gooddata_api_client.models.run_service_command_request import RunServiceCommandRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunServiceCommandRequest from a JSON string
run_service_command_request_instance = RunServiceCommandRequest.from_json(json)
# print the JSON string representation of the object
print(RunServiceCommandRequest.to_json())

# convert the object into a dict
run_service_command_request_dict = run_service_command_request_instance.to_dict()
# create an instance of RunServiceCommandRequest from a dict
run_service_command_request_from_dict = RunServiceCommandRequest.from_dict(run_service_command_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


