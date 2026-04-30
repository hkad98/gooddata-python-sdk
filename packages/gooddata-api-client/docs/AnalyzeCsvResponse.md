# AnalyzeCsvResponse

Describes the results of a CSV analysis of a single file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**List[AnalyzeCsvResponseColumn]**](AnalyzeCsvResponseColumn.md) | List of column metadata. | 
**config** | [**AnalyzeCsvResponseConfig**](AnalyzeCsvResponseConfig.md) |  | [optional] 
**location** | **str** | Location of the analyzed file in the source data source. | 
**preview_data** | **List[List[object]]** | Preview of the first N rows of the file. | 

## Example

```python
from gooddata_api_client.models.analyze_csv_response import AnalyzeCsvResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyzeCsvResponse from a JSON string
analyze_csv_response_instance = AnalyzeCsvResponse.from_json(json)
# print the JSON string representation of the object
print(AnalyzeCsvResponse.to_json())

# convert the object into a dict
analyze_csv_response_dict = analyze_csv_response_instance.to_dict()
# create an instance of AnalyzeCsvResponse from a dict
analyze_csv_response_from_dict = AnalyzeCsvResponse.from_dict(analyze_csv_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


