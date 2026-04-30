# GenerateDescriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **str** | Identifier of the object to describe | 
**object_type** | **str** | Type of the object to describe. One of: visualization, dashboard, metric, fact, attribute | 

## Example

```python
from gooddata_api_client.models.generate_description_request import GenerateDescriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDescriptionRequest from a JSON string
generate_description_request_instance = GenerateDescriptionRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateDescriptionRequest.to_json())

# convert the object into a dict
generate_description_request_dict = generate_description_request_instance.to_dict()
# create an instance of GenerateDescriptionRequest from a dict
generate_description_request_from_dict = GenerateDescriptionRequest.from_dict(generate_description_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


