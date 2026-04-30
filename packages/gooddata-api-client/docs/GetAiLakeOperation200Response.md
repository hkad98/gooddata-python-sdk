# GetAiLakeOperation200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the operation | 
**kind** | **str** | Type of the long-running operation. * &#x60;provision-database&#x60; — Provisioning of an AI Lake database. * &#x60;deprovision-database&#x60; — Deprovisioning (deletion) of an AI Lake database. * &#x60;run-service-command&#x60; — Running a command in a particular AI Lake service.  | 
**status** | **str** |  | 
**error** | [**OperationError**](OperationError.md) |  | 
**result** | **object** | Operation-specific result payload, can be missing for operations like delete | [optional] 

## Example

```python
from gooddata_api_client.models.get_ai_lake_operation200_response import GetAiLakeOperation200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAiLakeOperation200Response from a JSON string
get_ai_lake_operation200_response_instance = GetAiLakeOperation200Response.from_json(json)
# print the JSON string representation of the object
print(GetAiLakeOperation200Response.to_json())

# convert the object into a dict
get_ai_lake_operation200_response_dict = get_ai_lake_operation200_response_instance.to_dict()
# create an instance of GetAiLakeOperation200Response from a dict
get_ai_lake_operation200_response_from_dict = GetAiLakeOperation200Response.from_dict(get_ai_lake_operation200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


