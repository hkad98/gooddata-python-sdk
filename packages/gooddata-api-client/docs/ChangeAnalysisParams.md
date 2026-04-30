# ChangeAnalysisParams

Change analysis specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyzed_period** | **str** | The analyzed time period | 
**attributes** | [**List[AttributeItem]**](AttributeItem.md) | Attributes to analyze for significant changes | 
**date_attribute** | [**AttributeItem**](AttributeItem.md) |  | 
**filters** | [**List[ChangeAnalysisParamsFiltersInner]**](ChangeAnalysisParamsFiltersInner.md) | Optional filters to apply | 
**measure** | [**MeasureItem**](MeasureItem.md) |  | 
**measure_title** | **str** | The title of the measure being analyzed | 
**reference_period** | **str** | The reference time period | 
**use_smart_attribute_selection** | **bool** | Whether to use smart attribute selection | 

## Example

```python
from gooddata_api_client.models.change_analysis_params import ChangeAnalysisParams

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeAnalysisParams from a JSON string
change_analysis_params_instance = ChangeAnalysisParams.from_json(json)
# print the JSON string representation of the object
print(ChangeAnalysisParams.to_json())

# convert the object into a dict
change_analysis_params_dict = change_analysis_params_instance.to_dict()
# create an instance of ChangeAnalysisParams from a dict
change_analysis_params_from_dict = ChangeAnalysisParams.from_dict(change_analysis_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


