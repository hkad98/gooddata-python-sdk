# AacPermission

SHARE permission.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **bool** | Grant to all users. | [optional] 
**user_groups** | **List[str]** | List of user group IDs. | [optional] 
**users** | **List[str]** | List of user IDs. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_permission import AacPermission

# TODO update the JSON string below
json = "{}"
# create an instance of AacPermission from a JSON string
aac_permission_instance = AacPermission.from_json(json)
# print the JSON string representation of the object
print(AacPermission.to_json())

# convert the object into a dict
aac_permission_dict = aac_permission_instance.to_dict()
# create an instance of AacPermission from a dict
aac_permission_from_dict = AacPermission.from_dict(aac_permission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


