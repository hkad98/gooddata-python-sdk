# OutlierDetectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**ExecutionLinks**](ExecutionLinks.md) |  | 

## Example

```python
from gooddata_api_client.models.outlier_detection_response import OutlierDetectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OutlierDetectionResponse from a JSON string
outlier_detection_response_instance = OutlierDetectionResponse.from_json(json)
# print the JSON string representation of the object
print(OutlierDetectionResponse.to_json())

# convert the object into a dict
outlier_detection_response_dict = outlier_detection_response_instance.to_dict()
# create an instance of OutlierDetectionResponse from a dict
outlier_detection_response_from_dict = OutlierDetectionResponse.from_dict(outlier_detection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


