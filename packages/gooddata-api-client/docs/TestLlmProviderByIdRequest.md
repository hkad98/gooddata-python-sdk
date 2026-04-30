# TestLlmProviderByIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[LlmModel]**](LlmModel.md) | Models overrides. | [optional] 
**provider_config** | [**ListLlmProviderModelsRequestProviderConfig**](ListLlmProviderModelsRequestProviderConfig.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.test_llm_provider_by_id_request import TestLlmProviderByIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestLlmProviderByIdRequest from a JSON string
test_llm_provider_by_id_request_instance = TestLlmProviderByIdRequest.from_json(json)
# print the JSON string representation of the object
print(TestLlmProviderByIdRequest.to_json())

# convert the object into a dict
test_llm_provider_by_id_request_dict = test_llm_provider_by_id_request_instance.to_dict()
# create an instance of TestLlmProviderByIdRequest from a dict
test_llm_provider_by_id_request_from_dict = TestLlmProviderByIdRequest.from_dict(test_llm_provider_by_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


