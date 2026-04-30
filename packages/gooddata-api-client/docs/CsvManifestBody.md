# CsvManifestBody

Body of the CSV manifest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_date_formats** | **Dict[str, str]** | Map of column names to date formats to use when parsing them as dates. | [optional] 
**convert** | [**CsvConvertOptions**](CsvConvertOptions.md) |  | [optional] 
**parse** | [**CsvParseOptions**](CsvParseOptions.md) |  | [optional] 
**read** | [**CsvReadOptions**](CsvReadOptions.md) |  | [optional] 
**read_method** | **str** | Method used to read the CSV file. | [optional] 

## Example

```python
from gooddata_api_client.models.csv_manifest_body import CsvManifestBody

# TODO update the JSON string below
json = "{}"
# create an instance of CsvManifestBody from a JSON string
csv_manifest_body_instance = CsvManifestBody.from_json(json)
# print the JSON string representation of the object
print(CsvManifestBody.to_json())

# convert the object into a dict
csv_manifest_body_dict = csv_manifest_body_instance.to_dict()
# create an instance of CsvManifestBody from a dict
csv_manifest_body_from_dict = CsvManifestBody.from_dict(csv_manifest_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


