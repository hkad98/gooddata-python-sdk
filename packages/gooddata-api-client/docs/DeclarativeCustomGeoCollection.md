# DeclarativeCustomGeoCollection

A declarative form of custom geo collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the custom geo collection. | [optional] 
**id** | **str** | Custom geo collection ID. | 
**name** | **str** | Name of the custom geo collection. | [optional] 

## Example

```python
from gooddata_api_client.models.declarative_custom_geo_collection import DeclarativeCustomGeoCollection

# TODO update the JSON string below
json = "{}"
# create an instance of DeclarativeCustomGeoCollection from a JSON string
declarative_custom_geo_collection_instance = DeclarativeCustomGeoCollection.from_json(json)
# print the JSON string representation of the object
print(DeclarativeCustomGeoCollection.to_json())

# convert the object into a dict
declarative_custom_geo_collection_dict = declarative_custom_geo_collection_instance.to_dict()
# create an instance of DeclarativeCustomGeoCollection from a dict
declarative_custom_geo_collection_from_dict = DeclarativeCustomGeoCollection.from_dict(declarative_custom_geo_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


