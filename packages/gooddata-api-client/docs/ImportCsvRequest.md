# ImportCsvRequest

Request containing the information necessary to import one or more CSV files from the staging area.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tables** | [**List[ImportCsvRequestTable]**](ImportCsvRequestTable.md) | Information about the individual tables. | 

## Example

```python
from gooddata_api_client.models.import_csv_request import ImportCsvRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCsvRequest from a JSON string
import_csv_request_instance = ImportCsvRequest.from_json(json)
# print the JSON string representation of the object
print(ImportCsvRequest.to_json())

# convert the object into a dict
import_csv_request_dict = import_csv_request_instance.to_dict()
# create an instance of ImportCsvRequest from a dict
import_csv_request_from_dict = ImportCsvRequest.from_dict(import_csv_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


