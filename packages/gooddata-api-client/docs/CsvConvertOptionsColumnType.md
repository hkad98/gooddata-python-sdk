# CsvConvertOptionsColumnType

Information about a certain column in the table.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The column name. | [optional] 
**nullable** | **bool** | Whether the data in the given column can be null. | [optional] 
**type** | **str** | The column type. | [optional] 

## Example

```python
from gooddata_api_client.models.csv_convert_options_column_type import CsvConvertOptionsColumnType

# TODO update the JSON string below
json = "{}"
# create an instance of CsvConvertOptionsColumnType from a JSON string
csv_convert_options_column_type_instance = CsvConvertOptionsColumnType.from_json(json)
# print the JSON string representation of the object
print(CsvConvertOptionsColumnType.to_json())

# convert the object into a dict
csv_convert_options_column_type_dict = csv_convert_options_column_type_instance.to_dict()
# create an instance of CsvConvertOptionsColumnType from a dict
csv_convert_options_column_type_from_dict = CsvConvertOptionsColumnType.from_dict(csv_convert_options_column_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


