# AzureFoundryProviderConfig

Configuration for Azure Foundry provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**AzureFoundryProviderAuth**](AzureFoundryProviderAuth.md) |  | 
**endpoint** | **str** | Azure OpenAI endpoint URL. | 
**type** | **str** | Provider type. | 

## Example

```python
from gooddata_api_client.models.azure_foundry_provider_config import AzureFoundryProviderConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AzureFoundryProviderConfig from a JSON string
azure_foundry_provider_config_instance = AzureFoundryProviderConfig.from_json(json)
# print the JSON string representation of the object
print(AzureFoundryProviderConfig.to_json())

# convert the object into a dict
azure_foundry_provider_config_dict = azure_foundry_provider_config_instance.to_dict()
# create an instance of AzureFoundryProviderConfig from a dict
azure_foundry_provider_config_from_dict = AzureFoundryProviderConfig.from_dict(azure_foundry_provider_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


