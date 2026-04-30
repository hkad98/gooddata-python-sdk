# ImportCsvRequestTableSourceConfig

Config to use when accessing the data for executions, etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_date_formats** | **Dict[str, str]** | Date formats to use to use to read the given columns. | [optional] 
**convert_options** | [**CsvConvertOptions**](CsvConvertOptions.md) |  | [optional] 
**parse_options** | [**CsvParseOptions**](CsvParseOptions.md) |  | [optional] 
**read_options** | [**CsvReadOptions**](CsvReadOptions.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.import_csv_request_table_source_config import ImportCsvRequestTableSourceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCsvRequestTableSourceConfig from a JSON string
import_csv_request_table_source_config_instance = ImportCsvRequestTableSourceConfig.from_json(json)
# print the JSON string representation of the object
print(ImportCsvRequestTableSourceConfig.to_json())

# convert the object into a dict
import_csv_request_table_source_config_dict = import_csv_request_table_source_config_instance.to_dict()
# create an instance of ImportCsvRequestTableSourceConfig from a dict
import_csv_request_table_source_config_from_dict = ImportCsvRequestTableSourceConfig.from_dict(import_csv_request_table_source_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


