# GenerateTitleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object_id** | **str** | Identifier of the object to title | 
**object_type** | **str** | Type of the object to title. Matches chat-search object types. | 

## Example

```python
from gooddata_api_client.models.generate_title_request import GenerateTitleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateTitleRequest from a JSON string
generate_title_request_instance = GenerateTitleRequest.from_json(json)
# print the JSON string representation of the object
print(GenerateTitleRequest.to_json())

# convert the object into a dict
generate_title_request_dict = generate_title_request_instance.to_dict()
# create an instance of GenerateTitleRequest from a dict
generate_title_request_from_dict = GenerateTitleRequest.from_dict(generate_title_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


