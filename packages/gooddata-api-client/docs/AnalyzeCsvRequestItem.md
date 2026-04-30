# AnalyzeCsvRequestItem

CSV analysis request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**AnalyzeCsvRequestItemConfig**](AnalyzeCsvRequestItemConfig.md) |  | [optional] 
**location** | **str** | Location of the CSV file to analyze. | 

## Example

```python
from gooddata_api_client.models.analyze_csv_request_item import AnalyzeCsvRequestItem

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyzeCsvRequestItem from a JSON string
analyze_csv_request_item_instance = AnalyzeCsvRequestItem.from_json(json)
# print the JSON string representation of the object
print(AnalyzeCsvRequestItem.to_json())

# convert the object into a dict
analyze_csv_request_item_dict = analyze_csv_request_item_instance.to_dict()
# create an instance of AnalyzeCsvRequestItem from a dict
analyze_csv_request_item_from_dict = AnalyzeCsvRequestItem.from_dict(analyze_csv_request_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


