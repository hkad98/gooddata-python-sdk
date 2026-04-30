# DeclarativeAnalyticalDashboard


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certification** | **str** | Certification status of the entity. | [optional] 
**certification_message** | **str** | Optional message associated with the certification. | [optional] 
**certified_at** | **str** | Time when the certification was set. | [optional] 
**certified_by** | [**DeclarativeUserIdentifier**](DeclarativeUserIdentifier.md) |  | [optional] 
**content** | **object** | Free-form JSON object | 
**created_at** | **str** | Time of the entity creation. | [optional] 
**created_by** | [**DeclarativeUserIdentifier**](DeclarativeUserIdentifier.md) |  | [optional] 
**description** | **str** | Analytical dashboard description. | [optional] 
**id** | **str** | Analytical dashboard ID. | 
**modified_at** | **str** | Time of the last entity modification. | [optional] 
**modified_by** | [**DeclarativeUserIdentifier**](DeclarativeUserIdentifier.md) |  | [optional] 
**permissions** | [**List[DeclarativeAnalyticalDashboardPermissionsInner]**](DeclarativeAnalyticalDashboardPermissionsInner.md) | A list of permissions. | [optional] 
**summary** | **str** | AI-generated summary of the dashboard content | [optional] 
**tags** | **List[str]** | A list of tags. | [optional] 
**title** | **str** | Analytical dashboard title. | 

## Example

```python
from gooddata_api_client.models.declarative_analytical_dashboard import DeclarativeAnalyticalDashboard

# TODO update the JSON string below
json = "{}"
# create an instance of DeclarativeAnalyticalDashboard from a JSON string
declarative_analytical_dashboard_instance = DeclarativeAnalyticalDashboard.from_json(json)
# print the JSON string representation of the object
print(DeclarativeAnalyticalDashboard.to_json())

# convert the object into a dict
declarative_analytical_dashboard_dict = declarative_analytical_dashboard_instance.to_dict()
# create an instance of DeclarativeAnalyticalDashboard from a dict
declarative_analytical_dashboard_from_dict = DeclarativeAnalyticalDashboard.from_dict(declarative_analytical_dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


