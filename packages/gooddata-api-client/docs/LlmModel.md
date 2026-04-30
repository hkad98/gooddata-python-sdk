# LlmModel

LLM Model configuration (id, family) within a provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**family** | **str** | Family of LLM models. | 
**id** | **str** | Unique identifier of the model (e.g., gpt-5.3, claude-4.6). | 

## Example

```python
from gooddata_api_client.models.llm_model import LlmModel

# TODO update the JSON string below
json = "{}"
# create an instance of LlmModel from a JSON string
llm_model_instance = LlmModel.from_json(json)
# print the JSON string representation of the object
print(LlmModel.to_json())

# convert the object into a dict
llm_model_dict = llm_model_instance.to_dict()
# create an instance of LlmModel from a dict
llm_model_from_dict = LlmModel.from_dict(llm_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


