# AacVisualizationStackedBuckets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **Dict[str, object]** |  | [optional] 
**attributes** | [**List[AacVisualizationStackedBucketsAllOfAttributes]**](AacVisualizationStackedBucketsAllOfAttributes.md) | Attributes bucket (for scatter). | [optional] 
**columns** | [**List[AacVisualizationStackedBucketsAllOfColumns]**](AacVisualizationStackedBucketsAllOfColumns.md) | Columns bucket (for tables). | [optional] 
**config** | **object** | Free-form JSON object | [optional] 
**description** | **str** | Visualization description. | [optional] 
**var_from** | **object** | Free-form JSON object | [optional] 
**id** | **str** | Unique identifier of the visualization. | 
**is_hidden** | **bool** | Deprecated. Use showInAiResults instead. | [optional] 
**layers** | [**List[AacVisualizationLayer]**](AacVisualizationLayer.md) | Visualization data layers (for geo charts). | [optional] 
**metrics** | [**List[AacVisualizationStackedBucketsAllOfMetrics]**](AacVisualizationStackedBucketsAllOfMetrics.md) | Metrics bucket. | [optional] 
**query** | [**AacQuery**](AacQuery.md) |  | 
**rows** | [**List[AacVisualizationStackedBucketsAllOfRows]**](AacVisualizationStackedBucketsAllOfRows.md) | Rows bucket (for tables). | [optional] 
**segment_by** | [**List[AacVisualizationStackedBucketsAllOfSegmentBy]**](AacVisualizationStackedBucketsAllOfSegmentBy.md) | Segment by attributes bucket. | [optional] 
**show_in_ai_results** | **bool** | Whether to show in AI results. | [optional] 
**size_by** | [**List[AacVisualizationStackedBucketsAllOfSizeBy]**](AacVisualizationStackedBucketsAllOfSizeBy.md) | Size by metrics bucket. | [optional] 
**stack_by** | [**List[AacVisualizationStackedBucketsAllOfStackBy]**](AacVisualizationStackedBucketsAllOfStackBy.md) | Stack by attributes bucket. | [optional] 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**to** | **object** | Free-form JSON object | [optional] 
**trend_by** | [**List[AacVisualizationStackedBucketsAllOfTrendBy]**](AacVisualizationStackedBucketsAllOfTrendBy.md) | Trend by attributes bucket. | [optional] 
**type** | **str** |  | 
**view_by** | [**List[AacVisualizationStackedBucketsAllOfViewBy]**](AacVisualizationStackedBucketsAllOfViewBy.md) | View by attributes bucket. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_visualization_stacked_buckets import AacVisualizationStackedBuckets

# TODO update the JSON string below
json = "{}"
# create an instance of AacVisualizationStackedBuckets from a JSON string
aac_visualization_stacked_buckets_instance = AacVisualizationStackedBuckets.from_json(json)
# print the JSON string representation of the object
print(AacVisualizationStackedBuckets.to_json())

# convert the object into a dict
aac_visualization_stacked_buckets_dict = aac_visualization_stacked_buckets_instance.to_dict()
# create an instance of AacVisualizationStackedBuckets from a dict
aac_visualization_stacked_buckets_from_dict = AacVisualizationStackedBuckets.from_dict(aac_visualization_stacked_buckets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


