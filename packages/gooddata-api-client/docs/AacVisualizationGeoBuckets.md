# AacVisualizationGeoBuckets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **Dict[str, object]** |  | [optional] 
**attributes** | [**List[AacVisualizationGeoBucketsAllOfAttributes]**](AacVisualizationGeoBucketsAllOfAttributes.md) | Attributes bucket (for scatter). | [optional] 
**columns** | [**List[AacVisualizationGeoBucketsAllOfColumns]**](AacVisualizationGeoBucketsAllOfColumns.md) | Columns bucket (for tables). | [optional] 
**config** | **object** | Free-form JSON object | [optional] 
**description** | **str** | Visualization description. | [optional] 
**var_from** | **object** | Free-form JSON object | [optional] 
**id** | **str** | Unique identifier of the visualization. | 
**is_hidden** | **bool** | Deprecated. Use showInAiResults instead. | [optional] 
**layers** | [**List[AacVisualizationLayer]**](AacVisualizationLayer.md) | Visualization data layers (for geo charts). | [optional] 
**metrics** | [**List[AacVisualizationGeoBucketsAllOfMetrics]**](AacVisualizationGeoBucketsAllOfMetrics.md) | Metrics bucket. | [optional] 
**query** | [**AacQuery**](AacQuery.md) |  | 
**rows** | [**List[AacVisualizationGeoBucketsAllOfRows]**](AacVisualizationGeoBucketsAllOfRows.md) | Rows bucket (for tables). | [optional] 
**segment_by** | [**List[AacVisualizationGeoBucketsAllOfSegmentBy]**](AacVisualizationGeoBucketsAllOfSegmentBy.md) | Segment by attributes bucket. | [optional] 
**show_in_ai_results** | **bool** | Whether to show in AI results. | [optional] 
**size_by** | [**List[AacVisualizationGeoBucketsAllOfSizeBy]**](AacVisualizationGeoBucketsAllOfSizeBy.md) | Size by metrics bucket. | [optional] 
**stack_by** | [**List[AacVisualizationGeoBucketsAllOfStackBy]**](AacVisualizationGeoBucketsAllOfStackBy.md) | Stack by attributes bucket. | [optional] 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**to** | **object** | Free-form JSON object | [optional] 
**trend_by** | [**List[AacVisualizationGeoBucketsAllOfTrendBy]**](AacVisualizationGeoBucketsAllOfTrendBy.md) | Trend by attributes bucket. | [optional] 
**type** | **str** |  | 
**view_by** | [**List[AacVisualizationGeoBucketsAllOfViewBy]**](AacVisualizationGeoBucketsAllOfViewBy.md) | View by attributes bucket. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_visualization_geo_buckets import AacVisualizationGeoBuckets

# TODO update the JSON string below
json = "{}"
# create an instance of AacVisualizationGeoBuckets from a JSON string
aac_visualization_geo_buckets_instance = AacVisualizationGeoBuckets.from_json(json)
# print the JSON string representation of the object
print(AacVisualizationGeoBuckets.to_json())

# convert the object into a dict
aac_visualization_geo_buckets_dict = aac_visualization_geo_buckets_instance.to_dict()
# create an instance of AacVisualizationGeoBuckets from a dict
aac_visualization_geo_buckets_from_dict = AacVisualizationGeoBuckets.from_dict(aac_visualization_geo_buckets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


