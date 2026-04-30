# AnalyzeCsvResponseConfig

Config used to process the CSV file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**convert_options** | [**CsvConvertOptions**](CsvConvertOptions.md) |  | [optional] 
**parse_options** | [**CsvParseOptions**](CsvParseOptions.md) |  | [optional] 
**read_options** | [**CsvReadOptions**](CsvReadOptions.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.analyze_csv_response_config import AnalyzeCsvResponseConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyzeCsvResponseConfig from a JSON string
analyze_csv_response_config_instance = AnalyzeCsvResponseConfig.from_json(json)
# print the JSON string representation of the object
print(AnalyzeCsvResponseConfig.to_json())

# convert the object into a dict
analyze_csv_response_config_dict = analyze_csv_response_config_instance.to_dict()
# create an instance of AnalyzeCsvResponseConfig from a dict
analyze_csv_response_config_from_dict = AnalyzeCsvResponseConfig.from_dict(analyze_csv_response_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


