# AnalyticsCatalogCreatedBy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reasoning** | **str** | Reasoning for error states | 
**users** | [**List[AnalyticsCatalogUser]**](AnalyticsCatalogUser.md) | Users who created any object in the catalog | 

## Example

```python
from gooddata_api_client.models.analytics_catalog_created_by import AnalyticsCatalogCreatedBy

# TODO update the JSON string below
json = "{}"
# create an instance of AnalyticsCatalogCreatedBy from a JSON string
analytics_catalog_created_by_instance = AnalyticsCatalogCreatedBy.from_json(json)
# print the JSON string representation of the object
print(AnalyticsCatalogCreatedBy.to_json())

# convert the object into a dict
analytics_catalog_created_by_dict = analytics_catalog_created_by_instance.to_dict()
# create an instance of AnalyticsCatalogCreatedBy from a dict
analytics_catalog_created_by_from_dict = AnalyticsCatalogCreatedBy.from_dict(analytics_catalog_created_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


