# AacField

AAC field definition (attribute, fact, or aggregated_fact).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregated_as** | **str** | Aggregation method. | [optional] 
**assigned_to** | **str** | Source fact ID for aggregated fact. | [optional] 
**data_type** | **str** | Data type of the column. | [optional] 
**default_view** | **str** | Default view label ID. | [optional] 
**description** | **str** | Field description. | [optional] 
**is_hidden** | **bool** | Deprecated. Use showInAiResults instead. | [optional] 
**labels** | [**Dict[str, AacLabel]**](AacLabel.md) | Attribute labels. | [optional] 
**locale** | **str** | Locale for sorting. | [optional] 
**show_in_ai_results** | **bool** | Whether to show in AI results. | [optional] 
**sort_column** | **str** | Sort column name. | [optional] 
**sort_direction** | **str** | Sort direction. | [optional] 
**source_column** | **str** | Source column in the physical database. | [optional] 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**type** | **str** | Field type. | 

## Example

```python
from gooddata_api_client.models.aac_field import AacField

# TODO update the JSON string below
json = "{}"
# create an instance of AacField from a JSON string
aac_field_instance = AacField.from_json(json)
# print the JSON string representation of the object
print(AacField.to_json())

# convert the object into a dict
aac_field_dict = aac_field_instance.to_dict()
# create an instance of AacField from a dict
aac_field_from_dict = AacField.from_dict(aac_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


