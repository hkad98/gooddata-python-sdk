# Thought

Detailed thoughts/messages within this step.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | The text content of this thought. | 

## Example

```python
from gooddata_api_client.models.thought import Thought

# TODO update the JSON string below
json = "{}"
# create an instance of Thought from a JSON string
thought_instance = Thought.from_json(json)
# print the JSON string representation of the object
print(Thought.to_json())

# convert the object into a dict
thought_dict = thought_instance.to_dict()
# create an instance of Thought from a dict
thought_from_dict = Thought.from_dict(thought_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


