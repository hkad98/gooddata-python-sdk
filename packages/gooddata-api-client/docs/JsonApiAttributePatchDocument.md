# JsonApiAttributePatchDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**JsonApiAttributePatch**](JsonApiAttributePatch.md) |  | 

## Example

```python
from gooddata_api_client.models.json_api_attribute_patch_document import JsonApiAttributePatchDocument

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiAttributePatchDocument from a JSON string
json_api_attribute_patch_document_instance = JsonApiAttributePatchDocument.from_json(json)
# print the JSON string representation of the object
print(JsonApiAttributePatchDocument.to_json())

# convert the object into a dict
json_api_attribute_patch_document_dict = json_api_attribute_patch_document_instance.to_dict()
# create an instance of JsonApiAttributePatchDocument from a dict
json_api_attribute_patch_document_from_dict = JsonApiAttributePatchDocument.from_dict(json_api_attribute_patch_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


