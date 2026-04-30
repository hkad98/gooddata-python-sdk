# AacAttributeHierarchy

AAC attribute hierarchy definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | **List[str]** | Ordered list of attribute identifiers (first is top level). | 
**description** | **str** | Attribute hierarchy description. | [optional] 
**id** | **str** | Unique identifier of the attribute hierarchy. | 
**tags** | **List[str]** | Metadata tags. | [optional] 
**title** | **str** | Human readable title. | [optional] 
**type** | **str** | Attribute hierarchy type discriminator. | 

## Example

```python
from gooddata_api_client.models.aac_attribute_hierarchy import AacAttributeHierarchy

# TODO update the JSON string below
json = "{}"
# create an instance of AacAttributeHierarchy from a JSON string
aac_attribute_hierarchy_instance = AacAttributeHierarchy.from_json(json)
# print the JSON string representation of the object
print(AacAttributeHierarchy.to_json())

# convert the object into a dict
aac_attribute_hierarchy_dict = aac_attribute_hierarchy_instance.to_dict()
# create an instance of AacAttributeHierarchy from a dict
aac_attribute_hierarchy_from_dict = AacAttributeHierarchy.from_dict(aac_attribute_hierarchy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


