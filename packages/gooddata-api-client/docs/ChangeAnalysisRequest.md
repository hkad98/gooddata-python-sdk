# ChangeAnalysisRequest

Request for change analysis computation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analyzed_period** | **str** | The analyzed time period (e.g., &#39;2025-02&#39;) | 
**attributes** | [**List[AttributeItem]**](AttributeItem.md) | Attributes to analyze for significant changes. If empty, valid attributes will be automatically discovered. | [optional] 
**aux_measures** | [**List[MeasureItem]**](MeasureItem.md) | Auxiliary measures | [optional] 
**date_attribute** | [**AttributeItem**](AttributeItem.md) |  | 
**exclude_tags** | **List[str]** | Exclude attributes with any of these tags. This filter applies to both auto-discovered and explicitly provided attributes. | [optional] 
**filters** | [**List[ChangeAnalysisParamsFiltersInner]**](ChangeAnalysisParamsFiltersInner.md) | Optional filters to apply. | [optional] 
**include_tags** | **List[str]** | Only include attributes with at least one of these tags. If empty, no inclusion filter is applied. This filter applies to both auto-discovered and explicitly provided attributes. | [optional] 
**measure** | [**MeasureItem**](MeasureItem.md) |  | 
**reference_period** | **str** | The reference time period (e.g., &#39;2025-01&#39;) | 
**use_smart_attribute_selection** | **bool** | Whether to use smart attribute selection (LLM-based) instead of discovering all valid attributes. If true, GenAI will intelligently select the most relevant attributes for change analysis. If false or not set, all valid attributes will be discovered using Calcique. Smart attribute selection applies only when no attributes are provided. | [optional] [default to False]

## Example

```python
from gooddata_api_client.models.change_analysis_request import ChangeAnalysisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeAnalysisRequest from a JSON string
change_analysis_request_instance = ChangeAnalysisRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeAnalysisRequest.to_json())

# convert the object into a dict
change_analysis_request_dict = change_analysis_request_instance.to_dict()
# create an instance of ChangeAnalysisRequest from a dict
change_analysis_request_from_dict = ChangeAnalysisRequest.from_dict(change_analysis_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


