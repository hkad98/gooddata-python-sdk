# AacVisualizationTrendBuckets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **Dict[str, object]** |  | [optional] 
**attributes** | [**List[AacVisualizationTrendBucketsAllOfAttributes]**](AacVisualizationTrendBucketsAllOfAttributes.md) | Attributes bucket (for scatter). | [optional] 
**columns** | [**List[AacVisualizationTrendBucketsAllOfColumns]**](AacVisualizationTrendBucketsAllOfColumns.md) | Columns bucket (for tables). | [optional] 
**config** | **object** | Free-form JSON object | [optional] 
**description** | **str** | Visualization description. | [optional] 
**var_from** | **object** | Free-form JSON object | [optional] 
**id** | **str** | Unique identifier of the visualization. | 
**is_hidden** | **bool** | Deprecated. Use showInAiResults instead. | [optional] 
**layers** | [**List[AacVisualizationLayer]**](AacVisualizationLayer.md) | Visualization data layers (for geo charts). | [optional] 
**metrics** | [**List[AacVisualizationTrendBucketsAllOfMetrics]**](AacVisualizationTrendBucketsAllOfMetrics.md) | Metrics bucket. | [optional] 
**query** | [**AacQuery**](AacQuery.md) |  | 
**rows** | [**List[AacVisualizationTrendBucketsAllOfRows]**](AacVisualizationTrendBucketsAllOfRows.md) | Rows bucket (for tables). | [optional] 
**segment_by** | [**List[AacVisualizationTrendBucketsAllOfSegmentBy]**](AacVisualizationTrendBucketsAllOfSegmentBy.md) | Segment by attributes bucket. | [optional] 
**show_in_ai_results** | **bool** | Whether to show in AI results. | [optional] 
**size_by** | [**List[AacVisualizationTrendBucketsAllOfSizeBy]**](AacVisualizationTrendBucketsAllOfSizeBy.md) | Size by metrics bucket. | [optional] 
**stack_by** | [**List[AacVisualizationTrendBucketsAllOfStackBy]**](AacVisualizationTrendBucketsAllOfStackBy.md) | Stack by attributes bucket. | [optional] 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**to** | **object** | Free-form JSON object | [optional] 
**trend_by** | [**List[AacVisualizationTrendBucketsAllOfTrendBy]**](AacVisualizationTrendBucketsAllOfTrendBy.md) | Trend by attributes bucket. | [optional] 
**type** | **str** |  | 
**view_by** | [**List[AacVisualizationTrendBucketsAllOfViewBy]**](AacVisualizationTrendBucketsAllOfViewBy.md) | View by attributes bucket. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_visualization_trend_buckets import AacVisualizationTrendBuckets

# TODO update the JSON string below
json = "{}"
# create an instance of AacVisualizationTrendBuckets from a JSON string
aac_visualization_trend_buckets_instance = AacVisualizationTrendBuckets.from_json(json)
# print the JSON string representation of the object
print(AacVisualizationTrendBuckets.to_json())

# convert the object into a dict
aac_visualization_trend_buckets_dict = aac_visualization_trend_buckets_instance.to_dict()
# create an instance of AacVisualizationTrendBuckets from a dict
aac_visualization_trend_buckets_from_dict = AacVisualizationTrendBuckets.from_dict(aac_visualization_trend_buckets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


