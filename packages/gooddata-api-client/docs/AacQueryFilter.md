# AacQueryFilter

Layer filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **Dict[str, object]** |  | [optional] 
**attribute** | **str** | Attribute for ranking filter (identifier or localId). | [optional] 
**bottom** | **int** | Bottom N for ranking filter. | [optional] 
**condition** | **str** | Condition for metric value filter. | [optional] 
**dimensionality** | **List[str]** | Dimensionality for metric value filter. | [optional] 
**display_as** | **str** | Display as label (attribute filter). | [optional] 
**var_from** | [**AacDashboardFilterFrom**](AacDashboardFilterFrom.md) |  | [optional] 
**granularity** | **str** | Date granularity (date filter). | [optional] 
**null_values_as_zero** | **bool** | Null values are treated as zero (metric value filter). | [optional] 
**state** | [**AacFilterState**](AacFilterState.md) |  | [optional] 
**to** | [**AacDashboardFilterFrom**](AacDashboardFilterFrom.md) |  | [optional] 
**top** | **int** | Top N for ranking filter. | [optional] 
**type** | **str** | Filter type. | 
**using** | **str** | Reference to attribute/label/date/metric/fact (type-prefixed id). | [optional] 
**value** | **float** | Value for metric value filter. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_query_filter import AacQueryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AacQueryFilter from a JSON string
aac_query_filter_instance = AacQueryFilter.from_json(json)
# print the JSON string representation of the object
print(AacQueryFilter.to_json())

# convert the object into a dict
aac_query_filter_dict = aac_query_filter_instance.to_dict()
# create an instance of AacQueryFilter from a dict
aac_query_filter_from_dict = AacQueryFilter.from_dict(aac_query_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


