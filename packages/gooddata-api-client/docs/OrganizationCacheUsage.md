# OrganizationCacheUsage

Data about the whole organization's cache usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current** | [**OrganizationCurrentCacheUsage**](OrganizationCurrentCacheUsage.md) |  | 
**removal_intervals** | [**List[CacheRemovalInterval]**](CacheRemovalInterval.md) | List of cache removal intervals. | 
**settings** | [**OrganizationCacheSettings**](OrganizationCacheSettings.md) |  | 

## Example

```python
from gooddata_api_client.models.organization_cache_usage import OrganizationCacheUsage

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCacheUsage from a JSON string
organization_cache_usage_instance = OrganizationCacheUsage.from_json(json)
# print the JSON string representation of the object
print(OrganizationCacheUsage.to_json())

# convert the object into a dict
organization_cache_usage_dict = organization_cache_usage_instance.to_dict()
# create an instance of OrganizationCacheUsage from a dict
organization_cache_usage_from_dict = OrganizationCacheUsage.from_dict(organization_cache_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


