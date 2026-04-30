# ImportCsvRequestTable

Information about a particular table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the table. | 
**source** | [**ImportCsvRequestTableSource**](ImportCsvRequestTableSource.md) |  | 

## Example

```python
from gooddata_api_client.models.import_csv_request_table import ImportCsvRequestTable

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCsvRequestTable from a JSON string
import_csv_request_table_instance = ImportCsvRequestTable.from_json(json)
# print the JSON string representation of the object
print(ImportCsvRequestTable.to_json())

# convert the object into a dict
import_csv_request_table_dict = import_csv_request_table_instance.to_dict()
# create an instance of ImportCsvRequestTable from a dict
import_csv_request_table_from_dict = ImportCsvRequestTable.from_dict(import_csv_request_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


