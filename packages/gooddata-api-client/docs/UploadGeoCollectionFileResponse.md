# UploadGeoCollectionFileResponse

Information related to the geo collection file uploaded to the staging area.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Location to use when referencing the uploaded file in subsequent requests. | 

## Example

```python
from gooddata_api_client.models.upload_geo_collection_file_response import UploadGeoCollectionFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadGeoCollectionFileResponse from a JSON string
upload_geo_collection_file_response_instance = UploadGeoCollectionFileResponse.from_json(json)
# print the JSON string representation of the object
print(UploadGeoCollectionFileResponse.to_json())

# convert the object into a dict
upload_geo_collection_file_response_dict = upload_geo_collection_file_response_instance.to_dict()
# create an instance of UploadGeoCollectionFileResponse from a dict
upload_geo_collection_file_response_from_dict = UploadGeoCollectionFileResponse.from_dict(upload_geo_collection_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


