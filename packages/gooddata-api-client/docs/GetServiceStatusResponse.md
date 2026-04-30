# GetServiceStatusResponse

Status of an AI Lake service

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **object** | Free-form JSON object | 

## Example

```python
from gooddata_api_client.models.get_service_status_response import GetServiceStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetServiceStatusResponse from a JSON string
get_service_status_response_instance = GetServiceStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetServiceStatusResponse.to_json())

# convert the object into a dict
get_service_status_response_dict = get_service_status_response_instance.to_dict()
# create an instance of GetServiceStatusResponse from a dict
get_service_status_response_from_dict = GetServiceStatusResponse.from_dict(get_service_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


