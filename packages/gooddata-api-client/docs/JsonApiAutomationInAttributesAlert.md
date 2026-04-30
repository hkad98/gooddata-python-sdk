# JsonApiAutomationInAttributesAlert


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | [**AlertCondition**](AlertCondition.md) |  | 
**execution** | [**AlertAfm**](AlertAfm.md) |  | 
**interval** | **str** | Date granularity for the interval of ONCE_PER_INTERVAL trigger. Supported granularities: DAY, WEEK, MONTH, QUARTER, YEAR. | [optional] 
**trigger** | **str** | Trigger behavior for the alert. ALWAYS - alert is triggered every time the condition is met. ONCE - alert is triggered only once when the condition is met. ONCE_PER_INTERVAL - alert is triggered when the condition is met, then suppressed for the interval. If no interval is specified, it behaves as ALWAYS.  | [optional] [default to 'ALWAYS']

## Example

```python
from gooddata_api_client.models.json_api_automation_in_attributes_alert import JsonApiAutomationInAttributesAlert

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiAutomationInAttributesAlert from a JSON string
json_api_automation_in_attributes_alert_instance = JsonApiAutomationInAttributesAlert.from_json(json)
# print the JSON string representation of the object
print(JsonApiAutomationInAttributesAlert.to_json())

# convert the object into a dict
json_api_automation_in_attributes_alert_dict = json_api_automation_in_attributes_alert_instance.to_dict()
# create an instance of JsonApiAutomationInAttributesAlert from a dict
json_api_automation_in_attributes_alert_from_dict = JsonApiAutomationInAttributesAlert.from_dict(json_api_automation_in_attributes_alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


