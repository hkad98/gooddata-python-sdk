# AnomalyDetectionWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly** | [**AnomalyDetection**](AnomalyDetection.md) |  | 

## Example

```python
from gooddata_api_client.models.anomaly_detection_wrapper import AnomalyDetectionWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AnomalyDetectionWrapper from a JSON string
anomaly_detection_wrapper_instance = AnomalyDetectionWrapper.from_json(json)
# print the JSON string representation of the object
print(AnomalyDetectionWrapper.to_json())

# convert the object into a dict
anomaly_detection_wrapper_dict = anomaly_detection_wrapper_instance.to_dict()
# create an instance of AnomalyDetectionWrapper from a dict
anomaly_detection_wrapper_from_dict = AnomalyDetectionWrapper.from_dict(anomaly_detection_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


