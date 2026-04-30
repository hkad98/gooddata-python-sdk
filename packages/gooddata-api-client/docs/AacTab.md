# AacTab

Dashboard tabs (for tabbed dashboards).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**Dict[str, AacDashboardFilter]**](AacDashboardFilter.md) | Tab-specific filters. | [optional] 
**id** | **str** | Unique identifier of the tab. | 
**sections** | [**List[AacSection]**](AacSection.md) | Sections within the tab. | [optional] 
**title** | **str** | Display title for the tab. | 

## Example

```python
from gooddata_api_client.models.aac_tab import AacTab

# TODO update the JSON string below
json = "{}"
# create an instance of AacTab from a JSON string
aac_tab_instance = AacTab.from_json(json)
# print the JSON string representation of the object
print(AacTab.to_json())

# convert the object into a dict
aac_tab_dict = aac_tab_instance.to_dict()
# create an instance of AacTab from a dict
aac_tab_from_dict = AacTab.from_dict(aac_tab_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


