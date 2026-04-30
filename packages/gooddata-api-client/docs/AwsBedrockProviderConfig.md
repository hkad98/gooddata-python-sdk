# AwsBedrockProviderConfig

Configuration for AWS Bedrock provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**BedrockProviderAuth**](BedrockProviderAuth.md) |  | 
**region** | **str** | AWS region for Bedrock. | 
**type** | **str** | Provider type. | 

## Example

```python
from gooddata_api_client.models.aws_bedrock_provider_config import AwsBedrockProviderConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AwsBedrockProviderConfig from a JSON string
aws_bedrock_provider_config_instance = AwsBedrockProviderConfig.from_json(json)
# print the JSON string representation of the object
print(AwsBedrockProviderConfig.to_json())

# convert the object into a dict
aws_bedrock_provider_config_dict = aws_bedrock_provider_config_instance.to_dict()
# create an instance of AwsBedrockProviderConfig from a dict
aws_bedrock_provider_config_from_dict = AwsBedrockProviderConfig.from_dict(aws_bedrock_provider_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


