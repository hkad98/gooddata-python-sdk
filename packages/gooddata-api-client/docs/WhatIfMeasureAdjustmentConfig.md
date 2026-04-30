# WhatIfMeasureAdjustmentConfig

Measure adjustments for this scenario

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metric_id** | **str** | ID of the metric or fact to adjust | 
**metric_type** | **str** | Type: metric or fact | 
**scenario_maql** | **str** | Alternative MAQL expression for this scenario | 

## Example

```python
from gooddata_api_client.models.what_if_measure_adjustment_config import WhatIfMeasureAdjustmentConfig

# TODO update the JSON string below
json = "{}"
# create an instance of WhatIfMeasureAdjustmentConfig from a JSON string
what_if_measure_adjustment_config_instance = WhatIfMeasureAdjustmentConfig.from_json(json)
# print the JSON string representation of the object
print(WhatIfMeasureAdjustmentConfig.to_json())

# convert the object into a dict
what_if_measure_adjustment_config_dict = what_if_measure_adjustment_config_instance.to_dict()
# create an instance of WhatIfMeasureAdjustmentConfig from a dict
what_if_measure_adjustment_config_from_dict = WhatIfMeasureAdjustmentConfig.from_dict(what_if_measure_adjustment_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


