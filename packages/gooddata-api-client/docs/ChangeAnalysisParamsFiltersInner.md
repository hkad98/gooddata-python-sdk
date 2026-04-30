# ChangeAnalysisParamsFiltersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comparison_measure_value_filter** | [**ComparisonMeasureValueFilterComparisonMeasureValueFilter**](ComparisonMeasureValueFilterComparisonMeasureValueFilter.md) |  | 
**range_measure_value_filter** | [**RangeMeasureValueFilterRangeMeasureValueFilter**](RangeMeasureValueFilterRangeMeasureValueFilter.md) |  | 
**compound_measure_value_filter** | [**CompoundMeasureValueFilterCompoundMeasureValueFilter**](CompoundMeasureValueFilterCompoundMeasureValueFilter.md) |  | 
**ranking_filter** | [**RankingFilterRankingFilter**](RankingFilterRankingFilter.md) |  | 
**absolute_date_filter** | [**AbsoluteDateFilterAbsoluteDateFilter**](AbsoluteDateFilterAbsoluteDateFilter.md) |  | 
**relative_date_filter** | [**RelativeDateFilterRelativeDateFilter**](RelativeDateFilterRelativeDateFilter.md) |  | 
**all_time_date_filter** | [**AllTimeDateFilterAllTimeDateFilter**](AllTimeDateFilterAllTimeDateFilter.md) |  | 
**negative_attribute_filter** | [**NegativeAttributeFilterNegativeAttributeFilter**](NegativeAttributeFilterNegativeAttributeFilter.md) |  | 
**positive_attribute_filter** | [**PositiveAttributeFilterPositiveAttributeFilter**](PositiveAttributeFilterPositiveAttributeFilter.md) |  | 
**match_attribute_filter** | [**MatchAttributeFilterMatchAttributeFilter**](MatchAttributeFilterMatchAttributeFilter.md) |  | 
**inline** | [**InlineFilterDefinitionInline**](InlineFilterDefinitionInline.md) |  | 

## Example

```python
from gooddata_api_client.models.change_analysis_params_filters_inner import ChangeAnalysisParamsFiltersInner

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeAnalysisParamsFiltersInner from a JSON string
change_analysis_params_filters_inner_instance = ChangeAnalysisParamsFiltersInner.from_json(json)
# print the JSON string representation of the object
print(ChangeAnalysisParamsFiltersInner.to_json())

# convert the object into a dict
change_analysis_params_filters_inner_dict = change_analysis_params_filters_inner_instance.to_dict()
# create an instance of ChangeAnalysisParamsFiltersInner from a dict
change_analysis_params_filters_inner_from_dict = ChangeAnalysisParamsFiltersInner.from_dict(change_analysis_params_filters_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


