# ListLlmProviderModelsRequestProviderConfig


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
from gooddata_api_client.models.list_llm_provider_models_request_provider_config import ListLlmProviderModelsRequestProviderConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ListLlmProviderModelsRequestProviderConfig from a JSON string
list_llm_provider_models_request_provider_config_instance = ListLlmProviderModelsRequestProviderConfig.from_json(json)
# print the JSON string representation of the object
print(ListLlmProviderModelsRequestProviderConfig.to_json())

# convert the object into a dict
list_llm_provider_models_request_provider_config_dict = list_llm_provider_models_request_provider_config_instance.to_dict()
# create an instance of ListLlmProviderModelsRequestProviderConfig from a dict
list_llm_provider_models_request_provider_config_from_dict = ListLlmProviderModelsRequestProviderConfig.from_dict(list_llm_provider_models_request_provider_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


