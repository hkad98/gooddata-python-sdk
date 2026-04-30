# JsonApiAutomationResultOutList

A JSON:API document with a list of resources

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[JsonApiAutomationResultOutWithLinks]**](JsonApiAutomationResultOutWithLinks.md) |  | 
**included** | [**List[JsonApiAutomationOutWithLinks]**](JsonApiAutomationOutWithLinks.md) | Included resources | [optional] 
**links** | [**ListLinks**](ListLinks.md) |  | [optional] 
**meta** | [**JsonApiAggregatedFactOutListMeta**](JsonApiAggregatedFactOutListMeta.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_automation_result_out_list import JsonApiAutomationResultOutList

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiAutomationResultOutList from a JSON string
json_api_automation_result_out_list_instance = JsonApiAutomationResultOutList.from_json(json)
# print the JSON string representation of the object
print(JsonApiAutomationResultOutList.to_json())

# convert the object into a dict
json_api_automation_result_out_list_dict = json_api_automation_result_out_list_instance.to_dict()
# create an instance of JsonApiAutomationResultOutList from a dict
json_api_automation_result_out_list_from_dict = JsonApiAutomationResultOutList.from_dict(json_api_automation_result_out_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


