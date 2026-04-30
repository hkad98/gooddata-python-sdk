# AacSection

Sections within the tab.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Section description. | [optional] 
**header** | **bool** | Whether section header is visible. | [optional] 
**title** | **str** | Section title. | [optional] 
**widgets** | [**List[AacWidget]**](AacWidget.md) | Widgets in the section. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_section import AacSection

# TODO update the JSON string below
json = "{}"
# create an instance of AacSection from a JSON string
aac_section_instance = AacSection.from_json(json)
# print the JSON string representation of the object
print(AacSection.to_json())

# convert the object into a dict
aac_section_dict = aac_section_instance.to_dict()
# create an instance of AacSection from a dict
aac_section_from_dict = AacSection.from_dict(aac_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


