# AacFilterState

Filter state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude** | **List[str]** | Excluded values. | [optional] 
**include** | **List[str]** | Included values. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_filter_state import AacFilterState

# TODO update the JSON string below
json = "{}"
# create an instance of AacFilterState from a JSON string
aac_filter_state_instance = AacFilterState.from_json(json)
# print the JSON string representation of the object
print(AacFilterState.to_json())

# convert the object into a dict
aac_filter_state_dict = aac_filter_state_instance.to_dict()
# create an instance of AacFilterState from a dict
aac_filter_state_from_dict = AacFilterState.from_dict(aac_filter_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


