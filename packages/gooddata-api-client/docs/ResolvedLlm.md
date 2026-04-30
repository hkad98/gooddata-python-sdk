# ResolvedLlm

The resolved LLM configuration, or null if none is configured.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 

## Example

```python
from gooddata_api_client.models.resolved_llm import ResolvedLlm

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedLlm from a JSON string
resolved_llm_instance = ResolvedLlm.from_json(json)
# print the JSON string representation of the object
print(ResolvedLlm.to_json())

# convert the object into a dict
resolved_llm_dict = resolved_llm_instance.to_dict()
# create an instance of ResolvedLlm from a dict
resolved_llm_from_dict = ResolvedLlm.from_dict(resolved_llm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


