# EntitySearchSort

Sorting criteria for entity search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**direction** | **str** | Sort direction | [optional] [default to 'ASC']
**var_property** | **str** | Property name to sort by | 

## Example

```python
from gooddata_api_client.models.entity_search_sort import EntitySearchSort

# TODO update the JSON string below
json = "{}"
# create an instance of EntitySearchSort from a JSON string
entity_search_sort_instance = EntitySearchSort.from_json(json)
# print the JSON string representation of the object
print(EntitySearchSort.to_json())

# convert the object into a dict
entity_search_sort_dict = entity_search_sort_instance.to_dict()
# create an instance of EntitySearchSort from a dict
entity_search_sort_from_dict = EntitySearchSort.from_dict(entity_search_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


