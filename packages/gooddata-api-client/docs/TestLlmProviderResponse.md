# TestLlmProviderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_results** | [**List[ModelTestResult]**](ModelTestResult.md) | Per-model test results. | 
**provider_message** | **str** | Message about the provider connectivity test. | 
**provider_reachable** | **bool** | Whether the LLM provider is reachable. | 

## Example

```python
from gooddata_api_client.models.test_llm_provider_response import TestLlmProviderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TestLlmProviderResponse from a JSON string
test_llm_provider_response_instance = TestLlmProviderResponse.from_json(json)
# print the JSON string representation of the object
print(TestLlmProviderResponse.to_json())

# convert the object into a dict
test_llm_provider_response_dict = test_llm_provider_response_instance.to_dict()
# create an instance of TestLlmProviderResponse from a dict
test_llm_provider_response_from_dict = TestLlmProviderResponse.from_dict(test_llm_provider_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


