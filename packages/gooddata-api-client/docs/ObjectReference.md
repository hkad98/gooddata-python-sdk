# ObjectReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Object identifier (e.g. widget ID, metric ID). | 
**type** | **str** | Type of the referenced object. | 

## Example

```python
from gooddata_api_client.models.object_reference import ObjectReference

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectReference from a JSON string
object_reference_instance = ObjectReference.from_json(json)
# print the JSON string representation of the object
print(ObjectReference.to_json())

# convert the object into a dict
object_reference_dict = object_reference_instance.to_dict()
# create an instance of ObjectReference from a dict
object_reference_from_dict = ObjectReference.from_dict(object_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


