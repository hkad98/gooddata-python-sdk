# TrendingObjectItem

Trending analytics catalog objects

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | Timestamp when object was created. | [optional] 
**created_by** | **str** | ID of the user who created the object. | [optional] 
**dataset_id** | **str** | ID of the associated dataset, if applicable. | [optional] 
**dataset_title** | **str** | Title of the associated dataset, if applicable. | [optional] 
**dataset_type** | **str** | Type of the associated dataset, if applicable. | [optional] 
**description** | **str** | Object description. | [optional] 
**id** | **str** | Object ID. | 
**is_hidden** | **bool** | If true, this object is hidden from AI search results by default. | [optional] 
**is_hidden_from_kda** | **bool** | If true, this object is hidden from KDA. | [optional] 
**metric_type** | **str** | Type of the metric (e.g. MAQL), if applicable. | [optional] 
**modified_at** | **datetime** | Timestamp when object was last modified. | [optional] 
**modified_by** | **str** | ID of the user who last modified the object. | [optional] 
**tags** | **List[str]** |  | 
**title** | **str** | Object title. | 
**type** | **str** | Object type, e.g. dashboard, visualization, metric. | 
**usage_count** | **int** | Number of times this object has been used/referenced. | 
**visualization_url** | **str** | URL of the visualization, if applicable. | [optional] 
**workspace_id** | **str** | Workspace ID the object belongs to. | 

## Example

```python
from gooddata_api_client.models.trending_object_item import TrendingObjectItem

# TODO update the JSON string below
json = "{}"
# create an instance of TrendingObjectItem from a JSON string
trending_object_item_instance = TrendingObjectItem.from_json(json)
# print the JSON string representation of the object
print(TrendingObjectItem.to_json())

# convert the object into a dict
trending_object_item_dict = trending_object_item_instance.to_dict()
# create an instance of TrendingObjectItem from a dict
trending_object_item_from_dict = TrendingObjectItem.from_dict(trending_object_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


