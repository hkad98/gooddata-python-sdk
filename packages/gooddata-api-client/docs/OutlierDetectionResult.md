# OutlierDetectionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **List[str]** | Attribute values for outlier detection results. | 
**values** | **Dict[str, Optional[List[Optional[float]]]]** | Map of measure identifiers to their outlier detection values. Each value is a list of nullable numbers. | 

## Example

```python
from gooddata_api_client.models.outlier_detection_result import OutlierDetectionResult

# TODO update the JSON string below
json = "{}"
# create an instance of OutlierDetectionResult from a JSON string
outlier_detection_result_instance = OutlierDetectionResult.from_json(json)
# print the JSON string representation of the object
print(OutlierDetectionResult.to_json())

# convert the object into a dict
outlier_detection_result_dict = outlier_detection_result_instance.to_dict()
# create an instance of OutlierDetectionResult from a dict
outlier_detection_result_from_dict = OutlierDetectionResult.from_dict(outlier_detection_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


