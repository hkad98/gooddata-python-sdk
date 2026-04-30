# AacVisualizationBubbleBuckets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **Dict[str, object]** |  | [optional] 
**attributes** | [**List[AacVisualizationBubbleBucketsAllOfAttributes]**](AacVisualizationBubbleBucketsAllOfAttributes.md) | Attributes bucket (for scatter). | [optional] 
**columns** | [**List[AacVisualizationBubbleBucketsAllOfColumns]**](AacVisualizationBubbleBucketsAllOfColumns.md) | Columns bucket (for tables). | [optional] 
**config** | **object** | Free-form JSON object | [optional] 
**description** | **str** | Visualization description. | [optional] 
**var_from** | **object** | Free-form JSON object | [optional] 
**id** | **str** | Unique identifier of the visualization. | 
**is_hidden** | **bool** | Deprecated. Use showInAiResults instead. | [optional] 
**layers** | [**List[AacVisualizationLayer]**](AacVisualizationLayer.md) | Visualization data layers (for geo charts). | [optional] 
**metrics** | [**List[AacVisualizationBubbleBucketsAllOfMetrics]**](AacVisualizationBubbleBucketsAllOfMetrics.md) | Metrics bucket. | [optional] 
**query** | [**AacQuery**](AacQuery.md) |  | 
**rows** | [**List[AacVisualizationBubbleBucketsAllOfRows]**](AacVisualizationBubbleBucketsAllOfRows.md) | Rows bucket (for tables). | [optional] 
**segment_by** | [**List[AacVisualizationBubbleBucketsAllOfSegmentBy]**](AacVisualizationBubbleBucketsAllOfSegmentBy.md) | Segment by attributes bucket. | [optional] 
**show_in_ai_results** | **bool** | Whether to show in AI results. | [optional] 
**size_by** | [**List[AacVisualizationBubbleBucketsAllOfSizeBy]**](AacVisualizationBubbleBucketsAllOfSizeBy.md) | Size by metrics bucket. | [optional] 
**stack_by** | [**List[AacVisualizationBubbleBucketsAllOfStackBy]**](AacVisualizationBubbleBucketsAllOfStackBy.md) | Stack by attributes bucket. | [optional] 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**to** | **object** | Free-form JSON object | [optional] 
**trend_by** | [**List[AacVisualizationBubbleBucketsAllOfTrendBy]**](AacVisualizationBubbleBucketsAllOfTrendBy.md) | Trend by attributes bucket. | [optional] 
**type** | **str** |  | 
**view_by** | [**List[AacVisualizationBubbleBucketsAllOfViewBy]**](AacVisualizationBubbleBucketsAllOfViewBy.md) | View by attributes bucket. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_visualization_bubble_buckets import AacVisualizationBubbleBuckets

# TODO update the JSON string below
json = "{}"
# create an instance of AacVisualizationBubbleBuckets from a JSON string
aac_visualization_bubble_buckets_instance = AacVisualizationBubbleBuckets.from_json(json)
# print the JSON string representation of the object
print(AacVisualizationBubbleBuckets.to_json())

# convert the object into a dict
aac_visualization_bubble_buckets_dict = aac_visualization_bubble_buckets_instance.to_dict()
# create an instance of AacVisualizationBubbleBuckets from a dict
aac_visualization_bubble_buckets_from_dict = AacVisualizationBubbleBuckets.from_dict(aac_visualization_bubble_buckets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


