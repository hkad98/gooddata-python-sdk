# AacVisualizationScatterBuckets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **Dict[str, object]** |  | [optional] 
**attributes** | [**List[AacVisualizationScatterBucketsAllOfAttributes]**](AacVisualizationScatterBucketsAllOfAttributes.md) | Attributes bucket (for scatter). | [optional] 
**columns** | [**List[AacVisualizationScatterBucketsAllOfColumns]**](AacVisualizationScatterBucketsAllOfColumns.md) | Columns bucket (for tables). | [optional] 
**config** | **object** | Free-form JSON object | [optional] 
**description** | **str** | Visualization description. | [optional] 
**var_from** | **object** | Free-form JSON object | [optional] 
**id** | **str** | Unique identifier of the visualization. | 
**is_hidden** | **bool** | Deprecated. Use showInAiResults instead. | [optional] 
**layers** | [**List[AacVisualizationLayer]**](AacVisualizationLayer.md) | Visualization data layers (for geo charts). | [optional] 
**metrics** | [**List[AacVisualizationScatterBucketsAllOfMetrics]**](AacVisualizationScatterBucketsAllOfMetrics.md) | Metrics bucket. | [optional] 
**query** | [**AacQuery**](AacQuery.md) |  | 
**rows** | [**List[AacVisualizationScatterBucketsAllOfRows]**](AacVisualizationScatterBucketsAllOfRows.md) | Rows bucket (for tables). | [optional] 
**segment_by** | [**List[AacVisualizationScatterBucketsAllOfSegmentBy]**](AacVisualizationScatterBucketsAllOfSegmentBy.md) | Segment by attributes bucket. | [optional] 
**show_in_ai_results** | **bool** | Whether to show in AI results. | [optional] 
**size_by** | [**List[AacVisualizationScatterBucketsAllOfSizeBy]**](AacVisualizationScatterBucketsAllOfSizeBy.md) | Size by metrics bucket. | [optional] 
**stack_by** | [**List[AacVisualizationScatterBucketsAllOfStackBy]**](AacVisualizationScatterBucketsAllOfStackBy.md) | Stack by attributes bucket. | [optional] 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**to** | **object** | Free-form JSON object | [optional] 
**trend_by** | [**List[AacVisualizationScatterBucketsAllOfTrendBy]**](AacVisualizationScatterBucketsAllOfTrendBy.md) | Trend by attributes bucket. | [optional] 
**type** | **str** |  | 
**view_by** | [**List[AacVisualizationScatterBucketsAllOfViewBy]**](AacVisualizationScatterBucketsAllOfViewBy.md) | View by attributes bucket. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_visualization_scatter_buckets import AacVisualizationScatterBuckets

# TODO update the JSON string below
json = "{}"
# create an instance of AacVisualizationScatterBuckets from a JSON string
aac_visualization_scatter_buckets_instance = AacVisualizationScatterBuckets.from_json(json)
# print the JSON string representation of the object
print(AacVisualizationScatterBuckets.to_json())

# convert the object into a dict
aac_visualization_scatter_buckets_dict = aac_visualization_scatter_buckets_instance.to_dict()
# create an instance of AacVisualizationScatterBuckets from a dict
aac_visualization_scatter_buckets_from_dict = AacVisualizationScatterBuckets.from_dict(aac_visualization_scatter_buckets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


