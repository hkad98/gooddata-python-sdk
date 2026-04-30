# JsonApiCustomGeoCollectionOut

JSON:API representation of customGeoCollection entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**JsonApiCustomGeoCollectionInAttributes**](JsonApiCustomGeoCollectionInAttributes.md) |  | [optional] 
**id** | **str** | API identifier of an object | 
**type** | **str** | Object type | 

## Example

```python
from gooddata_api_client.models.json_api_custom_geo_collection_out import JsonApiCustomGeoCollectionOut

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiCustomGeoCollectionOut from a JSON string
json_api_custom_geo_collection_out_instance = JsonApiCustomGeoCollectionOut.from_json(json)
# print the JSON string representation of the object
print(JsonApiCustomGeoCollectionOut.to_json())

# convert the object into a dict
json_api_custom_geo_collection_out_dict = json_api_custom_geo_collection_out_instance.to_dict()
# create an instance of JsonApiCustomGeoCollectionOut from a dict
json_api_custom_geo_collection_out_from_dict = JsonApiCustomGeoCollectionOut.from_dict(json_api_custom_geo_collection_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


