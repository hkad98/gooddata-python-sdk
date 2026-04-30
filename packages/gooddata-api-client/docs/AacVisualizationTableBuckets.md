# AacVisualizationTableBuckets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **Dict[str, object]** |  | [optional] 
**attributes** | [**List[AacVisualizationTableBucketsAllOfAttributes]**](AacVisualizationTableBucketsAllOfAttributes.md) | Attributes bucket (for scatter). | [optional] 
**columns** | [**List[AacVisualizationTableBucketsAllOfColumns]**](AacVisualizationTableBucketsAllOfColumns.md) | Columns bucket (for tables). | [optional] 
**config** | **object** | Free-form JSON object | [optional] 
**description** | **str** | Visualization description. | [optional] 
**var_from** | **object** | Free-form JSON object | [optional] 
**id** | **str** | Unique identifier of the visualization. | 
**is_hidden** | **bool** | Deprecated. Use showInAiResults instead. | [optional] 
**layers** | [**List[AacVisualizationLayer]**](AacVisualizationLayer.md) | Visualization data layers (for geo charts). | [optional] 
**metrics** | [**List[AacVisualizationTableBucketsAllOfMetrics]**](AacVisualizationTableBucketsAllOfMetrics.md) | Metrics bucket. | [optional] 
**query** | [**AacQuery**](AacQuery.md) |  | 
**rows** | [**List[AacVisualizationTableBucketsAllOfRows]**](AacVisualizationTableBucketsAllOfRows.md) | Rows bucket (for tables). | [optional] 
**segment_by** | [**List[AacVisualizationTableBucketsAllOfSegmentBy]**](AacVisualizationTableBucketsAllOfSegmentBy.md) | Segment by attributes bucket. | [optional] 
**show_in_ai_results** | **bool** | Whether to show in AI results. | [optional] 
**size_by** | [**List[AacVisualizationTableBucketsAllOfSizeBy]**](AacVisualizationTableBucketsAllOfSizeBy.md) | Size by metrics bucket. | [optional] 
**stack_by** | [**List[AacVisualizationTableBucketsAllOfStackBy]**](AacVisualizationTableBucketsAllOfStackBy.md) | Stack by attributes bucket. | [optional] 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**to** | **object** | Free-form JSON object | [optional] 
**trend_by** | [**List[AacVisualizationTableBucketsAllOfTrendBy]**](AacVisualizationTableBucketsAllOfTrendBy.md) | Trend by attributes bucket. | [optional] 
**type** | **str** |  | 
**view_by** | [**List[AacVisualizationTableBucketsAllOfViewBy]**](AacVisualizationTableBucketsAllOfViewBy.md) | View by attributes bucket. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_visualization_table_buckets import AacVisualizationTableBuckets

# TODO update the JSON string below
json = "{}"
# create an instance of AacVisualizationTableBuckets from a JSON string
aac_visualization_table_buckets_instance = AacVisualizationTableBuckets.from_json(json)
# print the JSON string representation of the object
print(AacVisualizationTableBuckets.to_json())

# convert the object into a dict
aac_visualization_table_buckets_dict = aac_visualization_table_buckets_instance.to_dict()
# create an instance of AacVisualizationTableBuckets from a dict
aac_visualization_table_buckets_from_dict = AacVisualizationTableBuckets.from_dict(aac_visualization_table_buckets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


