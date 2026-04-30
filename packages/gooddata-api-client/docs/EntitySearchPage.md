# EntitySearchPage

Pagination information for entity search

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **int** | Zero-based page index | [default to 0]
**size** | **int** | Number of items per page | [default to 100]

## Example

```python
from gooddata_api_client.models.entity_search_page import EntitySearchPage

# TODO update the JSON string below
json = "{}"
# create an instance of EntitySearchPage from a JSON string
entity_search_page_instance = EntitySearchPage.from_json(json)
# print the JSON string representation of the object
print(EntitySearchPage.to_json())

# convert the object into a dict
entity_search_page_dict = entity_search_page_instance.to_dict()
# create an instance of EntitySearchPage from a dict
entity_search_page_from_dict = EntitySearchPage.from_dict(entity_search_page_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


