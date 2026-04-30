# DeclarativeCustomGeoCollections

Custom geo collections.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_geo_collections** | [**List[DeclarativeCustomGeoCollection]**](DeclarativeCustomGeoCollection.md) |  | 

## Example

```python
from gooddata_api_client.models.declarative_custom_geo_collections import DeclarativeCustomGeoCollections

# TODO update the JSON string below
json = "{}"
# create an instance of DeclarativeCustomGeoCollections from a JSON string
declarative_custom_geo_collections_instance = DeclarativeCustomGeoCollections.from_json(json)
# print the JSON string representation of the object
print(DeclarativeCustomGeoCollections.to_json())

# convert the object into a dict
declarative_custom_geo_collections_dict = declarative_custom_geo_collections_instance.to_dict()
# create an instance of DeclarativeCustomGeoCollections from a dict
declarative_custom_geo_collections_from_dict = DeclarativeCustomGeoCollections.from_dict(declarative_custom_geo_collections_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


