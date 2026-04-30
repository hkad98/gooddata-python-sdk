# ImportCsvRequestTableSource

Information about source data for a particular table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | [**ImportCsvRequestTableSourceConfig**](ImportCsvRequestTableSourceConfig.md) |  | 
**location** | **str** | Location of the data in the staging area. | 

## Example

```python
from gooddata_api_client.models.import_csv_request_table_source import ImportCsvRequestTableSource

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCsvRequestTableSource from a JSON string
import_csv_request_table_source_instance = ImportCsvRequestTableSource.from_json(json)
# print the JSON string representation of the object
print(ImportCsvRequestTableSource.to_json())

# convert the object into a dict
import_csv_request_table_source_dict = import_csv_request_table_source_instance.to_dict()
# create an instance of ImportCsvRequestTableSource from a dict
import_csv_request_table_source_from_dict = ImportCsvRequestTableSource.from_dict(import_csv_request_table_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


