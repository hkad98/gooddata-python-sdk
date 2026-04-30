# AacVisualizationLayer

Visualization data layers (for geo charts).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **Dict[str, object]** |  | [optional] 
**config** | **object** | Free-form JSON object | [optional] 
**filters** | [**Dict[str, AacQueryFilter]**](AacQueryFilter.md) | Layer filters. | [optional] 
**id** | **str** | Unique identifier of the layer. | 
**metrics** | [**List[AacVisualizationGeoBucketsAllOfViewBy]**](AacVisualizationGeoBucketsAllOfViewBy.md) | Layer metrics. | [optional] 
**segment_by** | [**List[AacVisualizationGeoBucketsAllOfViewBy]**](AacVisualizationGeoBucketsAllOfViewBy.md) | Layer segment by. | [optional] 
**sorts** | **List[object]** | Layer sorting definitions. | [optional] 
**title** | **str** | Layer title. | [optional] 
**type** | **str** | Layer type. | [optional] 
**view_by** | [**List[AacVisualizationGeoBucketsAllOfViewBy]**](AacVisualizationGeoBucketsAllOfViewBy.md) | Layer view by. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_visualization_layer import AacVisualizationLayer

# TODO update the JSON string below
json = "{}"
# create an instance of AacVisualizationLayer from a JSON string
aac_visualization_layer_instance = AacVisualizationLayer.from_json(json)
# print the JSON string representation of the object
print(AacVisualizationLayer.to_json())

# convert the object into a dict
aac_visualization_layer_dict = aac_visualization_layer_instance.to_dict()
# create an instance of AacVisualizationLayer from a dict
aac_visualization_layer_from_dict = AacVisualizationLayer.from_dict(aac_visualization_layer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


