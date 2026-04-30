# JsonApiAttributePatch

JSON:API representation of patching attribute entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**JsonApiAttributePatchAttributes**](JsonApiAttributePatchAttributes.md) |  | [optional] 
**id** | **str** | API identifier of an object | 
**relationships** | [**JsonApiAttributePatchRelationships**](JsonApiAttributePatchRelationships.md) |  | [optional] 
**type** | **str** | Object type | 

## Example

```python
from gooddata_api_client.models.json_api_attribute_patch import JsonApiAttributePatch

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiAttributePatch from a JSON string
json_api_attribute_patch_instance = JsonApiAttributePatch.from_json(json)
# print the JSON string representation of the object
print(JsonApiAttributePatch.to_json())

# convert the object into a dict
json_api_attribute_patch_dict = json_api_attribute_patch_instance.to_dict()
# create an instance of JsonApiAttributePatch from a dict
json_api_attribute_patch_from_dict = JsonApiAttributePatch.from_dict(json_api_attribute_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


