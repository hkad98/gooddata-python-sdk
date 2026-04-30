# GeoJsonFeatureCollection

GeoJSON FeatureCollection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bbox** | **List[float]** |  | [optional] 
**features** | [**List[GeoJsonFeature]**](GeoJsonFeature.md) |  | 
**type** | **str** |  | 

## Example

```python
from gooddata_api_client.models.geo_json_feature_collection import GeoJsonFeatureCollection

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJsonFeatureCollection from a JSON string
geo_json_feature_collection_instance = GeoJsonFeatureCollection.from_json(json)
# print the JSON string representation of the object
print(GeoJsonFeatureCollection.to_json())

# convert the object into a dict
geo_json_feature_collection_dict = geo_json_feature_collection_instance.to_dict()
# create an instance of GeoJsonFeatureCollection from a dict
geo_json_feature_collection_from_dict = GeoJsonFeatureCollection.from_dict(geo_json_feature_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


