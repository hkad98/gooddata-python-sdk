# CsvParseOptions

Options for parsing CSV files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delimiter** | **str** | The character delimiting individual cells in the CSV data. | [optional] 
**double_quote** | **bool** | Whether two quotes in a quoted CSV value denote a single quote in the data. | [optional] 
**escape_char** | **object** | The character used optionally for escaping special characters or false to disable escaping. | [optional] 
**ignore_empty_lines** | **bool** | Whether empty lines are ignored in CSV input. | [optional] 
**newlines_in_values** | **bool** | Whether newline characters are allowed in CSV values. | [optional] 
**quote_char** | **object** | The character used optionally for quoting CSV values or false to disable quoting. | [optional] 

## Example

```python
from gooddata_api_client.models.csv_parse_options import CsvParseOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CsvParseOptions from a JSON string
csv_parse_options_instance = CsvParseOptions.from_json(json)
# print the JSON string representation of the object
print(CsvParseOptions.to_json())

# convert the object into a dict
csv_parse_options_dict = csv_parse_options_instance.to_dict()
# create an instance of CsvParseOptions from a dict
csv_parse_options_from_dict = CsvParseOptions.from_dict(csv_parse_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


