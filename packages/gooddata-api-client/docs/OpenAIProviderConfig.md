# OpenAIProviderConfig

Configuration for OpenAI provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**OpenAiProviderAuth**](OpenAiProviderAuth.md) |  | 
**base_url** | **str** | Custom base URL for OpenAI API. | [optional] [default to 'https://api.openai.com/v1']
**organization** | **str** | OpenAI organization ID. | [optional] 
**type** | **str** | Provider type. | 

## Example

```python
from gooddata_api_client.models.open_ai_provider_config import OpenAIProviderConfig

# TODO update the JSON string below
json = "{}"
# create an instance of OpenAIProviderConfig from a JSON string
open_ai_provider_config_instance = OpenAIProviderConfig.from_json(json)
# print the JSON string representation of the object
print(OpenAIProviderConfig.to_json())

# convert the object into a dict
open_ai_provider_config_dict = open_ai_provider_config_instance.to_dict()
# create an instance of OpenAIProviderConfig from a dict
open_ai_provider_config_from_dict = OpenAIProviderConfig.from_dict(open_ai_provider_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


