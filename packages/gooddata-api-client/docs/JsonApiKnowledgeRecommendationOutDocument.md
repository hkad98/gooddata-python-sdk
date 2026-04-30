# JsonApiKnowledgeRecommendationOutDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**JsonApiKnowledgeRecommendationOut**](JsonApiKnowledgeRecommendationOut.md) |  | 
**included** | [**List[JsonApiKnowledgeRecommendationOutIncludes]**](JsonApiKnowledgeRecommendationOutIncludes.md) | Included resources | [optional] 
**links** | [**ObjectLinks**](ObjectLinks.md) |  | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_knowledge_recommendation_out_document import JsonApiKnowledgeRecommendationOutDocument

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiKnowledgeRecommendationOutDocument from a JSON string
json_api_knowledge_recommendation_out_document_instance = JsonApiKnowledgeRecommendationOutDocument.from_json(json)
# print the JSON string representation of the object
print(JsonApiKnowledgeRecommendationOutDocument.to_json())

# convert the object into a dict
json_api_knowledge_recommendation_out_document_dict = json_api_knowledge_recommendation_out_document_instance.to_dict()
# create an instance of JsonApiKnowledgeRecommendationOutDocument from a dict
json_api_knowledge_recommendation_out_document_from_dict = JsonApiKnowledgeRecommendationOutDocument.from_dict(json_api_knowledge_recommendation_out_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


