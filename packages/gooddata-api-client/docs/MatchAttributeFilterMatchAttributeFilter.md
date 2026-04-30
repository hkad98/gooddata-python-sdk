# MatchAttributeFilterMatchAttributeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apply_on_result** | **bool** |  | [optional] 
**case_sensitive** | **bool** | Indicates whether the filter match is evaluated in case-sensitive mode or not. | [optional] [default to False]
**label** | [**AfmIdentifier**](AfmIdentifier.md) |  | 
**literal** | **str** | Literal used to limit label values. | 
**local_identifier** | **str** |  | [optional] 
**match_type** | **str** | Requested match type. | 
**negate** | **bool** | Indicates whether the filter should negate the match. | [optional] [default to False]

## Example

```python
from gooddata_api_client.models.match_attribute_filter_match_attribute_filter import MatchAttributeFilterMatchAttributeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAttributeFilterMatchAttributeFilter from a JSON string
match_attribute_filter_match_attribute_filter_instance = MatchAttributeFilterMatchAttributeFilter.from_json(json)
# print the JSON string representation of the object
print(MatchAttributeFilterMatchAttributeFilter.to_json())

# convert the object into a dict
match_attribute_filter_match_attribute_filter_dict = match_attribute_filter_match_attribute_filter_instance.to_dict()
# create an instance of MatchAttributeFilterMatchAttributeFilter from a dict
match_attribute_filter_match_attribute_filter_from_dict = MatchAttributeFilterMatchAttributeFilter.from_dict(match_attribute_filter_match_attribute_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


