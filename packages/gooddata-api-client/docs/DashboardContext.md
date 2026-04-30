# DashboardContext

Dashboard the user is currently viewing.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Dashboard object ID. | 
**widgets** | [**List[WidgetDescriptor]**](WidgetDescriptor.md) | Widgets currently visible on the dashboard. | 

## Example

```python
from gooddata_api_client.models.dashboard_context import DashboardContext

# TODO update the JSON string below
json = "{}"
# create an instance of DashboardContext from a JSON string
dashboard_context_instance = DashboardContext.from_json(json)
# print the JSON string representation of the object
print(DashboardContext.to_json())

# convert the object into a dict
dashboard_context_dict = dashboard_context_instance.to_dict()
# create an instance of DashboardContext from a dict
dashboard_context_from_dict = DashboardContext.from_dict(dashboard_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


