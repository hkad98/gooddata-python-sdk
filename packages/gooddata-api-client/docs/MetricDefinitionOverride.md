# MetricDefinitionOverride

(EXPERIMENTAL) Override for a catalog metric definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | [**InlineMeasureDefinition**](InlineMeasureDefinition.md) |  | 
**item** | [**AfmObjectIdentifierCore**](AfmObjectIdentifierCore.md) |  | 

## Example

```python
from gooddata_api_client.models.metric_definition_override import MetricDefinitionOverride

# TODO update the JSON string below
json = "{}"
# create an instance of MetricDefinitionOverride from a JSON string
metric_definition_override_instance = MetricDefinitionOverride.from_json(json)
# print the JSON string representation of the object
print(MetricDefinitionOverride.to_json())

# convert the object into a dict
metric_definition_override_dict = metric_definition_override_instance.to_dict()
# create an instance of MetricDefinitionOverride from a dict
metric_definition_override_from_dict = MetricDefinitionOverride.from_dict(metric_definition_override_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


