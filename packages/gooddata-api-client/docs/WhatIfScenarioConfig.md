# WhatIfScenarioConfig

What-if scenario configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_baseline** | **bool** | Whether baseline (unmodified) values are included | 
**scenarios** | [**List[WhatIfScenarioItem]**](WhatIfScenarioItem.md) | Scenarios with alternative measure calculations | 

## Example

```python
from gooddata_api_client.models.what_if_scenario_config import WhatIfScenarioConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WhatIfScenarioConfig from a JSON string
what_if_scenario_config_instance = WhatIfScenarioConfig.from_json(json)
# print the JSON string representation of the object
print(WhatIfScenarioConfig.to_json())

# convert the object into a dict
what_if_scenario_config_dict = what_if_scenario_config_instance.to_dict()
# create an instance of WhatIfScenarioConfig from a dict
what_if_scenario_config_from_dict = WhatIfScenarioConfig.from_dict(what_if_scenario_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


