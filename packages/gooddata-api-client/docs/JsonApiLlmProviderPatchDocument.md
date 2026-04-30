# JsonApiLlmProviderPatchDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**JsonApiLlmProviderPatch**](JsonApiLlmProviderPatch.md) |  | 

## Example

```python
from gooddata_api_client.models.json_api_llm_provider_patch_document import JsonApiLlmProviderPatchDocument

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiLlmProviderPatchDocument from a JSON string
json_api_llm_provider_patch_document_instance = JsonApiLlmProviderPatchDocument.from_json(json)
# print the JSON string representation of the object
print(JsonApiLlmProviderPatchDocument.to_json())

# convert the object into a dict
json_api_llm_provider_patch_document_dict = json_api_llm_provider_patch_document_instance.to_dict()
# create an instance of JsonApiLlmProviderPatchDocument from a dict
json_api_llm_provider_patch_document_from_dict = JsonApiLlmProviderPatchDocument.from_dict(json_api_llm_provider_patch_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


