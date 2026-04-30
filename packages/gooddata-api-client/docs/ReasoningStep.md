# ReasoningStep

Steps taken during processing, showing the AI's reasoning process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thoughts** | [**List[Thought]**](Thought.md) | Detailed thoughts/messages within this step. | 
**title** | **str** | Title describing this reasoning step. | 

## Example

```python
from gooddata_api_client.models.reasoning_step import ReasoningStep

# TODO update the JSON string below
json = "{}"
# create an instance of ReasoningStep from a JSON string
reasoning_step_instance = ReasoningStep.from_json(json)
# print the JSON string representation of the object
print(ReasoningStep.to_json())

# convert the object into a dict
reasoning_step_dict = reasoning_step_instance.to_dict()
# create an instance of ReasoningStep from a dict
reasoning_step_from_dict = ReasoningStep.from_dict(reasoning_step_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


