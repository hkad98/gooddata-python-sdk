# AacDashboardPluginLink

Dashboard plugins.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Plugin ID. | 
**parameters** | **object** | Free-form JSON object | [optional] 

## Example

```python
from gooddata_api_client.models.aac_dashboard_plugin_link import AacDashboardPluginLink

# TODO update the JSON string below
json = "{}"
# create an instance of AacDashboardPluginLink from a JSON string
aac_dashboard_plugin_link_instance = AacDashboardPluginLink.from_json(json)
# print the JSON string representation of the object
print(AacDashboardPluginLink.to_json())

# convert the object into a dict
aac_dashboard_plugin_link_dict = aac_dashboard_plugin_link_instance.to_dict()
# create an instance of AacDashboardPluginLink from a dict
aac_dashboard_plugin_link_from_dict = AacDashboardPluginLink.from_dict(aac_dashboard_plugin_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


