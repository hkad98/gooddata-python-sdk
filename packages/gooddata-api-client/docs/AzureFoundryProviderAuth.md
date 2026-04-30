# AzureFoundryProviderAuth

Authentication configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | Azure API key. | [optional] 
**type** | **str** | Authentication type. | 

## Example

```python
from gooddata_api_client.models.azure_foundry_provider_auth import AzureFoundryProviderAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AzureFoundryProviderAuth from a JSON string
azure_foundry_provider_auth_instance = AzureFoundryProviderAuth.from_json(json)
# print the JSON string representation of the object
print(AzureFoundryProviderAuth.to_json())

# convert the object into a dict
azure_foundry_provider_auth_dict = azure_foundry_provider_auth_instance.to_dict()
# create an instance of AzureFoundryProviderAuth from a dict
azure_foundry_provider_auth_from_dict = AzureFoundryProviderAuth.from_dict(azure_foundry_provider_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


