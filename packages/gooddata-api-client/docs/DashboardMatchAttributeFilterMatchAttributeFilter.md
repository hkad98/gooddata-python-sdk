# DashboardMatchAttributeFilterMatchAttributeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**case_sensitive** | **bool** |  | 
**display_form** | [**IdentifierRef**](IdentifierRef.md) |  | 
**literal** | **str** |  | 
**local_identifier** | **str** |  | [optional] 
**negative_selection** | **bool** |  | 
**operator** | **str** |  | 
**title** | **str** |  | [optional] 

## Example

```python
from gooddata_api_client.models.dashboard_match_attribute_filter_match_attribute_filter import DashboardMatchAttributeFilterMatchAttributeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardMatchAttributeFilterMatchAttributeFilter from a JSON string
dashboard_match_attribute_filter_match_attribute_filter_instance = DashboardMatchAttributeFilterMatchAttributeFilter.from_json(json)
# print the JSON string representation of the object
print(DashboardMatchAttributeFilterMatchAttributeFilter.to_json())

# convert the object into a dict
dashboard_match_attribute_filter_match_attribute_filter_dict = dashboard_match_attribute_filter_match_attribute_filter_instance.to_dict()
# create an instance of DashboardMatchAttributeFilterMatchAttributeFilter from a dict
dashboard_match_attribute_filter_match_attribute_filter_from_dict = DashboardMatchAttributeFilterMatchAttributeFilter.from_dict(dashboard_match_attribute_filter_match_attribute_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


