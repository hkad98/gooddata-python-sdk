# AacReferenceSource

Source columns for the reference.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | Data type of the column. | [optional] 
**source_column** | **str** | Source column name. | 
**target** | **str** | Target in the referenced dataset. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_reference_source import AacReferenceSource

# TODO update the JSON string below
json = "{}"
# create an instance of AacReferenceSource from a JSON string
aac_reference_source_instance = AacReferenceSource.from_json(json)
# print the JSON string representation of the object
print(AacReferenceSource.to_json())

# convert the object into a dict
aac_reference_source_dict = aac_reference_source_instance.to_dict()
# create an instance of AacReferenceSource from a dict
aac_reference_source_from_dict = AacReferenceSource.from_dict(aac_reference_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


