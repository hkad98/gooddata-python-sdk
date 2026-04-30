# AnomalyDetection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | [**AfmObjectIdentifierDataset**](AfmObjectIdentifierDataset.md) |  | 
**granularity** | **str** | Date granularity for anomaly detection. Only time-based granularities are supported (HOUR, DAY, WEEK, MONTH, QUARTER, YEAR). | 
**measure** | [**LocalIdentifier**](LocalIdentifier.md) |  | 
**sensitivity** | **str** | Sensitivity level for anomaly detection | 

## Example

```python
from gooddata_api_client.models.anomaly_detection import AnomalyDetection

# TODO update the JSON string below
json = "{}"
# create an instance of AnomalyDetection from a JSON string
anomaly_detection_instance = AnomalyDetection.from_json(json)
# print the JSON string representation of the object
print(AnomalyDetection.to_json())

# convert the object into a dict
anomaly_detection_dict = anomaly_detection_instance.to_dict()
# create an instance of AnomalyDetection from a dict
anomaly_detection_from_dict = AnomalyDetection.from_dict(anomaly_detection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


