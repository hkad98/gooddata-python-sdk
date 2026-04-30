# AnomalyDetectionConfig

Anomaly detection configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sensitivity** | **str** | Outlier sensitivity level. | 

## Example

```python
from gooddata_api_client.models.anomaly_detection_config import AnomalyDetectionConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AnomalyDetectionConfig from a JSON string
anomaly_detection_config_instance = AnomalyDetectionConfig.from_json(json)
# print the JSON string representation of the object
print(AnomalyDetectionConfig.to_json())

# convert the object into a dict
anomaly_detection_config_dict = anomaly_detection_config_instance.to_dict()
# create an instance of AnomalyDetectionConfig from a dict
anomaly_detection_config_from_dict = AnomalyDetectionConfig.from_dict(anomaly_detection_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


