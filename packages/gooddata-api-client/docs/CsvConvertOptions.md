# CsvConvertOptions

Options for converting CSV files when reading.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_dict_encode** | **bool** | Whether to try to automatically dict-encode string / binary data. | [optional] 
**auto_dict_max_cardinality** | **int** | The maximum dictionary cardinality for autoDictEncode. | [optional] 
**check_utf8** | **bool** | Whether to check UTF8 validity of string columns. | [optional] 
**column_types** | [**List[CsvConvertOptionsColumnType]**](CsvConvertOptionsColumnType.md) | Information about the column types in the table. | [optional] 
**decimal_point** | **str** | The character used as decimal point in floating-point and decimal data. | [optional] 
**false_values** | **List[str]** | Sequence of strings that denote false Booleans in the data. | [optional] 
**include_columns** | **List[str]** | The names of columns to include in the Table. If empty, the Table will include all columns from the CSV file. If not empty, only these columns will be included, in this order. | [optional] 
**include_missing_columns** | **bool** | If false, columns in includeColumns but not in the CSV file will error out. | [optional] 
**null_values** | **List[str]** | Sequence of strings that denote nulls in the data. | [optional] 
**quoted_strings_can_be_null** | **bool** | Whether quoted values can be null. | [optional] 
**strings_can_be_null** | **bool** | Whether string / binary columns can have null values. | [optional] 
**timestamp_parsers** | **List[str]** | Sequence of strptime()-compatible format strings, tried in order when attempting to infer or convert timestamp values. | [optional] 
**true_values** | **List[str]** | Sequence of strings that denote true Booleans in the data. | [optional] 

## Example

```python
from gooddata_api_client.models.csv_convert_options import CsvConvertOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CsvConvertOptions from a JSON string
csv_convert_options_instance = CsvConvertOptions.from_json(json)
# print the JSON string representation of the object
print(CsvConvertOptions.to_json())

# convert the object into a dict
csv_convert_options_dict = csv_convert_options_instance.to_dict()
# create an instance of CsvConvertOptions from a dict
csv_convert_options_from_dict = CsvConvertOptions.from_dict(csv_convert_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


