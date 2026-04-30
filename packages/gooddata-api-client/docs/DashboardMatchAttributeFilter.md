# DashboardMatchAttributeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_attribute_filter** | [**DashboardMatchAttributeFilterMatchAttributeFilter**](DashboardMatchAttributeFilterMatchAttributeFilter.md) |  | 

## Example

```python
from gooddata_api_client.models.dashboard_match_attribute_filter import DashboardMatchAttributeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardMatchAttributeFilter from a JSON string
dashboard_match_attribute_filter_instance = DashboardMatchAttributeFilter.from_json(json)
# print the JSON string representation of the object
print(DashboardMatchAttributeFilter.to_json())

# convert the object into a dict
dashboard_match_attribute_filter_dict = dashboard_match_attribute_filter_instance.to_dict()
# create an instance of DashboardMatchAttributeFilter from a dict
dashboard_match_attribute_filter_from_dict = DashboardMatchAttributeFilter.from_dict(dashboard_match_attribute_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


