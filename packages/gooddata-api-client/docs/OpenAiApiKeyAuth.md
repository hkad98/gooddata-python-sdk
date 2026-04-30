# OpenAiApiKeyAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | OpenAI API key. | [optional] 
**type** | **str** | Authentication type. | 

## Example

```python
from gooddata_api_client.models.open_ai_api_key_auth import OpenAiApiKeyAuth

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAiApiKeyAuth from a JSON string
open_ai_api_key_auth_instance = OpenAiApiKeyAuth.from_json(json)
# print the JSON string representation of the object
print(OpenAiApiKeyAuth.to_json())

# convert the object into a dict
open_ai_api_key_auth_dict = open_ai_api_key_auth_instance.to_dict()
# create an instance of OpenAiApiKeyAuth from a dict
open_ai_api_key_auth_from_dict = OpenAiApiKeyAuth.from_dict(open_ai_api_key_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


