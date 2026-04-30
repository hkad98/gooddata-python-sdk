# GenerateTitleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Additional note with details in case generation was not performed | [optional] 
**title** | **str** | Generated title of the requested object | [optional] 

## Example

```python
from gooddata_api_client.models.generate_title_response import GenerateTitleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateTitleResponse from a JSON string
generate_title_response_instance = GenerateTitleResponse.from_json(json)
# print the JSON string representation of the object
print(GenerateTitleResponse.to_json())

# convert the object into a dict
generate_title_response_dict = generate_title_response_instance.to_dict()
# create an instance of GenerateTitleResponse from a dict
generate_title_response_from_dict = GenerateTitleResponse.from_dict(generate_title_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


