# ResolvedLlmProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Provider Id | 
**title** | **str** | Provider Title | 
**models** | [**List[LlmModel]**](LlmModel.md) |  | 

## Example

```python
from gooddata_api_client.models.resolved_llm_provider import ResolvedLlmProvider

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedLlmProvider from a JSON string
resolved_llm_provider_instance = ResolvedLlmProvider.from_json(json)
# print the JSON string representation of the object
print(ResolvedLlmProvider.to_json())

# convert the object into a dict
resolved_llm_provider_dict = resolved_llm_provider_instance.to_dict()
# create an instance of ResolvedLlmProvider from a dict
resolved_llm_provider_from_dict = ResolvedLlmProvider.from_dict(resolved_llm_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


