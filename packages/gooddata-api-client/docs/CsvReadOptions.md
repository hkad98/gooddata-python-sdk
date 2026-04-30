# CsvReadOptions

Options for reading CSV files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_generate_column_names** | **bool** | Whether to autogenerate column names if columnNames is empty. | [optional] 
**block_size** | **int** | How many bytes to process at a time from the input stream. | [optional] 
**column_names** | **List[str]** | The column names of the target table. | [optional] 
**encoding** | **str** | The character encoding of the CSV data. | [optional] 
**skip_rows** | **int** | The number of rows to skip before the column names (if any) and the CSV data. | [optional] 
**skip_rows_after_names** | **int** | The number of rows to skip after the column names. | [optional] 
**use_threads** | **bool** | Whether to use multiple threads to accelerate reading. | [optional] 

## Example

```python
from gooddata_api_client.models.csv_read_options import CsvReadOptions

# TODO update the JSON string below
json = "{}"
# create an instance of CsvReadOptions from a JSON string
csv_read_options_instance = CsvReadOptions.from_json(json)
# print the JSON string representation of the object
print(CsvReadOptions.to_json())

# convert the object into a dict
csv_read_options_dict = csv_read_options_instance.to_dict()
# create an instance of CsvReadOptions from a dict
csv_read_options_from_dict = CsvReadOptions.from_dict(csv_read_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


