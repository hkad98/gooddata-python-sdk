# AnalyzeCsvRequest

Bulk CSV analysis request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyze_requests** | [**List[AnalyzeCsvRequestItem]**](AnalyzeCsvRequestItem.md) | List of individual CSV analysis requests. | 

## Example

```python
from gooddata_api_client.models.analyze_csv_request import AnalyzeCsvRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyzeCsvRequest from a JSON string
analyze_csv_request_instance = AnalyzeCsvRequest.from_json(json)
# print the JSON string representation of the object
print(AnalyzeCsvRequest.to_json())

# convert the object into a dict
analyze_csv_request_dict = analyze_csv_request_instance.to_dict()
# create an instance of AnalyzeCsvRequest from a dict
analyze_csv_request_from_dict = AnalyzeCsvRequest.from_dict(analyze_csv_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


