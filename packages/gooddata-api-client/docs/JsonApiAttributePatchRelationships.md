# JsonApiAttributePatchRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default_view** | [**JsonApiAttributeOutRelationshipsDefaultView**](JsonApiAttributeOutRelationshipsDefaultView.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_attribute_patch_relationships import JsonApiAttributePatchRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiAttributePatchRelationships from a JSON string
json_api_attribute_patch_relationships_instance = JsonApiAttributePatchRelationships.from_json(json)
# print the JSON string representation of the object
print(JsonApiAttributePatchRelationships.to_json())

# convert the object into a dict
json_api_attribute_patch_relationships_dict = json_api_attribute_patch_relationships_instance.to_dict()
# create an instance of JsonApiAttributePatchRelationships from a dict
json_api_attribute_patch_relationships_from_dict = JsonApiAttributePatchRelationships.from_dict(json_api_attribute_patch_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


