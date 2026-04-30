# AacDashboardWithTabs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_tab_id** | **str** | Active tab ID for tabbed dashboards. | [optional] 
**cross_filtering** | **bool** | Whether cross filtering is enabled. | [optional] 
**description** | **str** | Dashboard description. | [optional] 
**enable_section_headers** | **bool** | Whether section headers are enabled. | [optional] 
**filter_views** | **bool** | Whether filter views are enabled. | [optional] 
**filters** | [**Dict[str, AacDashboardFilter]**](AacDashboardFilter.md) | Dashboard filters. | [optional] 
**id** | **str** | Unique identifier of the dashboard. | 
**permissions** | [**AacDashboardPermissions**](AacDashboardPermissions.md) |  | [optional] 
**plugins** | [**List[AacDashboardWithTabsAllOfPlugins]**](AacDashboardWithTabsAllOfPlugins.md) | Dashboard plugins. | [optional] 
**sections** | [**List[AacSection]**](AacSection.md) | Dashboard sections (for non-tabbed dashboards). | [optional] 
**tabs** | [**List[AacTab]**](AacTab.md) | Dashboard tabs (for tabbed dashboards). | 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**type** | **str** | Dashboard type discriminator. | 
**user_filters_reset** | **bool** | Whether user can reset custom filters. | [optional] 
**user_filters_save** | **bool** | Whether user filter settings are stored. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_dashboard_with_tabs import AacDashboardWithTabs

# TODO update the JSON string below
json = "{}"
# create an instance of AacDashboardWithTabs from a JSON string
aac_dashboard_with_tabs_instance = AacDashboardWithTabs.from_json(json)
# print the JSON string representation of the object
print(AacDashboardWithTabs.to_json())

# convert the object into a dict
aac_dashboard_with_tabs_dict = aac_dashboard_with_tabs_instance.to_dict()
# create an instance of AacDashboardWithTabs from a dict
aac_dashboard_with_tabs_from_dict = AacDashboardWithTabs.from_dict(aac_dashboard_with_tabs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


