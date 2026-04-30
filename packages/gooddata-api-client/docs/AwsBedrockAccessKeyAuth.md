# AwsBedrockAccessKeyAuth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_key_id** | **str** | AWS Access Key ID. | [optional] 
**secret_access_key** | **str** | AWS Secret Access Key. | [optional] 
**session_token** | **str** | AWS Session Token (for temporary credentials). | [optional] 
**type** | **str** | Authentication type. | 

## Example

```python
from gooddata_api_client.models.aws_bedrock_access_key_auth import AwsBedrockAccessKeyAuth

# TODO update the JSON string below
json = "{}"
# create an instance of AwsBedrockAccessKeyAuth from a JSON string
aws_bedrock_access_key_auth_instance = AwsBedrockAccessKeyAuth.from_json(json)
# print the JSON string representation of the object
print(AwsBedrockAccessKeyAuth.to_json())

# convert the object into a dict
aws_bedrock_access_key_auth_dict = aws_bedrock_access_key_auth_instance.to_dict()
# create an instance of AwsBedrockAccessKeyAuth from a dict
aws_bedrock_access_key_auth_from_dict = AwsBedrockAccessKeyAuth.from_dict(aws_bedrock_access_key_auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


