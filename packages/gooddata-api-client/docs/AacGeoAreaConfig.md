# AacGeoAreaConfig

GEO area configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection** | [**AacGeoCollectionIdentifier**](AacGeoCollectionIdentifier.md) |  | 

## Example

```python
from gooddata_api_client.models.aac_geo_area_config import AacGeoAreaConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AacGeoAreaConfig from a JSON string
aac_geo_area_config_instance = AacGeoAreaConfig.from_json(json)
# print the JSON string representation of the object
print(AacGeoAreaConfig.to_json())

# convert the object into a dict
aac_geo_area_config_dict = aac_geo_area_config_instance.to_dict()
# create an instance of AacGeoAreaConfig from a dict
aac_geo_area_config_from_dict = AacGeoAreaConfig.from_dict(aac_geo_area_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


