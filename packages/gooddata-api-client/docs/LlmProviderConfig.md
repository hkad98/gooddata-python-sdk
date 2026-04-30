# LlmProviderConfig

Provider configuration overrides.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**OpenAiProviderAuth**](OpenAiProviderAuth.md) |  | 
**region** | **str** | AWS region for Bedrock. | 
**type** | **str** | Provider type. | 
**endpoint** | **str** | Azure OpenAI endpoint URL. | 
**base_url** | **str** | Custom base URL for OpenAI API. | [optional] [default to 'https://api.openai.com/v1']
**organization** | **str** | OpenAI organization ID. | [optional] 

## Example

```python
from gooddata_api_client.models.llm_provider_config import LlmProviderConfig

# TODO update the JSON string below
json = "{}"
# create an instance of LlmProviderConfig from a JSON string
llm_provider_config_instance = LlmProviderConfig.from_json(json)
# print the JSON string representation of the object
print(LlmProviderConfig.to_json())

# convert the object into a dict
llm_provider_config_dict = llm_provider_config_instance.to_dict()
# create an instance of LlmProviderConfig from a dict
llm_provider_config_from_dict = LlmProviderConfig.from_dict(llm_provider_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


