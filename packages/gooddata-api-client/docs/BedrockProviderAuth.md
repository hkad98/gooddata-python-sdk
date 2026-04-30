# BedrockProviderAuth

Authentication configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | AWS Access Key ID. | [optional] 
**secret_access_key** | **str** | AWS Secret Access Key. | [optional] 
**session_token** | **str** | AWS Session Token (for temporary credentials). | [optional] 
**type** | **str** | Authentication type. | 

## Example

```python
from gooddata_api_client.models.bedrock_provider_auth import BedrockProviderAuth

# TODO update the JSON string below
json = "{}"
# create an instance of BedrockProviderAuth from a JSON string
bedrock_provider_auth_instance = BedrockProviderAuth.from_json(json)
# print the JSON string representation of the object
print(BedrockProviderAuth.to_json())

# convert the object into a dict
bedrock_provider_auth_dict = bedrock_provider_auth_instance.to_dict()
# create an instance of BedrockProviderAuth from a dict
bedrock_provider_auth_from_dict = BedrockProviderAuth.from_dict(bedrock_provider_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


