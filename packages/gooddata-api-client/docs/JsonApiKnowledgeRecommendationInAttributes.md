# JsonApiKnowledgeRecommendationInAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytical_dashboard_title** | **str** | Human-readable title of the analytical dashboard (denormalized for display) | [optional] 
**analyzed_period** | **str** | Analyzed time period (e.g., &#39;2023-07&#39; or &#39;July 2023&#39;) | [optional] 
**analyzed_value** | **object** | Metric value in the analyzed period (the observed value that triggered the anomaly) | [optional] 
**are_relations_valid** | **bool** |  | [optional] 
**comparison_type** | **str** | Time period for comparison | 
**confidence** | **object** | Confidence score (0.0 to 1.0) | [optional] 
**description** | **str** | Description of the recommendation | [optional] 
**direction** | **str** | Direction of the metric change | 
**metric_title** | **str** | Human-readable title of the metric (denormalized for display) | [optional] 
**recommendations** | **object** | Structured recommendations data as JSON | [optional] 
**reference_period** | **str** | Reference time period for comparison (e.g., &#39;2023-06&#39; or &#39;Jun 2023&#39;) | [optional] 
**reference_value** | **object** | Metric value in the reference period | [optional] 
**source_count** | **int** | Number of source documents used for generation | [optional] 
**tags** | **List[str]** |  | [optional] 
**title** | **str** | Human-readable title for the recommendation, e.g. &#39;Revenue decreased vs last month&#39; | 
**widget_id** | **str** | ID of the widget where the anomaly was detected | [optional] 
**widget_name** | **str** | Name of the widget where the anomaly was detected | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_knowledge_recommendation_in_attributes import JsonApiKnowledgeRecommendationInAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiKnowledgeRecommendationInAttributes from a JSON string
json_api_knowledge_recommendation_in_attributes_instance = JsonApiKnowledgeRecommendationInAttributes.from_json(json)
# print the JSON string representation of the object
print(JsonApiKnowledgeRecommendationInAttributes.to_json())

# convert the object into a dict
json_api_knowledge_recommendation_in_attributes_dict = json_api_knowledge_recommendation_in_attributes_instance.to_dict()
# create an instance of JsonApiKnowledgeRecommendationInAttributes from a dict
json_api_knowledge_recommendation_in_attributes_from_dict = JsonApiKnowledgeRecommendationInAttributes.from_dict(json_api_knowledge_recommendation_in_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


