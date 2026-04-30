# AzureFoundryApiKeyAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Azure API key. | [optional] 
**type** | **str** | Authentication type. | 

## Example

```python
from gooddata_api_client.models.azure_foundry_api_key_auth import AzureFoundryApiKeyAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AzureFoundryApiKeyAuth from a JSON string
azure_foundry_api_key_auth_instance = AzureFoundryApiKeyAuth.from_json(json)
# print the JSON string representation of the object
print(AzureFoundryApiKeyAuth.to_json())

# convert the object into a dict
azure_foundry_api_key_auth_dict = azure_foundry_api_key_auth_instance.to_dict()
# create an instance of AzureFoundryApiKeyAuth from a dict
azure_foundry_api_key_auth_from_dict = AzureFoundryApiKeyAuth.from_dict(azure_foundry_api_key_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


