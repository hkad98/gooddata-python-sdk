# JsonApiDatasetPatchDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**JsonApiDatasetPatch**](JsonApiDatasetPatch.md) |  | 

## Example

```python
from gooddata_api_client.models.json_api_dataset_patch_document import JsonApiDatasetPatchDocument

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiDatasetPatchDocument from a JSON string
json_api_dataset_patch_document_instance = JsonApiDatasetPatchDocument.from_json(json)
# print the JSON string representation of the object
print(JsonApiDatasetPatchDocument.to_json())

# convert the object into a dict
json_api_dataset_patch_document_dict = json_api_dataset_patch_document_instance.to_dict()
# create an instance of JsonApiDatasetPatchDocument from a dict
json_api_dataset_patch_document_from_dict = JsonApiDatasetPatchDocument.from_dict(json_api_dataset_patch_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


