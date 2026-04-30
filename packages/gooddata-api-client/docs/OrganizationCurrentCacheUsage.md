# OrganizationCurrentCacheUsage

Current cache usage of the organization.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cache_used** | **int** | Cache currently used by the organization, in bytes. | 
**removal_period_start** | **datetime** | Start timestamp of removal period. | [optional] 
**removed_since_start** | **int** | Bytes removed since start due to insufficient cache. | 

## Example

```python
from gooddata_api_client.models.organization_current_cache_usage import OrganizationCurrentCacheUsage

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationCurrentCacheUsage from a JSON string
organization_current_cache_usage_instance = OrganizationCurrentCacheUsage.from_json(json)
# print the JSON string representation of the object
print(OrganizationCurrentCacheUsage.to_json())

# convert the object into a dict
organization_current_cache_usage_dict = organization_current_cache_usage_instance.to_dict()
# create an instance of OrganizationCurrentCacheUsage from a dict
organization_current_cache_usage_from_dict = OrganizationCurrentCacheUsage.from_dict(organization_current_cache_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


