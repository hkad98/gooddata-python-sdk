# GeoAreaConfig

Configuration specific to geo area labels.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**GeoCollectionIdentifier**](GeoCollectionIdentifier.md) |  | 

## Example

```python
from gooddata_api_client.models.geo_area_config import GeoAreaConfig

# TODO update the JSON string below
json = "{}"
# create an instance of GeoAreaConfig from a JSON string
geo_area_config_instance = GeoAreaConfig.from_json(json)
# print the JSON string representation of the object
print(GeoAreaConfig.to_json())

# convert the object into a dict
geo_area_config_dict = geo_area_config_instance.to_dict()
# create an instance of GeoAreaConfig from a dict
geo_area_config_from_dict = GeoAreaConfig.from_dict(geo_area_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


