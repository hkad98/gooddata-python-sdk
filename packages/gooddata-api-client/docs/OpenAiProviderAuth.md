# OpenAiProviderAuth

Authentication configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | OpenAI API key. | [optional] 
**type** | **str** | Authentication type. | 

## Example

```python
from gooddata_api_client.models.open_ai_provider_auth import OpenAiProviderAuth

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAiProviderAuth from a JSON string
open_ai_provider_auth_instance = OpenAiProviderAuth.from_json(json)
# print the JSON string representation of the object
print(OpenAiProviderAuth.to_json())

# convert the object into a dict
open_ai_provider_auth_dict = open_ai_provider_auth_instance.to_dict()
# create an instance of OpenAiProviderAuth from a dict
open_ai_provider_auth_from_dict = OpenAiProviderAuth.from_dict(open_ai_provider_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


