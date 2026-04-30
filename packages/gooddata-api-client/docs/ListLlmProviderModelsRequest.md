# ListLlmProviderModelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_config** | [**ListLlmProviderModelsRequestProviderConfig**](ListLlmProviderModelsRequestProviderConfig.md) |  | 

## Example

```python
from gooddata_api_client.models.list_llm_provider_models_request import ListLlmProviderModelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ListLlmProviderModelsRequest from a JSON string
list_llm_provider_models_request_instance = ListLlmProviderModelsRequest.from_json(json)
# print the JSON string representation of the object
print(ListLlmProviderModelsRequest.to_json())

# convert the object into a dict
list_llm_provider_models_request_dict = list_llm_provider_models_request_instance.to_dict()
# create an instance of ListLlmProviderModelsRequest from a dict
list_llm_provider_models_request_from_dict = ListLlmProviderModelsRequest.from_dict(list_llm_provider_models_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


