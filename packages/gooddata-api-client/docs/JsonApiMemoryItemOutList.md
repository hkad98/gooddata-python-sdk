# JsonApiMemoryItemOutList

A JSON:API document with a list of resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JsonApiMemoryItemOutWithLinks]**](JsonApiMemoryItemOutWithLinks.md) |  | 
**included** | [**List[JsonApiUserIdentifierOutWithLinks]**](JsonApiUserIdentifierOutWithLinks.md) | Included resources | [optional] 
**links** | [**ListLinks**](ListLinks.md) |  | [optional] 
**meta** | [**JsonApiAggregatedFactOutListMeta**](JsonApiAggregatedFactOutListMeta.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_memory_item_out_list import JsonApiMemoryItemOutList

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiMemoryItemOutList from a JSON string
json_api_memory_item_out_list_instance = JsonApiMemoryItemOutList.from_json(json)
# print the JSON string representation of the object
print(JsonApiMemoryItemOutList.to_json())

# convert the object into a dict
json_api_memory_item_out_list_dict = json_api_memory_item_out_list_instance.to_dict()
# create an instance of JsonApiMemoryItemOutList from a dict
json_api_memory_item_out_list_from_dict = JsonApiMemoryItemOutList.from_dict(json_api_memory_item_out_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


