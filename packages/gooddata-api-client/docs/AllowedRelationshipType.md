# AllowedRelationshipType

Allowed relationship type combination.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_orphans** | **bool** | If true, allows target objects that are not part of any relationship (orphans) to be included in results. If false, orphan target objects will be excluded even if they directly match the search query. Default is true (orphans are allowed). | [optional] [default to True]
**source_type** | **str** | Source object type (e.g., &#39;dashboard&#39;, &#39;visualization&#39;, &#39;metric&#39;). | 
**target_type** | **str** | Target object type (e.g., &#39;visualization&#39;, &#39;metric&#39;, &#39;attribute&#39;). | 

## Example

```python
from gooddata_api_client.models.allowed_relationship_type import AllowedRelationshipType

# TODO update the JSON string below
json = "{}"
# create an instance of AllowedRelationshipType from a JSON string
allowed_relationship_type_instance = AllowedRelationshipType.from_json(json)
# print the JSON string representation of the object
print(AllowedRelationshipType.to_json())

# convert the object into a dict
allowed_relationship_type_dict = allowed_relationship_type_instance.to_dict()
# create an instance of AllowedRelationshipType from a dict
allowed_relationship_type_from_dict = AllowedRelationshipType.from_dict(allowed_relationship_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


