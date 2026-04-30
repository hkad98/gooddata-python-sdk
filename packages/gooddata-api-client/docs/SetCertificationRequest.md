# SetCertificationRequest

Request to set or clear the certification of a workspace entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the entity. | 
**message** | **str** | Optional message associated with the certification. | [optional] 
**status** | **str** | Certification status of the entity. | [optional] 
**type** | **str** | Type of the entity. | 

## Example

```python
from gooddata_api_client.models.set_certification_request import SetCertificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetCertificationRequest from a JSON string
set_certification_request_instance = SetCertificationRequest.from_json(json)
# print the JSON string representation of the object
print(SetCertificationRequest.to_json())

# convert the object into a dict
set_certification_request_dict = set_certification_request_instance.to_dict()
# create an instance of SetCertificationRequest from a dict
set_certification_request_from_dict = SetCertificationRequest.from_dict(set_certification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


