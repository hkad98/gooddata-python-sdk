# GeoJsonGeometry

GeoJSON Geometry

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**coordinates** | **object** |  | 
**type** | **str** |  | 

## Example

```python
from gooddata_api_client.models.geo_json_geometry import GeoJsonGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonGeometry from a JSON string
geo_json_geometry_instance = GeoJsonGeometry.from_json(json)
# print the JSON string representation of the object
print(GeoJsonGeometry.to_json())

# convert the object into a dict
geo_json_geometry_dict = geo_json_geometry_instance.to_dict()
# create an instance of GeoJsonGeometry from a dict
geo_json_geometry_from_dict = GeoJsonGeometry.from_dict(geo_json_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


