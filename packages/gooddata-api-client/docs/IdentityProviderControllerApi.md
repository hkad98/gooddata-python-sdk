# gooddata_api_client.IdentityProviderControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_identity_providers**](IdentityProviderControllerApi.md#create_entity_identity_providers) | **POST** /api/v1/entities/identityProviders | Post Identity Providers
[**delete_entity_identity_providers**](IdentityProviderControllerApi.md#delete_entity_identity_providers) | **DELETE** /api/v1/entities/identityProviders/{id} | Delete Identity Provider
[**get_all_entities_identity_providers**](IdentityProviderControllerApi.md#get_all_entities_identity_providers) | **GET** /api/v1/entities/identityProviders | Get all Identity Providers
[**get_entity_identity_providers**](IdentityProviderControllerApi.md#get_entity_identity_providers) | **GET** /api/v1/entities/identityProviders/{id} | Get Identity Provider
[**patch_entity_identity_providers**](IdentityProviderControllerApi.md#patch_entity_identity_providers) | **PATCH** /api/v1/entities/identityProviders/{id} | Patch Identity Provider
[**update_entity_identity_providers**](IdentityProviderControllerApi.md#update_entity_identity_providers) | **PUT** /api/v1/entities/identityProviders/{id} | Put Identity Provider


# **create_entity_identity_providers**
> JsonApiIdentityProviderOutDocument create_entity_identity_providers(json_api_identity_provider_in_document)

Post Identity Providers

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_identity_provider_in_document import JsonApiIdentityProviderInDocument
from gooddata_api_client.models.json_api_identity_provider_out_document import JsonApiIdentityProviderOutDocument
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
    api_instance = gooddata_api_client.IdentityProviderControllerApi(api_client)
    json_api_identity_provider_in_document = gooddata_api_client.JsonApiIdentityProviderInDocument() # JsonApiIdentityProviderInDocument | 

    try:
        # Post Identity Providers
        api_response = api_instance.create_entity_identity_providers(json_api_identity_provider_in_document)
        print("The response of IdentityProviderControllerApi->create_entity_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderControllerApi->create_entity_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_api_identity_provider_in_document** | [**JsonApiIdentityProviderInDocument**](JsonApiIdentityProviderInDocument.md)|  | 

### Return type

[**JsonApiIdentityProviderOutDocument**](JsonApiIdentityProviderOutDocument.md)

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

# **delete_entity_identity_providers**
> delete_entity_identity_providers(id)

Delete Identity Provider

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
    api_instance = gooddata_api_client.IdentityProviderControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Identity Provider
        api_instance.delete_entity_identity_providers(id)
    except Exception as e:
        print("Exception when calling IdentityProviderControllerApi->delete_entity_identity_providers: %s\n" % e)
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

# **get_all_entities_identity_providers**
> JsonApiIdentityProviderOutList get_all_entities_identity_providers(filter=filter, page=page, size=size, sort=sort, meta_include=meta_include)

Get all Identity Providers

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_identity_provider_out_list import JsonApiIdentityProviderOutList
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
    api_instance = gooddata_api_client.IdentityProviderControllerApi(api_client)
    filter = 'identifiers==v1,v2,v3;customClaimMapping==MapValue' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    meta_include = ['metaInclude=page,all'] # List[str] | Include Meta objects. (optional)

    try:
        # Get all Identity Providers
        api_response = api_instance.get_all_entities_identity_providers(filter=filter, page=page, size=size, sort=sort, meta_include=meta_include)
        print("The response of IdentityProviderControllerApi->get_all_entities_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderControllerApi->get_all_entities_identity_providers: %s\n" % e)
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

[**JsonApiIdentityProviderOutList**](JsonApiIdentityProviderOutList.md)

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

# **get_entity_identity_providers**
> JsonApiIdentityProviderOutDocument get_entity_identity_providers(id, filter=filter)

Get Identity Provider

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_identity_provider_out_document import JsonApiIdentityProviderOutDocument
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
    api_instance = gooddata_api_client.IdentityProviderControllerApi(api_client)
    id = 'id_example' # str | 
    filter = 'identifiers==v1,v2,v3;customClaimMapping==MapValue' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)

    try:
        # Get Identity Provider
        api_response = api_instance.get_entity_identity_providers(id, filter=filter)
        print("The response of IdentityProviderControllerApi->get_entity_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderControllerApi->get_entity_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 

### Return type

[**JsonApiIdentityProviderOutDocument**](JsonApiIdentityProviderOutDocument.md)

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

# **patch_entity_identity_providers**
> JsonApiIdentityProviderOutDocument patch_entity_identity_providers(id, json_api_identity_provider_patch_document, filter=filter)

Patch Identity Provider

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_identity_provider_out_document import JsonApiIdentityProviderOutDocument
from gooddata_api_client.models.json_api_identity_provider_patch_document import JsonApiIdentityProviderPatchDocument
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
    api_instance = gooddata_api_client.IdentityProviderControllerApi(api_client)
    id = 'id_example' # str | 
    json_api_identity_provider_patch_document = gooddata_api_client.JsonApiIdentityProviderPatchDocument() # JsonApiIdentityProviderPatchDocument | 
    filter = 'identifiers==v1,v2,v3;customClaimMapping==MapValue' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)

    try:
        # Patch Identity Provider
        api_response = api_instance.patch_entity_identity_providers(id, json_api_identity_provider_patch_document, filter=filter)
        print("The response of IdentityProviderControllerApi->patch_entity_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderControllerApi->patch_entity_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **json_api_identity_provider_patch_document** | [**JsonApiIdentityProviderPatchDocument**](JsonApiIdentityProviderPatchDocument.md)|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 

### Return type

[**JsonApiIdentityProviderOutDocument**](JsonApiIdentityProviderOutDocument.md)

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

# **update_entity_identity_providers**
> JsonApiIdentityProviderOutDocument update_entity_identity_providers(id, json_api_identity_provider_in_document, filter=filter)

Put Identity Provider

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_identity_provider_in_document import JsonApiIdentityProviderInDocument
from gooddata_api_client.models.json_api_identity_provider_out_document import JsonApiIdentityProviderOutDocument
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
    api_instance = gooddata_api_client.IdentityProviderControllerApi(api_client)
    id = 'id_example' # str | 
    json_api_identity_provider_in_document = gooddata_api_client.JsonApiIdentityProviderInDocument() # JsonApiIdentityProviderInDocument | 
    filter = 'identifiers==v1,v2,v3;customClaimMapping==MapValue' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)

    try:
        # Put Identity Provider
        api_response = api_instance.update_entity_identity_providers(id, json_api_identity_provider_in_document, filter=filter)
        print("The response of IdentityProviderControllerApi->update_entity_identity_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IdentityProviderControllerApi->update_entity_identity_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **json_api_identity_provider_in_document** | [**JsonApiIdentityProviderInDocument**](JsonApiIdentityProviderInDocument.md)|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 

### Return type

[**JsonApiIdentityProviderOutDocument**](JsonApiIdentityProviderOutDocument.md)

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

