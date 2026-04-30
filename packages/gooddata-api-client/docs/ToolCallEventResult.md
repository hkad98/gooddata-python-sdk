# ToolCallEventResult

Tool call events emitted during the agentic loop (only present when GEN_AI_YIELD_TOOL_CALL_EVENTS is enabled).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_arguments** | **str** | JSON-encoded arguments passed to the tool function. | 
**function_name** | **str** | Name of the tool function that was called. | 
**result** | **str** | Result returned by the tool function. | 

## Example

```python
from gooddata_api_client.models.tool_call_event_result import ToolCallEventResult

# TODO update the JSON string below
json = "{}"
# create an instance of ToolCallEventResult from a JSON string
tool_call_event_result_instance = ToolCallEventResult.from_json(json)
# print the JSON string representation of the object
print(ToolCallEventResult.to_json())

# convert the object into a dict
tool_call_event_result_dict = tool_call_event_result_instance.to_dict()
# create an instance of ToolCallEventResult from a dict
tool_call_event_result_from_dict = ToolCallEventResult.from_dict(tool_call_event_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


