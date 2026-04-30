# ConvertGeoFileRequest

Request to convert a geo file to GeoParquet format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Location of the file in the staging area to convert. | 

## Example

```python
from gooddata_api_client.models.convert_geo_file_request import ConvertGeoFileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertGeoFileRequest from a JSON string
convert_geo_file_request_instance = ConvertGeoFileRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertGeoFileRequest.to_json())

# convert the object into a dict
convert_geo_file_request_dict = convert_geo_file_request_instance.to_dict()
# create an instance of ConvertGeoFileRequest from a dict
convert_geo_file_request_from_dict = ConvertGeoFileRequest.from_dict(convert_geo_file_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


