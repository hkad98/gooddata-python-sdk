# JsonApiLabelPatch

JSON:API representation of patching label entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**JsonApiAttributePatchAttributes**](JsonApiAttributePatchAttributes.md) |  | [optional] 
**id** | **str** | API identifier of an object | 
**type** | **str** | Object type | 

## Example

```python
from gooddata_api_client.models.json_api_label_patch import JsonApiLabelPatch

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiLabelPatch from a JSON string
json_api_label_patch_instance = JsonApiLabelPatch.from_json(json)
# print the JSON string representation of the object
print(JsonApiLabelPatch.to_json())

# convert the object into a dict
json_api_label_patch_dict = json_api_label_patch_instance.to_dict()
# create an instance of JsonApiLabelPatch from a dict
json_api_label_patch_from_dict = JsonApiLabelPatch.from_dict(json_api_label_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


