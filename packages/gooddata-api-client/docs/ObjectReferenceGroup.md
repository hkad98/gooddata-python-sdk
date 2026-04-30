# ObjectReferenceGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ObjectReference**](ObjectReference.md) |  | [optional] 
**objects** | [**List[ObjectReference]**](ObjectReference.md) | Objects the user explicitly referenced within this context. | 

## Example

```python
from gooddata_api_client.models.object_reference_group import ObjectReferenceGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectReferenceGroup from a JSON string
object_reference_group_instance = ObjectReferenceGroup.from_json(json)
# print the JSON string representation of the object
print(ObjectReferenceGroup.to_json())

# convert the object into a dict
object_reference_group_dict = object_reference_group_instance.to_dict()
# create an instance of ObjectReferenceGroup from a dict
object_reference_group_from_dict = ObjectReferenceGroup.from_dict(object_reference_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


