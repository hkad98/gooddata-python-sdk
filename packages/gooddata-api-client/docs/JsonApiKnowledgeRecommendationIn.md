# JsonApiKnowledgeRecommendationIn

JSON:API representation of knowledgeRecommendation entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**JsonApiKnowledgeRecommendationInAttributes**](JsonApiKnowledgeRecommendationInAttributes.md) |  | 
**id** | **str** | API identifier of an object | 
**relationships** | [**JsonApiKnowledgeRecommendationInRelationships**](JsonApiKnowledgeRecommendationInRelationships.md) |  | 
**type** | **str** | Object type | 

## Example

```python
from gooddata_api_client.models.json_api_knowledge_recommendation_in import JsonApiKnowledgeRecommendationIn

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiKnowledgeRecommendationIn from a JSON string
json_api_knowledge_recommendation_in_instance = JsonApiKnowledgeRecommendationIn.from_json(json)
# print the JSON string representation of the object
print(JsonApiKnowledgeRecommendationIn.to_json())

# convert the object into a dict
json_api_knowledge_recommendation_in_dict = json_api_knowledge_recommendation_in_instance.to_dict()
# create an instance of JsonApiKnowledgeRecommendationIn from a dict
json_api_knowledge_recommendation_in_from_dict = JsonApiKnowledgeRecommendationIn.from_dict(json_api_knowledge_recommendation_in_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


