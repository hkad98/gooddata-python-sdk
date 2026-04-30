# TestLlmProviderDefinitionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[LlmModel]**](LlmModel.md) | Models to test. | [optional] 
**provider_config** | [**ListLlmProviderModelsRequestProviderConfig**](ListLlmProviderModelsRequestProviderConfig.md) |  | 

## Example

```python
from gooddata_api_client.models.test_llm_provider_definition_request import TestLlmProviderDefinitionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestLlmProviderDefinitionRequest from a JSON string
test_llm_provider_definition_request_instance = TestLlmProviderDefinitionRequest.from_json(json)
# print the JSON string representation of the object
print(TestLlmProviderDefinitionRequest.to_json())

# convert the object into a dict
test_llm_provider_definition_request_dict = test_llm_provider_definition_request_instance.to_dict()
# create an instance of TestLlmProviderDefinitionRequest from a dict
test_llm_provider_definition_request_from_dict = TestLlmProviderDefinitionRequest.from_dict(test_llm_provider_definition_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


