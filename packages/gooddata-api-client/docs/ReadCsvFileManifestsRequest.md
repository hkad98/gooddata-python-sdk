# ReadCsvFileManifestsRequest

Request to read the manifests of the specified CSV files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest_requests** | [**List[ReadCsvFileManifestsRequestItem]**](ReadCsvFileManifestsRequestItem.md) | Files to read the manifests for. | 

## Example

```python
from gooddata_api_client.models.read_csv_file_manifests_request import ReadCsvFileManifestsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReadCsvFileManifestsRequest from a JSON string
read_csv_file_manifests_request_instance = ReadCsvFileManifestsRequest.from_json(json)
# print the JSON string representation of the object
print(ReadCsvFileManifestsRequest.to_json())

# convert the object into a dict
read_csv_file_manifests_request_dict = read_csv_file_manifests_request_instance.to_dict()
# create an instance of ReadCsvFileManifestsRequest from a dict
read_csv_file_manifests_request_from_dict = ReadCsvFileManifestsRequest.from_dict(read_csv_file_manifests_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


