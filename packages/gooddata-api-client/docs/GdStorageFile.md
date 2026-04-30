# GdStorageFile

File stored in GD Storage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**modified_at** | **datetime** | Last modification timestamp of the file. | 
**name** | **str** | Name of the file. | 
**size** | **int** | Size of the file in bytes. | 
**type** | **str** | Type of the file. | 

## Example

```python
from gooddata_api_client.models.gd_storage_file import GdStorageFile

# TODO update the JSON string below
json = "{}"
# create an instance of GdStorageFile from a JSON string
gd_storage_file_instance = GdStorageFile.from_json(json)
# print the JSON string representation of the object
print(GdStorageFile.to_json())

# convert the object into a dict
gd_storage_file_dict = gd_storage_file_instance.to_dict()
# create an instance of GdStorageFile from a dict
gd_storage_file_from_dict = GdStorageFile.from_dict(gd_storage_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


