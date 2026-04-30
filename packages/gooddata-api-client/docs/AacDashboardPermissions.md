# AacDashboardPermissions

Dashboard permissions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edit** | [**AacPermission**](AacPermission.md) |  | [optional] 
**share** | [**AacPermission**](AacPermission.md) |  | [optional] 
**view** | [**AacPermission**](AacPermission.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.aac_dashboard_permissions import AacDashboardPermissions

# TODO update the JSON string below
json = "{}"
# create an instance of AacDashboardPermissions from a JSON string
aac_dashboard_permissions_instance = AacDashboardPermissions.from_json(json)
# print the JSON string representation of the object
print(AacDashboardPermissions.to_json())

# convert the object into a dict
aac_dashboard_permissions_dict = aac_dashboard_permissions_instance.to_dict()
# create an instance of AacDashboardPermissions from a dict
aac_dashboard_permissions_from_dict = AacDashboardPermissions.from_dict(aac_dashboard_permissions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


