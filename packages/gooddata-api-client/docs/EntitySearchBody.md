# EntitySearchBody

Request body for entity search operations

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter** | **str** | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 
**include** | **List[str]** | List of related entities to include in the response | [optional] 
**meta_include** | **List[str]** | Set of metadata fields to include in the response | [optional] 
**page** | [**EntitySearchPage**](EntitySearchPage.md) |  | [optional] 
**sort** | [**List[EntitySearchSort]**](EntitySearchSort.md) | Sorting criteria (can specify multiple sort orders) | [optional] 

## Example

```python
from gooddata_api_client.models.entity_search_body import EntitySearchBody

# TODO update the JSON string below
json = "{}"
# create an instance of EntitySearchBody from a JSON string
entity_search_body_instance = EntitySearchBody.from_json(json)
# print the JSON string representation of the object
print(EntitySearchBody.to_json())

# convert the object into a dict
entity_search_body_dict = entity_search_body_instance.to_dict()
# create an instance of EntitySearchBody from a dict
entity_search_body_from_dict = EntitySearchBody.from_dict(entity_search_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


