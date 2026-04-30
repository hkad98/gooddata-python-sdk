# JsonApiCustomGeoCollectionIn

JSON:API representation of customGeoCollection entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**JsonApiCustomGeoCollectionInAttributes**](JsonApiCustomGeoCollectionInAttributes.md) |  | [optional] 
**id** | **str** | API identifier of an object | 
**type** | **str** | Object type | 

## Example

```python
from gooddata_api_client.models.json_api_custom_geo_collection_in import JsonApiCustomGeoCollectionIn

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiCustomGeoCollectionIn from a JSON string
json_api_custom_geo_collection_in_instance = JsonApiCustomGeoCollectionIn.from_json(json)
# print the JSON string representation of the object
print(JsonApiCustomGeoCollectionIn.to_json())

# convert the object into a dict
json_api_custom_geo_collection_in_dict = json_api_custom_geo_collection_in_instance.to_dict()
# create an instance of JsonApiCustomGeoCollectionIn from a dict
json_api_custom_geo_collection_in_from_dict = JsonApiCustomGeoCollectionIn.from_dict(json_api_custom_geo_collection_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


