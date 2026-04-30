# MatchAttributeFilter

Filter via label with given match type and literal value.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_attribute_filter** | [**MatchAttributeFilterMatchAttributeFilter**](MatchAttributeFilterMatchAttributeFilter.md) |  | 

## Example

```python
from gooddata_api_client.models.match_attribute_filter import MatchAttributeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of MatchAttributeFilter from a JSON string
match_attribute_filter_instance = MatchAttributeFilter.from_json(json)
# print the JSON string representation of the object
print(MatchAttributeFilter.to_json())

# convert the object into a dict
match_attribute_filter_dict = match_attribute_filter_instance.to_dict()
# create an instance of MatchAttributeFilter from a dict
match_attribute_filter_from_dict = MatchAttributeFilter.from_dict(match_attribute_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


