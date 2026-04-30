# AacLogicalModel

AAC logical data model representation compatible with Analytics-as-Code YAML format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datasets** | [**List[AacDataset]**](AacDataset.md) | An array of datasets. | [optional] 
**date_datasets** | [**List[AacDateDataset]**](AacDateDataset.md) | An array of date datasets. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_logical_model import AacLogicalModel

# TODO update the JSON string below
json = "{}"
# create an instance of AacLogicalModel from a JSON string
aac_logical_model_instance = AacLogicalModel.from_json(json)
# print the JSON string representation of the object
print(AacLogicalModel.to_json())

# convert the object into a dict
aac_logical_model_dict = aac_logical_model_instance.to_dict()
# create an instance of AacLogicalModel from a dict
aac_logical_model_from_dict = AacLogicalModel.from_dict(aac_logical_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


