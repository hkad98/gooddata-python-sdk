# ImportGeoCollectionResponse

Response after successfully importing a geo collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | The version of the imported geo collection. | 

## Example

```python
from gooddata_api_client.models.import_geo_collection_response import ImportGeoCollectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImportGeoCollectionResponse from a JSON string
import_geo_collection_response_instance = ImportGeoCollectionResponse.from_json(json)
# print the JSON string representation of the object
print(ImportGeoCollectionResponse.to_json())

# convert the object into a dict
import_geo_collection_response_dict = import_geo_collection_response_instance.to_dict()
# create an instance of ImportGeoCollectionResponse from a dict
import_geo_collection_response_from_dict = ImportGeoCollectionResponse.from_dict(import_geo_collection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


