# AacGeoCollectionIdentifier

GEO collection configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Collection identifier. | 
**kind** | **str** | Type of geo collection. | [optional] [default to 'STATIC']

## Example

```python
from gooddata_api_client.models.aac_geo_collection_identifier import AacGeoCollectionIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of AacGeoCollectionIdentifier from a JSON string
aac_geo_collection_identifier_instance = AacGeoCollectionIdentifier.from_json(json)
# print the JSON string representation of the object
print(AacGeoCollectionIdentifier.to_json())

# convert the object into a dict
aac_geo_collection_identifier_dict = aac_geo_collection_identifier_instance.to_dict()
# create an instance of AacGeoCollectionIdentifier from a dict
aac_geo_collection_identifier_from_dict = AacGeoCollectionIdentifier.from_dict(aac_geo_collection_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


