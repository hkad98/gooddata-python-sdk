# JsonApiLabelPatchDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**JsonApiLabelPatch**](JsonApiLabelPatch.md) |  | 

## Example

```python
from gooddata_api_client.models.json_api_label_patch_document import JsonApiLabelPatchDocument

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiLabelPatchDocument from a JSON string
json_api_label_patch_document_instance = JsonApiLabelPatchDocument.from_json(json)
# print the JSON string representation of the object
print(JsonApiLabelPatchDocument.to_json())

# convert the object into a dict
json_api_label_patch_document_dict = json_api_label_patch_document_instance.to_dict()
# create an instance of JsonApiLabelPatchDocument from a dict
json_api_label_patch_document_from_dict = JsonApiLabelPatchDocument.from_dict(json_api_label_patch_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


