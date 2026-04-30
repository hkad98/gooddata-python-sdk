# JsonApiOrganizationInAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_origins** | **List[str]** |  | [optional] 
**early_access** | **str** | The early access feature identifier. It is used to enable experimental features. Deprecated in favor of earlyAccessValues. | [optional] 
**early_access_values** | **List[str]** | The early access feature identifiers. They are used to enable experimental features. | [optional] 
**hostname** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_organization_in_attributes import JsonApiOrganizationInAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiOrganizationInAttributes from a JSON string
json_api_organization_in_attributes_instance = JsonApiOrganizationInAttributes.from_json(json)
# print the JSON string representation of the object
print(JsonApiOrganizationInAttributes.to_json())

# convert the object into a dict
json_api_organization_in_attributes_dict = json_api_organization_in_attributes_instance.to_dict()
# create an instance of JsonApiOrganizationInAttributes from a dict
json_api_organization_in_attributes_from_dict = JsonApiOrganizationInAttributes.from_dict(json_api_organization_in_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


