# AacPlugin

AAC dashboard plugin definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Plugin description. | [optional] 
**id** | **str** | Unique identifier of the plugin. | 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**type** | **str** | Plugin type discriminator. | 
**url** | **str** | URL of the plugin. | 

## Example

```python
from gooddata_api_client.models.aac_plugin import AacPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of AacPlugin from a JSON string
aac_plugin_instance = AacPlugin.from_json(json)
# print the JSON string representation of the object
print(AacPlugin.to_json())

# convert the object into a dict
aac_plugin_dict = aac_plugin_instance.to_dict()
# create an instance of AacPlugin from a dict
aac_plugin_from_dict = AacPlugin.from_dict(aac_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


