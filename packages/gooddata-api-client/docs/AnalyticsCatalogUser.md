# AnalyticsCatalogUser

Users who created any object in the catalog

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firstname** | **str** | First name of the user who created any objects | 
**lastname** | **str** | Last name of the user who created any objects | 
**user_id** | **str** | User ID of the user who created any objects | 

## Example

```python
from gooddata_api_client.models.analytics_catalog_user import AnalyticsCatalogUser

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsCatalogUser from a JSON string
analytics_catalog_user_instance = AnalyticsCatalogUser.from_json(json)
# print the JSON string representation of the object
print(AnalyticsCatalogUser.to_json())

# convert the object into a dict
analytics_catalog_user_dict = analytics_catalog_user_instance.to_dict()
# create an instance of AnalyticsCatalogUser from a dict
analytics_catalog_user_from_dict = AnalyticsCatalogUser.from_dict(analytics_catalog_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


