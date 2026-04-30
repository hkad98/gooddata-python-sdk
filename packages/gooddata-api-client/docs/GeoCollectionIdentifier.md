# GeoCollectionIdentifier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Geo collection identifier. | 
**kind** | **str** | Type of geo collection. | [optional] [default to 'STATIC']

## Example

```python
from gooddata_api_client.models.geo_collection_identifier import GeoCollectionIdentifier

# TODO update the JSON string below
json = "{}"
# create an instance of GeoCollectionIdentifier from a JSON string
geo_collection_identifier_instance = GeoCollectionIdentifier.from_json(json)
# print the JSON string representation of the object
print(GeoCollectionIdentifier.to_json())

# convert the object into a dict
geo_collection_identifier_dict = geo_collection_identifier_instance.to_dict()
# create an instance of GeoCollectionIdentifier from a dict
geo_collection_identifier_from_dict = GeoCollectionIdentifier.from_dict(geo_collection_identifier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


