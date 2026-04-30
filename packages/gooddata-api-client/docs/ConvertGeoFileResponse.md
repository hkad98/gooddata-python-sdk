# ConvertGeoFileResponse

Response after successfully converting a geo file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Location of the converted GeoParquet file in the staging area. | 

## Example

```python
from gooddata_api_client.models.convert_geo_file_response import ConvertGeoFileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertGeoFileResponse from a JSON string
convert_geo_file_response_instance = ConvertGeoFileResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertGeoFileResponse.to_json())

# convert the object into a dict
convert_geo_file_response_dict = convert_geo_file_response_instance.to_dict()
# create an instance of ConvertGeoFileResponse from a dict
convert_geo_file_response_from_dict = ConvertGeoFileResponse.from_dict(convert_geo_file_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


