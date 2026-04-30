# VisualizationConfig

Visualization config for smart-function rendering.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly_detection** | [**AnomalyDetectionConfig**](AnomalyDetectionConfig.md) |  | [optional] 
**clustering** | [**ClusteringConfig**](ClusteringConfig.md) |  | [optional] 
**forecast** | [**ForecastConfig**](ForecastConfig.md) |  | [optional] 
**what_if** | [**WhatIfScenarioConfig**](WhatIfScenarioConfig.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.visualization_config import VisualizationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VisualizationConfig from a JSON string
visualization_config_instance = VisualizationConfig.from_json(json)
# print the JSON string representation of the object
print(VisualizationConfig.to_json())

# convert the object into a dict
visualization_config_dict = visualization_config_instance.to_dict()
# create an instance of VisualizationConfig from a dict
visualization_config_from_dict = VisualizationConfig.from_dict(visualization_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


