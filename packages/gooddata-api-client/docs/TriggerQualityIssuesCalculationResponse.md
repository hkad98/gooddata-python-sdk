# TriggerQualityIssuesCalculationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**process_id** | **str** | Process ID for tracking the calculation status | 
**status** | **str** | Current status of the calculation | 

## Example

```python
from gooddata_api_client.models.trigger_quality_issues_calculation_response import TriggerQualityIssuesCalculationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerQualityIssuesCalculationResponse from a JSON string
trigger_quality_issues_calculation_response_instance = TriggerQualityIssuesCalculationResponse.from_json(json)
# print the JSON string representation of the object
print(TriggerQualityIssuesCalculationResponse.to_json())

# convert the object into a dict
trigger_quality_issues_calculation_response_dict = trigger_quality_issues_calculation_response_instance.to_dict()
# create an instance of TriggerQualityIssuesCalculationResponse from a dict
trigger_quality_issues_calculation_response_from_dict = TriggerQualityIssuesCalculationResponse.from_dict(trigger_quality_issues_calculation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


