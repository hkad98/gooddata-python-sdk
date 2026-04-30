# UIContext

Ambient UI state: what the user is currently looking at (dashboard, visible widgets).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dashboard** | [**DashboardContext**](DashboardContext.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.ui_context import UIContext

# TODO update the JSON string below
json = "{}"
# create an instance of UIContext from a JSON string
ui_context_instance = UIContext.from_json(json)
# print the JSON string representation of the object
print(UIContext.to_json())

# convert the object into a dict
ui_context_dict = ui_context_instance.to_dict()
# create an instance of UIContext from a dict
ui_context_from_dict = UIContext.from_dict(ui_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


