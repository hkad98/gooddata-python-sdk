# AacDateDataset

AAC date dataset definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Date dataset description. | [optional] 
**granularities** | **List[str]** | List of granularities. | [optional] 
**id** | **str** | Unique identifier of the date dataset. | 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**title_base** | **str** | Title base for formatting. | [optional] 
**title_pattern** | **str** | Title pattern for formatting. | [optional] 
**type** | **str** | Dataset type discriminator. | 

## Example

```python
from gooddata_api_client.models.aac_date_dataset import AacDateDataset

# TODO update the JSON string below
json = "{}"
# create an instance of AacDateDataset from a JSON string
aac_date_dataset_instance = AacDateDataset.from_json(json)
# print the JSON string representation of the object
print(AacDateDataset.to_json())

# convert the object into a dict
aac_date_dataset_dict = aac_date_dataset_instance.to_dict()
# create an instance of AacDateDataset from a dict
aac_date_dataset_from_dict = AacDateDataset.from_dict(aac_date_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


