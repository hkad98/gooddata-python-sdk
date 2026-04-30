# WhatIfScenarioItem

Scenarios with alternative measure calculations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustments** | [**List[WhatIfMeasureAdjustmentConfig]**](WhatIfMeasureAdjustmentConfig.md) | Measure adjustments for this scenario | 
**label** | **str** | Human-readable scenario label | 

## Example

```python
from gooddata_api_client.models.what_if_scenario_item import WhatIfScenarioItem

# TODO update the JSON string below
json = "{}"
# create an instance of WhatIfScenarioItem from a JSON string
what_if_scenario_item_instance = WhatIfScenarioItem.from_json(json)
# print the JSON string representation of the object
print(WhatIfScenarioItem.to_json())

# convert the object into a dict
what_if_scenario_item_dict = what_if_scenario_item_instance.to_dict()
# create an instance of WhatIfScenarioItem from a dict
what_if_scenario_item_from_dict = WhatIfScenarioItem.from_dict(what_if_scenario_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


