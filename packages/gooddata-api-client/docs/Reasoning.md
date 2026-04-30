# Reasoning

Reasoning wrapper containing steps taken during request handling.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answer** | **str** | Final answer/reasoning from the use case result. | [optional] 
**steps** | [**List[ReasoningStep]**](ReasoningStep.md) | Steps taken during processing, showing the AI&#39;s reasoning process. | 

## Example

```python
from gooddata_api_client.models.reasoning import Reasoning

# TODO update the JSON string below
json = "{}"
# create an instance of Reasoning from a JSON string
reasoning_instance = Reasoning.from_json(json)
# print the JSON string representation of the object
print(Reasoning.to_json())

# convert the object into a dict
reasoning_dict = reasoning_instance.to_dict()
# create an instance of Reasoning from a dict
reasoning_from_dict = Reasoning.from_dict(reasoning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


