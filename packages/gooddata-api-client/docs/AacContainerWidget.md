# AacContainerWidget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_properties** | **Dict[str, object]** |  | [optional] 
**columns** | **int** | Widget width in grid columns (GAAC). | [optional] 
**container** | **str** | Container widget identifier. | [optional] 
**content** | **str** | Rich text content. | [optional] 
**var_date** | **str** | Date dataset for filtering. | [optional] 
**description** | [**AacContainerWidgetAllOfDescription**](AacContainerWidgetAllOfDescription.md) |  | [optional] 
**drill_down** | **object** | Free-form JSON object | [optional] 
**enable_section_headers** | **bool** | Whether section headers are enabled for container widgets. | [optional] 
**ignore_dashboard_filters** | **List[str]** | Deprecated. Use ignoredFilters instead. | [optional] 
**ignored_filters** | **List[str]** | A list of dashboard filters to be ignored for this widget (GAAC). | [optional] 
**interactions** | **List[object]** | Widget interactions (GAAC). | [optional] 
**layout_direction** | **str** | Layout direction for container widgets. | [optional] 
**metric** | **str** | Inline metric reference. | [optional] 
**rows** | **int** | Widget height in grid rows (GAAC). | [optional] 
**sections** | [**List[AacSection]**](AacSection.md) | Nested sections for layout widgets. | 
**size** | [**AacWidgetSize**](AacWidgetSize.md) |  | [optional] 
**title** | [**AacContainerWidgetAllOfTitle**](AacContainerWidgetAllOfTitle.md) |  | [optional] 
**type** | **str** | Widget type. | [optional] 
**visualization** | **str** | Visualization ID reference. | [optional] 
**visualizations** | [**List[AacWidget]**](AacWidget.md) | Visualization switcher items. | [optional] 
**zoom_data** | **bool** | Enable zooming to the data for certain visualization types (GAAC). | [optional] 

## Example

```python
from gooddata_api_client.models.aac_container_widget import AacContainerWidget

# TODO update the JSON string below
json = "{}"
# create an instance of AacContainerWidget from a JSON string
aac_container_widget_instance = AacContainerWidget.from_json(json)
# print the JSON string representation of the object
print(AacContainerWidget.to_json())

# convert the object into a dict
aac_container_widget_dict = aac_container_widget_instance.to_dict()
# create an instance of AacContainerWidget from a dict
aac_container_widget_from_dict = AacContainerWidget.from_dict(aac_container_widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


