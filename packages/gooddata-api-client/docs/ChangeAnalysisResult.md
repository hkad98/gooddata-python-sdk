# ChangeAnalysisResult

Result of a change analysis execution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[MetricValueChange]**](MetricValueChange.md) | The change analysis result data containing significant changes. | 

## Example

```python
from gooddata_api_client.models.change_analysis_result import ChangeAnalysisResult

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeAnalysisResult from a JSON string
change_analysis_result_instance = ChangeAnalysisResult.from_json(json)
# print the JSON string representation of the object
print(ChangeAnalysisResult.to_json())

# convert the object into a dict
change_analysis_result_dict = change_analysis_result_instance.to_dict()
# create an instance of ChangeAnalysisResult from a dict
change_analysis_result_from_dict = ChangeAnalysisResult.from_dict(change_analysis_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


