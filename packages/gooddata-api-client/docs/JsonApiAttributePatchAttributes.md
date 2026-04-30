# JsonApiAttributePatchAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_attribute_patch_attributes import JsonApiAttributePatchAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiAttributePatchAttributes from a JSON string
json_api_attribute_patch_attributes_instance = JsonApiAttributePatchAttributes.from_json(json)
# print the JSON string representation of the object
print(JsonApiAttributePatchAttributes.to_json())

# convert the object into a dict
json_api_attribute_patch_attributes_dict = json_api_attribute_patch_attributes_instance.to_dict()
# create an instance of JsonApiAttributePatchAttributes from a dict
json_api_attribute_patch_attributes_from_dict = JsonApiAttributePatchAttributes.from_dict(json_api_attribute_patch_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


