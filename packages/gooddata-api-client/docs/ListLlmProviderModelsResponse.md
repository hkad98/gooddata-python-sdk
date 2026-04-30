# ListLlmProviderModelsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message about the listing result. | 
**models** | [**List[LlmModel]**](LlmModel.md) | Available models on the provider. | 
**success** | **bool** | Whether the model listing succeeded. | 

## Example

```python
from gooddata_api_client.models.list_llm_provider_models_response import ListLlmProviderModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ListLlmProviderModelsResponse from a JSON string
list_llm_provider_models_response_instance = ListLlmProviderModelsResponse.from_json(json)
# print the JSON string representation of the object
print(ListLlmProviderModelsResponse.to_json())

# convert the object into a dict
list_llm_provider_models_response_dict = list_llm_provider_models_response_instance.to_dict()
# create an instance of ListLlmProviderModelsResponse from a dict
list_llm_provider_models_response_from_dict = ListLlmProviderModelsResponse.from_dict(list_llm_provider_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


