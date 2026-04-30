# DeleteFilesRequest

Request to delete files from the storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_names** | **List[str]** | Names of the files to delete. | 

## Example

```python
from gooddata_api_client.models.delete_files_request import DeleteFilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteFilesRequest from a JSON string
delete_files_request_instance = DeleteFilesRequest.from_json(json)
# print the JSON string representation of the object
print(DeleteFilesRequest.to_json())

# convert the object into a dict
delete_files_request_dict = delete_files_request_instance.to_dict()
# create an instance of DeleteFilesRequest from a dict
delete_files_request_from_dict = DeleteFilesRequest.from_dict(delete_files_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


