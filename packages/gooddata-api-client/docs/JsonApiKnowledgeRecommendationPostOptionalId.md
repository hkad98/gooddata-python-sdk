# JsonApiKnowledgeRecommendationPostOptionalId

JSON:API representation of knowledgeRecommendation entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**JsonApiKnowledgeRecommendationInAttributes**](JsonApiKnowledgeRecommendationInAttributes.md) |  | 
**id** | **str** | API identifier of an object | [optional] 
**relationships** | [**JsonApiKnowledgeRecommendationInRelationships**](JsonApiKnowledgeRecommendationInRelationships.md) |  | 
**type** | **str** | Object type | 

## Example

```python
from gooddata_api_client.models.json_api_knowledge_recommendation_post_optional_id import JsonApiKnowledgeRecommendationPostOptionalId

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiKnowledgeRecommendationPostOptionalId from a JSON string
json_api_knowledge_recommendation_post_optional_id_instance = JsonApiKnowledgeRecommendationPostOptionalId.from_json(json)
# print the JSON string representation of the object
print(JsonApiKnowledgeRecommendationPostOptionalId.to_json())

# convert the object into a dict
json_api_knowledge_recommendation_post_optional_id_dict = json_api_knowledge_recommendation_post_optional_id_instance.to_dict()
# create an instance of JsonApiKnowledgeRecommendationPostOptionalId from a dict
json_api_knowledge_recommendation_post_optional_id_from_dict = JsonApiKnowledgeRecommendationPostOptionalId.from_dict(json_api_knowledge_recommendation_post_optional_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


