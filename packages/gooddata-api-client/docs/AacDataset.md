# AacDataset

AAC dataset definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_source** | **str** | Data source ID. | [optional] 
**description** | **str** | Dataset description. | [optional] 
**fields** | [**Dict[str, AacField]**](AacField.md) | Dataset fields (attributes, facts, aggregated facts). | [optional] 
**id** | **str** | Unique identifier of the dataset. | 
**precedence** | **int** | Precedence value for aggregate awareness. | [optional] 
**primary_key** | [**AacDatasetPrimaryKey**](AacDatasetPrimaryKey.md) |  | [optional] 
**references** | [**List[AacReference]**](AacReference.md) | References to other datasets. | [optional] 
**sql** | **str** | SQL statement defining this dataset. | [optional] 
**table_path** | **str** | Table path in the data source. | [optional] 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**type** | **str** | Dataset type discriminator. | 
**workspace_data_filters** | [**List[AacWorkspaceDataFilter]**](AacWorkspaceDataFilter.md) | Workspace data filters. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_dataset import AacDataset

# TODO update the JSON string below
json = "{}"
# create an instance of AacDataset from a JSON string
aac_dataset_instance = AacDataset.from_json(json)
# print the JSON string representation of the object
print(AacDataset.to_json())

# convert the object into a dict
aac_dataset_dict = aac_dataset_instance.to_dict()
# create an instance of AacDataset from a dict
aac_dataset_from_dict = AacDataset.from_dict(aac_dataset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


