# ReadCsvFileManifestsResponse

Describes the results of a CSV manifest read of a single file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manifest** | [**CsvManifestBody**](CsvManifestBody.md) |  | 
**name** | **str** | Name of the file in the source data source. | 
**version** | **int** | Version of the file in the source data source. | 

## Example

```python
from gooddata_api_client.models.read_csv_file_manifests_response import ReadCsvFileManifestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReadCsvFileManifestsResponse from a JSON string
read_csv_file_manifests_response_instance = ReadCsvFileManifestsResponse.from_json(json)
# print the JSON string representation of the object
print(ReadCsvFileManifestsResponse.to_json())

# convert the object into a dict
read_csv_file_manifests_response_dict = read_csv_file_manifests_response_instance.to_dict()
# create an instance of ReadCsvFileManifestsResponse from a dict
read_csv_file_manifests_response_from_dict = ReadCsvFileManifestsResponse.from_dict(read_csv_file_manifests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


