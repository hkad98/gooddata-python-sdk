# AiUsageMetadataItem

AI usage metadata returned after the interaction (e.g. current query count vs. entitlement limit).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**counter_type** | **str** | Type of usage counter, e.g. AI_QUERIES. | 
**current_value** | **int** | Current usage value after this request. | 
**limit** | **int** | Entitlement limit. 0 means unlimited. | 

## Example

```python
from gooddata_api_client.models.ai_usage_metadata_item import AiUsageMetadataItem

# TODO update the JSON string below
json = "{}"
# create an instance of AiUsageMetadataItem from a JSON string
ai_usage_metadata_item_instance = AiUsageMetadataItem.from_json(json)
# print the JSON string representation of the object
print(AiUsageMetadataItem.to_json())

# convert the object into a dict
ai_usage_metadata_item_dict = ai_usage_metadata_item_instance.to_dict()
# create an instance of AiUsageMetadataItem from a dict
ai_usage_metadata_item_from_dict = AiUsageMetadataItem.from_dict(ai_usage_metadata_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


