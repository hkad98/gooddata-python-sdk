# JsonApiLlmProviderInAttributesModelsInner

LLM Model configuration (id, family) within a provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** | Family of LLM models. | 
**id** | **str** | Unique identifier of the model (e.g., gpt-5.3, claude-4.6). | 

## Example

```python
from gooddata_api_client.models.json_api_llm_provider_in_attributes_models_inner import JsonApiLlmProviderInAttributesModelsInner

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiLlmProviderInAttributesModelsInner from a JSON string
json_api_llm_provider_in_attributes_models_inner_instance = JsonApiLlmProviderInAttributesModelsInner.from_json(json)
# print the JSON string representation of the object
print(JsonApiLlmProviderInAttributesModelsInner.to_json())

# convert the object into a dict
json_api_llm_provider_in_attributes_models_inner_dict = json_api_llm_provider_in_attributes_models_inner_instance.to_dict()
# create an instance of JsonApiLlmProviderInAttributesModelsInner from a dict
json_api_llm_provider_in_attributes_models_inner_from_dict = JsonApiLlmProviderInAttributesModelsInner.from_dict(json_api_llm_provider_in_attributes_models_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


