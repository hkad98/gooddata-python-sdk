# JsonApiLlmProviderInAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_model_id** | **str** | Required ID of the default model to use from the models list. | [optional] 
**description** | **str** | Description of the LLM Provider. | [optional] 
**models** | [**List[JsonApiLlmProviderInAttributesModelsInner]**](JsonApiLlmProviderInAttributesModelsInner.md) | List of LLM models available for this provider. | [optional] 
**name** | **str** |  | [optional] 
**provider_config** | [**JsonApiLlmProviderInAttributesProviderConfig**](JsonApiLlmProviderInAttributesProviderConfig.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_llm_provider_in_attributes import JsonApiLlmProviderInAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiLlmProviderInAttributes from a JSON string
json_api_llm_provider_in_attributes_instance = JsonApiLlmProviderInAttributes.from_json(json)
# print the JSON string representation of the object
print(JsonApiLlmProviderInAttributes.to_json())

# convert the object into a dict
json_api_llm_provider_in_attributes_dict = json_api_llm_provider_in_attributes_instance.to_dict()
# create an instance of JsonApiLlmProviderInAttributes from a dict
json_api_llm_provider_in_attributes_from_dict = JsonApiLlmProviderInAttributes.from_dict(json_api_llm_provider_in_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


