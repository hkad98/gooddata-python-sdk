# OutlierDetectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[AttributeItem]**](AttributeItem.md) | Attributes to be used in the computation. | 
**aux_measures** | [**List[MeasureItem]**](MeasureItem.md) | Metrics to be referenced from other AFM objects (e.g. filters) but not included in the result. | [optional] 
**filters** | [**List[ChangeAnalysisParamsFiltersInner]**](ChangeAnalysisParamsFiltersInner.md) | Various filter types to filter the execution result. | 
**granularity** | **str** | Date granularity for anomaly detection. Only time-based granularities are supported (HOUR, DAY, WEEK, MONTH, QUARTER, YEAR). | 
**measures** | [**List[MeasureItem]**](MeasureItem.md) |  | 
**sensitivity** | **str** | Sensitivity level for outlier detection | 

## Example

```python
from gooddata_api_client.models.outlier_detection_request import OutlierDetectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OutlierDetectionRequest from a JSON string
outlier_detection_request_instance = OutlierDetectionRequest.from_json(json)
# print the JSON string representation of the object
print(OutlierDetectionRequest.to_json())

# convert the object into a dict
outlier_detection_request_dict = outlier_detection_request_instance.to_dict()
# create an instance of OutlierDetectionRequest from a dict
outlier_detection_request_from_dict = OutlierDetectionRequest.from_dict(outlier_detection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


