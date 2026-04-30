# DependentEntitiesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifiers** | [**List[EntityIdentifier]**](EntityIdentifier.md) |  | 
**relation** | **str** | Entity relation for graph traversal from the entry points. DEPENDENTS returns entities that depend on the entry points. DEPENDENCIES returns entities that the entry points depend on. | [optional] [default to 'DEPENDENTS']

## Example

```python
from gooddata_api_client.models.dependent_entities_request import DependentEntitiesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DependentEntitiesRequest from a JSON string
dependent_entities_request_instance = DependentEntitiesRequest.from_json(json)
# print the JSON string representation of the object
print(DependentEntitiesRequest.to_json())

# convert the object into a dict
dependent_entities_request_dict = dependent_entities_request_instance.to_dict()
# create an instance of DependentEntitiesRequest from a dict
dependent_entities_request_from_dict = DependentEntitiesRequest.from_dict(dependent_entities_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


