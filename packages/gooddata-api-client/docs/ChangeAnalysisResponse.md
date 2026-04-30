# ChangeAnalysisResponse

Response for change analysis computation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ExecutionLinks**](ExecutionLinks.md) |  | 

## Example

```python
from gooddata_api_client.models.change_analysis_response import ChangeAnalysisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeAnalysisResponse from a JSON string
change_analysis_response_instance = ChangeAnalysisResponse.from_json(json)
# print the JSON string representation of the object
print(ChangeAnalysisResponse.to_json())

# convert the object into a dict
change_analysis_response_dict = change_analysis_response_instance.to_dict()
# create an instance of ChangeAnalysisResponse from a dict
change_analysis_response_from_dict = ChangeAnalysisResponse.from_dict(change_analysis_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


