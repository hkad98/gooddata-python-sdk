# DashboardArbitraryAttributeFilterArbitraryAttributeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_form** | [**IdentifierRef**](IdentifierRef.md) |  | 
**filter_elements_by** | [**List[AttributeFilterParent]**](AttributeFilterParent.md) |  | [optional] 
**filter_elements_by_date** | [**List[AttributeFilterByDate]**](AttributeFilterByDate.md) |  | [optional] 
**local_identifier** | **str** |  | [optional] 
**negative_selection** | **bool** |  | 
**title** | **str** |  | [optional] 
**validate_elements_by** | [**List[IdentifierRef]**](IdentifierRef.md) |  | [optional] 
**values** | **List[str]** |  | 

## Example

```python
from gooddata_api_client.models.dashboard_arbitrary_attribute_filter_arbitrary_attribute_filter import DashboardArbitraryAttributeFilterArbitraryAttributeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardArbitraryAttributeFilterArbitraryAttributeFilter from a JSON string
dashboard_arbitrary_attribute_filter_arbitrary_attribute_filter_instance = DashboardArbitraryAttributeFilterArbitraryAttributeFilter.from_json(json)
# print the JSON string representation of the object
print(DashboardArbitraryAttributeFilterArbitraryAttributeFilter.to_json())

# convert the object into a dict
dashboard_arbitrary_attribute_filter_arbitrary_attribute_filter_dict = dashboard_arbitrary_attribute_filter_arbitrary_attribute_filter_instance.to_dict()
# create an instance of DashboardArbitraryAttributeFilterArbitraryAttributeFilter from a dict
dashboard_arbitrary_attribute_filter_arbitrary_attribute_filter_from_dict = DashboardArbitraryAttributeFilterArbitraryAttributeFilter.from_dict(dashboard_arbitrary_attribute_filter_arbitrary_attribute_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


