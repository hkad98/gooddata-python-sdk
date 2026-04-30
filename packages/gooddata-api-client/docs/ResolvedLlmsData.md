# ResolvedLlmsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Provider Id | 
**title** | **str** | Provider Title | 
**models** | [**List[LlmModel]**](LlmModel.md) |  | 

## Example

```python
from gooddata_api_client.models.resolved_llms_data import ResolvedLlmsData

# TODO update the JSON string below
json = "{}"
# create an instance of ResolvedLlmsData from a JSON string
resolved_llms_data_instance = ResolvedLlmsData.from_json(json)
# print the JSON string representation of the object
print(ResolvedLlmsData.to_json())

# convert the object into a dict
resolved_llms_data_dict = resolved_llms_data_instance.to_dict()
# create an instance of ResolvedLlmsData from a dict
resolved_llms_data_from_dict = ResolvedLlmsData.from_dict(resolved_llms_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


