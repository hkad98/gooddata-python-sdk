# gooddata_api_client.MemoryItemControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_memory_items**](MemoryItemControllerApi.md#create_entity_memory_items) | **POST** /api/v1/entities/workspaces/{workspaceId}/memoryItems | Post Memory Items
[**delete_entity_memory_items**](MemoryItemControllerApi.md#delete_entity_memory_items) | **DELETE** /api/v1/entities/workspaces/{workspaceId}/memoryItems/{objectId} | Delete a Memory Item
[**get_all_entities_memory_items**](MemoryItemControllerApi.md#get_all_entities_memory_items) | **GET** /api/v1/entities/workspaces/{workspaceId}/memoryItems | Get all Memory Items
[**get_entity_memory_items**](MemoryItemControllerApi.md#get_entity_memory_items) | **GET** /api/v1/entities/workspaces/{workspaceId}/memoryItems/{objectId} | Get a Memory Item
[**patch_entity_memory_items**](MemoryItemControllerApi.md#patch_entity_memory_items) | **PATCH** /api/v1/entities/workspaces/{workspaceId}/memoryItems/{objectId} | Patch a Memory Item
[**search_entities_memory_items**](MemoryItemControllerApi.md#search_entities_memory_items) | **POST** /api/v1/entities/workspaces/{workspaceId}/memoryItems/search | The search endpoint (beta)
[**update_entity_memory_items**](MemoryItemControllerApi.md#update_entity_memory_items) | **PUT** /api/v1/entities/workspaces/{workspaceId}/memoryItems/{objectId} | Put a Memory Item


# **create_entity_memory_items**
> JsonApiMemoryItemOutDocument create_entity_memory_items(workspace_id, json_api_memory_item_post_optional_id_document, include=include, meta_include=meta_include)

Post Memory Items

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_memory_item_out_document import JsonApiMemoryItemOutDocument
from gooddata_api_client.models.json_api_memory_item_post_optional_id_document import JsonApiMemoryItemPostOptionalIdDocument
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
    api_instance = gooddata_api_client.MemoryItemControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    json_api_memory_item_post_optional_id_document = gooddata_api_client.JsonApiMemoryItemPostOptionalIdDocument() # JsonApiMemoryItemPostOptionalIdDocument | 
    include = ['createdBy,modifiedBy'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)
    meta_include = ['metaInclude=origin,all'] # List[str] | Include Meta objects. (optional)

    try:
        # Post Memory Items
        api_response = api_instance.create_entity_memory_items(workspace_id, json_api_memory_item_post_optional_id_document, include=include, meta_include=meta_include)
        print("The response of MemoryItemControllerApi->create_entity_memory_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryItemControllerApi->create_entity_memory_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **json_api_memory_item_post_optional_id_document** | [**JsonApiMemoryItemPostOptionalIdDocument**](JsonApiMemoryItemPostOptionalIdDocument.md)|  | 
 **include** | [**List[str]**](str.md)| Array of included collections or individual relationships. Includes are separated by commas (e.g. include&#x3D;entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \&quot;ALL\&quot; is present, all possible includes are used (include&#x3D;ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. | [optional] 
 **meta_include** | [**List[str]**](str.md)| Include Meta objects. | [optional] 

### Return type

[**JsonApiMemoryItemOutDocument**](JsonApiMemoryItemOutDocument.md)

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

# **delete_entity_memory_items**
> delete_entity_memory_items(workspace_id, object_id)

Delete a Memory Item

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
    api_instance = gooddata_api_client.MemoryItemControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    object_id = 'object_id_example' # str | 

    try:
        # Delete a Memory Item
        api_instance.delete_entity_memory_items(workspace_id, object_id)
    except Exception as e:
        print("Exception when calling MemoryItemControllerApi->delete_entity_memory_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **object_id** | **str**|  | 

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

# **get_all_entities_memory_items**
> JsonApiMemoryItemOutList get_all_entities_memory_items(workspace_id, origin=origin, filter=filter, include=include, page=page, size=size, sort=sort, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)

Get all Memory Items

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_memory_item_out_list import JsonApiMemoryItemOutList
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
    api_instance = gooddata_api_client.MemoryItemControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    origin = ALL # str |  (optional) (default to ALL)
    filter = 'title==someString;description==someString;createdBy.id==321;modifiedBy.id==321' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    include = ['createdBy,modifiedBy'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    x_gdc_validate_relations = False # bool |  (optional) (default to False)
    meta_include = ['metaInclude=origin,page,all'] # List[str] | Include Meta objects. (optional)

    try:
        # Get all Memory Items
        api_response = api_instance.get_all_entities_memory_items(workspace_id, origin=origin, filter=filter, include=include, page=page, size=size, sort=sort, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)
        print("The response of MemoryItemControllerApi->get_all_entities_memory_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryItemControllerApi->get_all_entities_memory_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **origin** | **str**|  | [optional] [default to ALL]
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 
 **include** | [**List[str]**](str.md)| Array of included collections or individual relationships. Includes are separated by commas (e.g. include&#x3D;entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \&quot;ALL\&quot; is present, all possible includes are used (include&#x3D;ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. | [optional] 
 **page** | **int**| Zero-based page index (0..N) | [optional] [default to 0]
 **size** | **int**| The size of the page to be returned | [optional] [default to 20]
 **sort** | [**List[str]**](str.md)| Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. | [optional] 
 **x_gdc_validate_relations** | **bool**|  | [optional] [default to False]
 **meta_include** | [**List[str]**](str.md)| Include Meta objects. | [optional] 

### Return type

[**JsonApiMemoryItemOutList**](JsonApiMemoryItemOutList.md)

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

# **get_entity_memory_items**
> JsonApiMemoryItemOutDocument get_entity_memory_items(workspace_id, object_id, filter=filter, include=include, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)

Get a Memory Item

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_memory_item_out_document import JsonApiMemoryItemOutDocument
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
    api_instance = gooddata_api_client.MemoryItemControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    object_id = 'object_id_example' # str | 
    filter = 'title==someString;description==someString;createdBy.id==321;modifiedBy.id==321' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    include = ['createdBy,modifiedBy'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)
    x_gdc_validate_relations = False # bool |  (optional) (default to False)
    meta_include = ['metaInclude=origin,all'] # List[str] | Include Meta objects. (optional)

    try:
        # Get a Memory Item
        api_response = api_instance.get_entity_memory_items(workspace_id, object_id, filter=filter, include=include, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)
        print("The response of MemoryItemControllerApi->get_entity_memory_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryItemControllerApi->get_entity_memory_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **object_id** | **str**|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 
 **include** | [**List[str]**](str.md)| Array of included collections or individual relationships. Includes are separated by commas (e.g. include&#x3D;entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \&quot;ALL\&quot; is present, all possible includes are used (include&#x3D;ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. | [optional] 
 **x_gdc_validate_relations** | **bool**|  | [optional] [default to False]
 **meta_include** | [**List[str]**](str.md)| Include Meta objects. | [optional] 

### Return type

[**JsonApiMemoryItemOutDocument**](JsonApiMemoryItemOutDocument.md)

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

# **patch_entity_memory_items**
> JsonApiMemoryItemOutDocument patch_entity_memory_items(workspace_id, object_id, json_api_memory_item_patch_document, filter=filter, include=include)

Patch a Memory Item

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_memory_item_out_document import JsonApiMemoryItemOutDocument
from gooddata_api_client.models.json_api_memory_item_patch_document import JsonApiMemoryItemPatchDocument
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
    api_instance = gooddata_api_client.MemoryItemControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    object_id = 'object_id_example' # str | 
    json_api_memory_item_patch_document = gooddata_api_client.JsonApiMemoryItemPatchDocument() # JsonApiMemoryItemPatchDocument | 
    filter = 'title==someString;description==someString;createdBy.id==321;modifiedBy.id==321' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    include = ['createdBy,modifiedBy'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)

    try:
        # Patch a Memory Item
        api_response = api_instance.patch_entity_memory_items(workspace_id, object_id, json_api_memory_item_patch_document, filter=filter, include=include)
        print("The response of MemoryItemControllerApi->patch_entity_memory_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryItemControllerApi->patch_entity_memory_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **object_id** | **str**|  | 
 **json_api_memory_item_patch_document** | [**JsonApiMemoryItemPatchDocument**](JsonApiMemoryItemPatchDocument.md)|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 
 **include** | [**List[str]**](str.md)| Array of included collections or individual relationships. Includes are separated by commas (e.g. include&#x3D;entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \&quot;ALL\&quot; is present, all possible includes are used (include&#x3D;ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. | [optional] 

### Return type

[**JsonApiMemoryItemOutDocument**](JsonApiMemoryItemOutDocument.md)

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

# **search_entities_memory_items**
> JsonApiMemoryItemOutList search_entities_memory_items(workspace_id, entity_search_body, origin=origin, x_gdc_validate_relations=x_gdc_validate_relations)

The search endpoint (beta)

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.entity_search_body import EntitySearchBody
from gooddata_api_client.models.json_api_memory_item_out_list import JsonApiMemoryItemOutList
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
    api_instance = gooddata_api_client.MemoryItemControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    entity_search_body = gooddata_api_client.EntitySearchBody() # EntitySearchBody | Search request body with filter, pagination, and sorting options
    origin = ALL # str |  (optional) (default to ALL)
    x_gdc_validate_relations = False # bool |  (optional) (default to False)

    try:
        # The search endpoint (beta)
        api_response = api_instance.search_entities_memory_items(workspace_id, entity_search_body, origin=origin, x_gdc_validate_relations=x_gdc_validate_relations)
        print("The response of MemoryItemControllerApi->search_entities_memory_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryItemControllerApi->search_entities_memory_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **entity_search_body** | [**EntitySearchBody**](EntitySearchBody.md)| Search request body with filter, pagination, and sorting options | 
 **origin** | **str**|  | [optional] [default to ALL]
 **x_gdc_validate_relations** | **bool**|  | [optional] [default to False]

### Return type

[**JsonApiMemoryItemOutList**](JsonApiMemoryItemOutList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/vnd.gooddata.api+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successfully processed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_entity_memory_items**
> JsonApiMemoryItemOutDocument update_entity_memory_items(workspace_id, object_id, json_api_memory_item_in_document, filter=filter, include=include)

Put a Memory Item

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_memory_item_in_document import JsonApiMemoryItemInDocument
from gooddata_api_client.models.json_api_memory_item_out_document import JsonApiMemoryItemOutDocument
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
    api_instance = gooddata_api_client.MemoryItemControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    object_id = 'object_id_example' # str | 
    json_api_memory_item_in_document = gooddata_api_client.JsonApiMemoryItemInDocument() # JsonApiMemoryItemInDocument | 
    filter = 'title==someString;description==someString;createdBy.id==321;modifiedBy.id==321' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    include = ['createdBy,modifiedBy'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)

    try:
        # Put a Memory Item
        api_response = api_instance.update_entity_memory_items(workspace_id, object_id, json_api_memory_item_in_document, filter=filter, include=include)
        print("The response of MemoryItemControllerApi->update_entity_memory_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemoryItemControllerApi->update_entity_memory_items: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **object_id** | **str**|  | 
 **json_api_memory_item_in_document** | [**JsonApiMemoryItemInDocument**](JsonApiMemoryItemInDocument.md)|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 
 **include** | [**List[str]**](str.md)| Array of included collections or individual relationships. Includes are separated by commas (e.g. include&#x3D;entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \&quot;ALL\&quot; is present, all possible includes are used (include&#x3D;ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. | [optional] 

### Return type

[**JsonApiMemoryItemOutDocument**](JsonApiMemoryItemOutDocument.md)

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

