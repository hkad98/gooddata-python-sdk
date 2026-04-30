# JsonApiMetricInAttributesContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | Excel-like format string with optional dynamic tokens. Filter value tokens: [$FILTER:&lt;label_id&gt;] for raw filter value passthrough. Currency tokens: [$CURRENCY:&lt;label_id&gt;] for currency symbol, with optional forms :symbol, :narrow, :code, :name. Locale abbreviations: [$K], [$M], [$B], [$T] for locale-specific scale abbreviations. Tokens are resolved at execution time based on AFM filters and user&#39;s format locale. Single-value filters only; multi-value filters use fallback values. | [optional] 
**maql** | **str** |  | 
**metric_type** | **str** | Categorizes metric semantics (e.g., currency). | [optional] 

## Example

```python
from gooddata_api_client.models.json_api_metric_in_attributes_content import JsonApiMetricInAttributesContent

# TODO update the JSON string below
json = "{}"
# create an instance of JsonApiMetricInAttributesContent from a JSON string
json_api_metric_in_attributes_content_instance = JsonApiMetricInAttributesContent.from_json(json)
# print the JSON string representation of the object
print(JsonApiMetricInAttributesContent.to_json())

# convert the object into a dict
json_api_metric_in_attributes_content_dict = json_api_metric_in_attributes_content_instance.to_dict()
# create an instance of JsonApiMetricInAttributesContent from a dict
json_api_metric_in_attributes_content_from_dict = JsonApiMetricInAttributesContent.from_dict(json_api_metric_in_attributes_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


