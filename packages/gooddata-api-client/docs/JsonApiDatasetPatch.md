# JsonApiDatasetPatch

JSON:API representation of patching dataset entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**JsonApiAttributePatchAttributes**](JsonApiAttributePatchAttributes.md) |  | [optional] 
**id** | **str** | API identifier of an object | 
**type** | **str** | Object type | 

## Example

```python
from gooddata_api_client.models.json_api_dataset_patch import JsonApiDatasetPatch

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiDatasetPatch from a JSON string
json_api_dataset_patch_instance = JsonApiDatasetPatch.from_json(json)
# print the JSON string representation of the object
print(JsonApiDatasetPatch.to_json())

# convert the object into a dict
json_api_dataset_patch_dict = json_api_dataset_patch_instance.to_dict()
# create an instance of JsonApiDatasetPatch from a dict
json_api_dataset_patch_from_dict = JsonApiDatasetPatch.from_dict(json_api_dataset_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


