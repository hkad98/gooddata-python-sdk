# gooddata_api_client.CustomGeoCollectionControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_custom_geo_collections**](CustomGeoCollectionControllerApi.md#create_entity_custom_geo_collections) | **POST** /api/v1/entities/customGeoCollections | Post Custom Geo Collections
[**delete_entity_custom_geo_collections**](CustomGeoCollectionControllerApi.md#delete_entity_custom_geo_collections) | **DELETE** /api/v1/entities/customGeoCollections/{id} | Delete Custom Geo Collection
[**get_all_entities_custom_geo_collections**](CustomGeoCollectionControllerApi.md#get_all_entities_custom_geo_collections) | **GET** /api/v1/entities/customGeoCollections | Get all Custom Geo Collections
[**get_entity_custom_geo_collections**](CustomGeoCollectionControllerApi.md#get_entity_custom_geo_collections) | **GET** /api/v1/entities/customGeoCollections/{id} | Get Custom Geo Collection
[**patch_entity_custom_geo_collections**](CustomGeoCollectionControllerApi.md#patch_entity_custom_geo_collections) | **PATCH** /api/v1/entities/customGeoCollections/{id} | Patch Custom Geo Collection
[**update_entity_custom_geo_collections**](CustomGeoCollectionControllerApi.md#update_entity_custom_geo_collections) | **PUT** /api/v1/entities/customGeoCollections/{id} | Put Custom Geo Collection


# **create_entity_custom_geo_collections**
> JsonApiCustomGeoCollectionOutDocument create_entity_custom_geo_collections(json_api_custom_geo_collection_in_document)

Post Custom Geo Collections

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_custom_geo_collection_in_document import JsonApiCustomGeoCollectionInDocument
from gooddata_api_client.models.json_api_custom_geo_collection_out_document import JsonApiCustomGeoCollectionOutDocument
from gooddata_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gooddata_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with gooddata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gooddata_api_client.CustomGeoCollectionControllerApi(api_client)
    json_api_custom_geo_collection_in_document = gooddata_api_client.JsonApiCustomGeoCollectionInDocument() # JsonApiCustomGeoCollectionInDocument | 

    try:
        # Post Custom Geo Collections
        api_response = api_instance.create_entity_custom_geo_collections(json_api_custom_geo_collection_in_document)
        print("The response of CustomGeoCollectionControllerApi->create_entity_custom_geo_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGeoCollectionControllerApi->create_entity_custom_geo_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_api_custom_geo_collection_in_document** | [**JsonApiCustomGeoCollectionInDocument**](JsonApiCustomGeoCollectionInDocument.md)|  | 

### Return type

[**JsonApiCustomGeoCollectionOutDocument**](JsonApiCustomGeoCollectionOutDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.gooddata.api+json
 - **Accept**: application/json, application/vnd.gooddata.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Request successfully processed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_entity_custom_geo_collections**
> delete_entity_custom_geo_collections(id)

Delete Custom Geo Collection

### Example


```python
import gooddata_api_client
from gooddata_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gooddata_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with gooddata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gooddata_api_client.CustomGeoCollectionControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Custom Geo Collection
        api_instance.delete_entity_custom_geo_collections(id)
    except Exception as e:
        print("Exception when calling CustomGeoCollectionControllerApi->delete_entity_custom_geo_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_entities_custom_geo_collections**
> JsonApiCustomGeoCollectionOutList get_all_entities_custom_geo_collections(filter=filter, page=page, size=size, sort=sort, meta_include=meta_include)

Get all Custom Geo Collections

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_custom_geo_collection_out_list import JsonApiCustomGeoCollectionOutList
from gooddata_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gooddata_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with gooddata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gooddata_api_client.CustomGeoCollectionControllerApi(api_client)
    filter = 'name==someString;description==someString' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    meta_include = ['metaInclude=page,all'] # List[str] | Include Meta objects. (optional)

    try:
        # Get all Custom Geo Collections
        api_response = api_instance.get_all_entities_custom_geo_collections(filter=filter, page=page, size=size, sort=sort, meta_include=meta_include)
        print("The response of CustomGeoCollectionControllerApi->get_all_entities_custom_geo_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGeoCollectionControllerApi->get_all_entities_custom_geo_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 
 **meta_include** | [**List[str]**](str.md)| Include Meta objects. | [optional] 

### Return type

[**JsonApiCustomGeoCollectionOutList**](JsonApiCustomGeoCollectionOutList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.gooddata.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successfully processed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_custom_geo_collections**
> JsonApiCustomGeoCollectionOutDocument get_entity_custom_geo_collections(id, filter=filter)

Get Custom Geo Collection

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_custom_geo_collection_out_document import JsonApiCustomGeoCollectionOutDocument
from gooddata_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gooddata_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with gooddata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gooddata_api_client.CustomGeoCollectionControllerApi(api_client)
    id = 'id_example' # str | 
    filter = 'name==someString;description==someString' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)

    try:
        # Get Custom Geo Collection
        api_response = api_instance.get_entity_custom_geo_collections(id, filter=filter)
        print("The response of CustomGeoCollectionControllerApi->get_entity_custom_geo_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGeoCollectionControllerApi->get_entity_custom_geo_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 

### Return type

[**JsonApiCustomGeoCollectionOutDocument**](JsonApiCustomGeoCollectionOutDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/vnd.gooddata.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successfully processed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_entity_custom_geo_collections**
> JsonApiCustomGeoCollectionOutDocument patch_entity_custom_geo_collections(id, json_api_custom_geo_collection_patch_document, filter=filter)

Patch Custom Geo Collection

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_custom_geo_collection_out_document import JsonApiCustomGeoCollectionOutDocument
from gooddata_api_client.models.json_api_custom_geo_collection_patch_document import JsonApiCustomGeoCollectionPatchDocument
from gooddata_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gooddata_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with gooddata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gooddata_api_client.CustomGeoCollectionControllerApi(api_client)
    id = 'id_example' # str | 
    json_api_custom_geo_collection_patch_document = gooddata_api_client.JsonApiCustomGeoCollectionPatchDocument() # JsonApiCustomGeoCollectionPatchDocument | 
    filter = 'name==someString;description==someString' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)

    try:
        # Patch Custom Geo Collection
        api_response = api_instance.patch_entity_custom_geo_collections(id, json_api_custom_geo_collection_patch_document, filter=filter)
        print("The response of CustomGeoCollectionControllerApi->patch_entity_custom_geo_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGeoCollectionControllerApi->patch_entity_custom_geo_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **json_api_custom_geo_collection_patch_document** | [**JsonApiCustomGeoCollectionPatchDocument**](JsonApiCustomGeoCollectionPatchDocument.md)|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 

### Return type

[**JsonApiCustomGeoCollectionOutDocument**](JsonApiCustomGeoCollectionOutDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.gooddata.api+json
 - **Accept**: application/json, application/vnd.gooddata.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successfully processed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_custom_geo_collections**
> JsonApiCustomGeoCollectionOutDocument update_entity_custom_geo_collections(id, json_api_custom_geo_collection_in_document, filter=filter)

Put Custom Geo Collection

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_custom_geo_collection_in_document import JsonApiCustomGeoCollectionInDocument
from gooddata_api_client.models.json_api_custom_geo_collection_out_document import JsonApiCustomGeoCollectionOutDocument
from gooddata_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gooddata_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with gooddata_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gooddata_api_client.CustomGeoCollectionControllerApi(api_client)
    id = 'id_example' # str | 
    json_api_custom_geo_collection_in_document = gooddata_api_client.JsonApiCustomGeoCollectionInDocument() # JsonApiCustomGeoCollectionInDocument | 
    filter = 'name==someString;description==someString' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)

    try:
        # Put Custom Geo Collection
        api_response = api_instance.update_entity_custom_geo_collections(id, json_api_custom_geo_collection_in_document, filter=filter)
        print("The response of CustomGeoCollectionControllerApi->update_entity_custom_geo_collections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomGeoCollectionControllerApi->update_entity_custom_geo_collections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **json_api_custom_geo_collection_in_document** | [**JsonApiCustomGeoCollectionInDocument**](JsonApiCustomGeoCollectionInDocument.md)|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 

### Return type

[**JsonApiCustomGeoCollectionOutDocument**](JsonApiCustomGeoCollectionOutDocument.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/vnd.gooddata.api+json
 - **Accept**: application/json, application/vnd.gooddata.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successfully processed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

