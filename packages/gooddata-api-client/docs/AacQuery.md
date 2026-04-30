# AacQuery

Query definition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**Dict[str, AacQueryFieldsValue]**](AacQueryFieldsValue.md) | Query fields map: localId -&gt; field definition (identifier string or structured object). | 
**filter_by** | [**Dict[str, AacQueryFilter]**](AacQueryFilter.md) | Query filters map: localId -&gt; filter definition. | [optional] 
**sort_by** | **List[object]** | Sorting definitions. | [optional] 

## Example

```python
from gooddata_api_client.models.aac_query import AacQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AacQuery from a JSON string
aac_query_instance = AacQuery.from_json(json)
# print the JSON string representation of the object
print(AacQuery.to_json())

# convert the object into a dict
aac_query_dict = aac_query_instance.to_dict()
# create an instance of AacQuery from a dict
aac_query_from_dict = AacQuery.from_dict(aac_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


