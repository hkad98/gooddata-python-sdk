# ImportCsvResponse

Response containing the information about the imported CSV file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the table the file was imported to. | 
**version** | **int** | Version the file was imported as. | 

## Example

```python
from gooddata_api_client.models.import_csv_response import ImportCsvResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportCsvResponse from a JSON string
import_csv_response_instance = ImportCsvResponse.from_json(json)
# print the JSON string representation of the object
print(ImportCsvResponse.to_json())

# convert the object into a dict
import_csv_response_dict = import_csv_response_instance.to_dict()
# create an instance of ImportCsvResponse from a dict
import_csv_response_from_dict = ImportCsvResponse.from_dict(import_csv_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


