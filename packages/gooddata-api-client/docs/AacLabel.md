# AacLabel

AAC label definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_type** | **str** | Data type of the column. | [optional] 
**description** | **str** | Label description. | [optional] 
**geo_area_config** | [**AacGeoAreaConfig**](AacGeoAreaConfig.md) |  | [optional] 
**is_hidden** | **bool** | Deprecated. Use showInAiResults instead. | [optional] 
**locale** | **str** | Locale for sorting. | [optional] 
**show_in_ai_results** | **bool** | Whether to show in AI results. | [optional] 
**source_column** | **str** | Source column name. | [optional] 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**translations** | [**List[AacLabelTranslation]**](AacLabelTranslation.md) | Localized source columns. | [optional] 
**value_type** | **str** | Value type. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_label import AacLabel

# TODO update the JSON string below
json = "{}"
# create an instance of AacLabel from a JSON string
aac_label_instance = AacLabel.from_json(json)
# print the JSON string representation of the object
print(AacLabel.to_json())

# convert the object into a dict
aac_label_dict = aac_label_instance.to_dict()
# create an instance of AacLabel from a dict
aac_label_from_dict = AacLabel.from_dict(aac_label_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


