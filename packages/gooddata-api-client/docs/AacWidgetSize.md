# AacWidgetSize

Deprecated widget size (legacy AAC).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** | Height in grid rows. | [optional] 
**height_as_ratio** | **bool** | Height definition mode. | [optional] 
**width** | **int** | Width in grid columns. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_widget_size import AacWidgetSize

# TODO update the JSON string below
json = "{}"
# create an instance of AacWidgetSize from a JSON string
aac_widget_size_instance = AacWidgetSize.from_json(json)
# print the JSON string representation of the object
print(AacWidgetSize.to_json())

# convert the object into a dict
aac_widget_size_dict = aac_widget_size_instance.to_dict()
# create an instance of AacWidgetSize from a dict
aac_widget_size_from_dict = AacWidgetSize.from_dict(aac_widget_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


