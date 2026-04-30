# DeclarativeLabelTranslation

A label translation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**locale** | **str** | Translation locale. | 
**source_column** | **str** | Translation source column. | 

## Example

```python
from gooddata_api_client.models.declarative_label_translation import DeclarativeLabelTranslation

# TODO update the JSON string below
json = "{}"
# create an instance of DeclarativeLabelTranslation from a JSON string
declarative_label_translation_instance = DeclarativeLabelTranslation.from_json(json)
# print the JSON string representation of the object
print(DeclarativeLabelTranslation.to_json())

# convert the object into a dict
declarative_label_translation_dict = declarative_label_translation_instance.to_dict()
# create an instance of DeclarativeLabelTranslation from a dict
declarative_label_translation_from_dict = DeclarativeLabelTranslation.from_dict(declarative_label_translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


