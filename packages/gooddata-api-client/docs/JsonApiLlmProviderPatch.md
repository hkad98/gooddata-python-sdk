# JsonApiLlmProviderPatch

LLM Provider configuration for connecting to LLM services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**JsonApiLlmProviderInAttributes**](JsonApiLlmProviderInAttributes.md) |  | [optional] 
**id** | **str** | API identifier of an object | 
**type** | **str** | Object type | 

## Example

```python
from gooddata_api_client.models.json_api_llm_provider_patch import JsonApiLlmProviderPatch

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiLlmProviderPatch from a JSON string
json_api_llm_provider_patch_instance = JsonApiLlmProviderPatch.from_json(json)
# print the JSON string representation of the object
print(JsonApiLlmProviderPatch.to_json())

# convert the object into a dict
json_api_llm_provider_patch_dict = json_api_llm_provider_patch_instance.to_dict()
# create an instance of JsonApiLlmProviderPatch from a dict
json_api_llm_provider_patch_from_dict = JsonApiLlmProviderPatch.from_dict(json_api_llm_provider_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


