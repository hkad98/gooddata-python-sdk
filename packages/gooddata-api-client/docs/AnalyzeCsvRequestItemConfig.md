# AnalyzeCsvRequestItemConfig

CSV analysis request config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delimiters** | **List[str]** | Possible column delimiters. | [optional] 
**header_detect_max_rows** | **int** | Maximum number of rows to work with during header detection. | [optional] 
**header_row_count** | **int** | Number of rows to consider as header, if null, header will be detected. | [optional] 
**result_rows** | **int** | Number of rows to return in the flight that represents analysis result. If 0, no rows are returned, if less than 0, all rows that were in the sample are returned. | [optional] 

## Example

```python
from gooddata_api_client.models.analyze_csv_request_item_config import AnalyzeCsvRequestItemConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyzeCsvRequestItemConfig from a JSON string
analyze_csv_request_item_config_instance = AnalyzeCsvRequestItemConfig.from_json(json)
# print the JSON string representation of the object
print(AnalyzeCsvRequestItemConfig.to_json())

# convert the object into a dict
analyze_csv_request_item_config_dict = analyze_csv_request_item_config_instance.to_dict()
# create an instance of AnalyzeCsvRequestItemConfig from a dict
analyze_csv_request_item_config_from_dict = AnalyzeCsvRequestItemConfig.from_dict(analyze_csv_request_item_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


