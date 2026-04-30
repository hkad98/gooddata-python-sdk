# AacDashboardFilter

Tab-specific filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Date dataset reference. | [optional] 
**display_as** | **str** | Display as label. | [optional] 
**var_from** | [**AacDashboardFilterFrom**](AacDashboardFilterFrom.md) |  | [optional] 
**granularity** | **str** | Date granularity. | [optional] 
**metric_filters** | **List[str]** | Metric filters for validation. | [optional] 
**mode** | **str** | Filter mode. | [optional] 
**multiselect** | **bool** | Whether multiselect is enabled. | [optional] 
**parents** | **List[object]** | Parent filter references. | [optional] 
**state** | [**AacFilterState**](AacFilterState.md) |  | [optional] 
**title** | **str** | Filter title. | [optional] 
**to** | [**AacDashboardFilterFrom**](AacDashboardFilterFrom.md) |  | [optional] 
**type** | **str** | Filter type. | 
**using** | **str** | Attribute or label to filter by. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_dashboard_filter import AacDashboardFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AacDashboardFilter from a JSON string
aac_dashboard_filter_instance = AacDashboardFilter.from_json(json)
# print the JSON string representation of the object
print(AacDashboardFilter.to_json())

# convert the object into a dict
aac_dashboard_filter_dict = aac_dashboard_filter_instance.to_dict()
# create an instance of AacDashboardFilter from a dict
aac_dashboard_filter_from_dict = AacDashboardFilter.from_dict(aac_dashboard_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


