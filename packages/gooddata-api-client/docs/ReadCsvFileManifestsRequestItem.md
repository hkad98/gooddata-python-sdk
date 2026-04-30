# ReadCsvFileManifestsRequestItem

Request to read the manifest of a single CSV file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_name** | **str** | Name of the CSV file to read the manifest for. | 
**version** | **int** | Optional version of the file to read the manifest for. If null or not specified, the latest version is read. | [optional] 

## Example

```python
from gooddata_api_client.models.read_csv_file_manifests_request_item import ReadCsvFileManifestsRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReadCsvFileManifestsRequestItem from a JSON string
read_csv_file_manifests_request_item_instance = ReadCsvFileManifestsRequestItem.from_json(json)
# print the JSON string representation of the object
print(ReadCsvFileManifestsRequestItem.to_json())

# convert the object into a dict
read_csv_file_manifests_request_item_dict = read_csv_file_manifests_request_item_instance.to_dict()
# create an instance of ReadCsvFileManifestsRequestItem from a dict
read_csv_file_manifests_request_item_from_dict = ReadCsvFileManifestsRequestItem.from_dict(read_csv_file_manifests_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


