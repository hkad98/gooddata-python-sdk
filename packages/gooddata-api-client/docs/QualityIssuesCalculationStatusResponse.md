# QualityIssuesCalculationStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** | Error message (available when status is FAILED or NOT_FOUND) | [optional] 
**issues** | [**List[QualityIssue]**](QualityIssue.md) | List of quality issues (available when status is COMPLETED) | [optional] 
**status** | **str** | Current status of the calculation | 

## Example

```python
from gooddata_api_client.models.quality_issues_calculation_status_response import QualityIssuesCalculationStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of QualityIssuesCalculationStatusResponse from a JSON string
quality_issues_calculation_status_response_instance = QualityIssuesCalculationStatusResponse.from_json(json)
# print the JSON string representation of the object
print(QualityIssuesCalculationStatusResponse.to_json())

# convert the object into a dict
quality_issues_calculation_status_response_dict = quality_issues_calculation_status_response_instance.to_dict()
# create an instance of QualityIssuesCalculationStatusResponse from a dict
quality_issues_calculation_status_response_from_dict = QualityIssuesCalculationStatusResponse.from_dict(quality_issues_calculation_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


