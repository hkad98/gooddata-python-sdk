# AacLabelTranslation

Localized source columns.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | Locale identifier. | 
**source_column** | **str** | Source column for translation. | 

## Example

```python
from gooddata_api_client.models.aac_label_translation import AacLabelTranslation

# TODO update the JSON string below
json = "{}"
# create an instance of AacLabelTranslation from a JSON string
aac_label_translation_instance = AacLabelTranslation.from_json(json)
# print the JSON string representation of the object
print(AacLabelTranslation.to_json())

# convert the object into a dict
aac_label_translation_dict = aac_label_translation_instance.to_dict()
# create an instance of AacLabelTranslation from a dict
aac_label_translation_from_dict = AacLabelTranslation.from_dict(aac_label_translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


