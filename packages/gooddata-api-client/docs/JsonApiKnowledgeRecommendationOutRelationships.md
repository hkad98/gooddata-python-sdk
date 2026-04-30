# JsonApiKnowledgeRecommendationOutRelationships


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**analytical_dashboard** | [**JsonApiAutomationInRelationshipsAnalyticalDashboard**](JsonApiAutomationInRelationshipsAnalyticalDashboard.md) |  | [optional] 
**metric** | [**JsonApiKnowledgeRecommendationInRelationshipsMetric**](JsonApiKnowledgeRecommendationInRelationshipsMetric.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_knowledge_recommendation_out_relationships import JsonApiKnowledgeRecommendationOutRelationships

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiKnowledgeRecommendationOutRelationships from a JSON string
json_api_knowledge_recommendation_out_relationships_instance = JsonApiKnowledgeRecommendationOutRelationships.from_json(json)
# print the JSON string representation of the object
print(JsonApiKnowledgeRecommendationOutRelationships.to_json())

# convert the object into a dict
json_api_knowledge_recommendation_out_relationships_dict = json_api_knowledge_recommendation_out_relationships_instance.to_dict()
# create an instance of JsonApiKnowledgeRecommendationOutRelationships from a dict
json_api_knowledge_recommendation_out_relationships_from_dict = JsonApiKnowledgeRecommendationOutRelationships.from_dict(json_api_knowledge_recommendation_out_relationships_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


