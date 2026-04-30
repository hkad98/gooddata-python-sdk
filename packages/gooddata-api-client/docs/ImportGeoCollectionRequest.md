# ImportGeoCollectionRequest

Request to import a geo collection file from the staging area.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location** | **str** | Location of the file in the staging area. | 

## Example

```python
from gooddata_api_client.models.import_geo_collection_request import ImportGeoCollectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ImportGeoCollectionRequest from a JSON string
import_geo_collection_request_instance = ImportGeoCollectionRequest.from_json(json)
# print the JSON string representation of the object
print(ImportGeoCollectionRequest.to_json())

# convert the object into a dict
import_geo_collection_request_dict = import_geo_collection_request_instance.to_dict()
# create an instance of ImportGeoCollectionRequest from a dict
import_geo_collection_request_from_dict = ImportGeoCollectionRequest.from_dict(import_geo_collection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


