# AacReference

AAC reference to another dataset.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dataset** | **str** | Target dataset ID. | 
**multi_directional** | **bool** | Whether the reference is multi-directional. | [optional] 
**sources** | [**List[AacReferenceSource]**](AacReferenceSource.md) | Source columns for the reference. | 

## Example

```python
from gooddata_api_client.models.aac_reference import AacReference

# TODO update the JSON string below
json = "{}"
# create an instance of AacReference from a JSON string
aac_reference_instance = AacReference.from_json(json)
# print the JSON string representation of the object
print(AacReference.to_json())

# convert the object into a dict
aac_reference_dict = aac_reference_instance.to_dict()
# create an instance of AacReference from a dict
aac_reference_from_dict = AacReference.from_dict(aac_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


