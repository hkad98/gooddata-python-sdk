# JsonApiCustomGeoCollectionOutList

A JSON:API document with a list of resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JsonApiCustomGeoCollectionOutWithLinks]**](JsonApiCustomGeoCollectionOutWithLinks.md) |  | 
**links** | [**ListLinks**](ListLinks.md) |  | [optional] 
**meta** | [**JsonApiAggregatedFactOutListMeta**](JsonApiAggregatedFactOutListMeta.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_custom_geo_collection_out_list import JsonApiCustomGeoCollectionOutList

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiCustomGeoCollectionOutList from a JSON string
json_api_custom_geo_collection_out_list_instance = JsonApiCustomGeoCollectionOutList.from_json(json)
# print the JSON string representation of the object
print(JsonApiCustomGeoCollectionOutList.to_json())

# convert the object into a dict
json_api_custom_geo_collection_out_list_dict = json_api_custom_geo_collection_out_list_instance.to_dict()
# create an instance of JsonApiCustomGeoCollectionOutList from a dict
json_api_custom_geo_collection_out_list_from_dict = JsonApiCustomGeoCollectionOutList.from_dict(json_api_custom_geo_collection_out_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


