# gooddata_api_client.UserDataFilterControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_user_data_filters**](UserDataFilterControllerApi.md#create_entity_user_data_filters) | **POST** /api/v1/entities/workspaces/{workspaceId}/userDataFilters | Post User Data Filters
[**delete_entity_user_data_filters**](UserDataFilterControllerApi.md#delete_entity_user_data_filters) | **DELETE** /api/v1/entities/workspaces/{workspaceId}/userDataFilters/{objectId} | Delete a User Data Filter
[**get_all_entities_user_data_filters**](UserDataFilterControllerApi.md#get_all_entities_user_data_filters) | **GET** /api/v1/entities/workspaces/{workspaceId}/userDataFilters | Get all User Data Filters
[**get_entity_user_data_filters**](UserDataFilterControllerApi.md#get_entity_user_data_filters) | **GET** /api/v1/entities/workspaces/{workspaceId}/userDataFilters/{objectId} | Get a User Data Filter
[**patch_entity_user_data_filters**](UserDataFilterControllerApi.md#patch_entity_user_data_filters) | **PATCH** /api/v1/entities/workspaces/{workspaceId}/userDataFilters/{objectId} | Patch a User Data Filter
[**search_entities_user_data_filters**](UserDataFilterControllerApi.md#search_entities_user_data_filters) | **POST** /api/v1/entities/workspaces/{workspaceId}/userDataFilters/search | The search endpoint (beta)
[**update_entity_user_data_filters**](UserDataFilterControllerApi.md#update_entity_user_data_filters) | **PUT** /api/v1/entities/workspaces/{workspaceId}/userDataFilters/{objectId} | Put a User Data Filter


# **create_entity_user_data_filters**
> JsonApiUserDataFilterOutDocument create_entity_user_data_filters(workspace_id, json_api_user_data_filter_post_optional_id_document, include=include, meta_include=meta_include)

Post User Data Filters

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_user_data_filter_out_document import JsonApiUserDataFilterOutDocument
from gooddata_api_client.models.json_api_user_data_filter_post_optional_id_document import JsonApiUserDataFilterPostOptionalIdDocument
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
    api_instance = gooddata_api_client.UserDataFilterControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    json_api_user_data_filter_post_optional_id_document = gooddata_api_client.JsonApiUserDataFilterPostOptionalIdDocument() # JsonApiUserDataFilterPostOptionalIdDocument | 
    include = ['user,userGroup,facts,attributes,labels,metrics,datasets'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)
    meta_include = ['metaInclude=origin,all'] # List[str] | Include Meta objects. (optional)

    try:
        # Post User Data Filters
        api_response = api_instance.create_entity_user_data_filters(workspace_id, json_api_user_data_filter_post_optional_id_document, include=include, meta_include=meta_include)
        print("The response of UserDataFilterControllerApi->create_entity_user_data_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataFilterControllerApi->create_entity_user_data_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **json_api_user_data_filter_post_optional_id_document** | [**JsonApiUserDataFilterPostOptionalIdDocument**](JsonApiUserDataFilterPostOptionalIdDocument.md)|  | 
 **include** | [**List[str]**](str.md)| Array of included collections or individual relationships. Includes are separated by commas (e.g. include&#x3D;entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \&quot;ALL\&quot; is present, all possible includes are used (include&#x3D;ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. | [optional] 
 **meta_include** | [**List[str]**](str.md)| Include Meta objects. | [optional] 

### Return type

[**JsonApiUserDataFilterOutDocument**](JsonApiUserDataFilterOutDocument.md)

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

# **delete_entity_user_data_filters**
> delete_entity_user_data_filters(workspace_id, object_id)

Delete a User Data Filter

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
    api_instance = gooddata_api_client.UserDataFilterControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    object_id = 'object_id_example' # str | 

    try:
        # Delete a User Data Filter
        api_instance.delete_entity_user_data_filters(workspace_id, object_id)
    except Exception as e:
        print("Exception when calling UserDataFilterControllerApi->delete_entity_user_data_filters: %s\n" % e)
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

# **get_all_entities_user_data_filters**
> JsonApiUserDataFilterOutList get_all_entities_user_data_filters(workspace_id, origin=origin, filter=filter, include=include, page=page, size=size, sort=sort, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)

Get all User Data Filters

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_user_data_filter_out_list import JsonApiUserDataFilterOutList
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
    api_instance = gooddata_api_client.UserDataFilterControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    origin = ALL # str |  (optional) (default to ALL)
    filter = 'title==someString;description==someString;user.id==321;userGroup.id==321' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    include = ['user,userGroup,facts,attributes,labels,metrics,datasets'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    x_gdc_validate_relations = False # bool |  (optional) (default to False)
    meta_include = ['metaInclude=origin,page,all'] # List[str] | Include Meta objects. (optional)

    try:
        # Get all User Data Filters
        api_response = api_instance.get_all_entities_user_data_filters(workspace_id, origin=origin, filter=filter, include=include, page=page, size=size, sort=sort, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)
        print("The response of UserDataFilterControllerApi->get_all_entities_user_data_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataFilterControllerApi->get_all_entities_user_data_filters: %s\n" % e)
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

[**JsonApiUserDataFilterOutList**](JsonApiUserDataFilterOutList.md)

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

# **get_entity_user_data_filters**
> JsonApiUserDataFilterOutDocument get_entity_user_data_filters(workspace_id, object_id, filter=filter, include=include, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)

Get a User Data Filter

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_user_data_filter_out_document import JsonApiUserDataFilterOutDocument
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
    api_instance = gooddata_api_client.UserDataFilterControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    object_id = 'object_id_example' # str | 
    filter = 'title==someString;description==someString;user.id==321;userGroup.id==321' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    include = ['user,userGroup,facts,attributes,labels,metrics,datasets'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)
    x_gdc_validate_relations = False # bool |  (optional) (default to False)
    meta_include = ['metaInclude=origin,all'] # List[str] | Include Meta objects. (optional)

    try:
        # Get a User Data Filter
        api_response = api_instance.get_entity_user_data_filters(workspace_id, object_id, filter=filter, include=include, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)
        print("The response of UserDataFilterControllerApi->get_entity_user_data_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataFilterControllerApi->get_entity_user_data_filters: %s\n" % e)
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

[**JsonApiUserDataFilterOutDocument**](JsonApiUserDataFilterOutDocument.md)

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

# **patch_entity_user_data_filters**
> JsonApiUserDataFilterOutDocument patch_entity_user_data_filters(workspace_id, object_id, json_api_user_data_filter_patch_document, filter=filter, include=include)

Patch a User Data Filter

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_user_data_filter_out_document import JsonApiUserDataFilterOutDocument
from gooddata_api_client.models.json_api_user_data_filter_patch_document import JsonApiUserDataFilterPatchDocument
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
    api_instance = gooddata_api_client.UserDataFilterControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    object_id = 'object_id_example' # str | 
    json_api_user_data_filter_patch_document = gooddata_api_client.JsonApiUserDataFilterPatchDocument() # JsonApiUserDataFilterPatchDocument | 
    filter = 'title==someString;description==someString;user.id==321;userGroup.id==321' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    include = ['user,userGroup,facts,attributes,labels,metrics,datasets'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)

    try:
        # Patch a User Data Filter
        api_response = api_instance.patch_entity_user_data_filters(workspace_id, object_id, json_api_user_data_filter_patch_document, filter=filter, include=include)
        print("The response of UserDataFilterControllerApi->patch_entity_user_data_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataFilterControllerApi->patch_entity_user_data_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **object_id** | **str**|  | 
 **json_api_user_data_filter_patch_document** | [**JsonApiUserDataFilterPatchDocument**](JsonApiUserDataFilterPatchDocument.md)|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 
 **include** | [**List[str]**](str.md)| Array of included collections or individual relationships. Includes are separated by commas (e.g. include&#x3D;entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \&quot;ALL\&quot; is present, all possible includes are used (include&#x3D;ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. | [optional] 

### Return type

[**JsonApiUserDataFilterOutDocument**](JsonApiUserDataFilterOutDocument.md)

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

# **search_entities_user_data_filters**
> JsonApiUserDataFilterOutList search_entities_user_data_filters(workspace_id, entity_search_body, origin=origin, x_gdc_validate_relations=x_gdc_validate_relations)

The search endpoint (beta)

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.entity_search_body import EntitySearchBody
from gooddata_api_client.models.json_api_user_data_filter_out_list import JsonApiUserDataFilterOutList
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
    api_instance = gooddata_api_client.UserDataFilterControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    entity_search_body = gooddata_api_client.EntitySearchBody() # EntitySearchBody | Search request body with filter, pagination, and sorting options
    origin = ALL # str |  (optional) (default to ALL)
    x_gdc_validate_relations = False # bool |  (optional) (default to False)

    try:
        # The search endpoint (beta)
        api_response = api_instance.search_entities_user_data_filters(workspace_id, entity_search_body, origin=origin, x_gdc_validate_relations=x_gdc_validate_relations)
        print("The response of UserDataFilterControllerApi->search_entities_user_data_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataFilterControllerApi->search_entities_user_data_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **entity_search_body** | [**EntitySearchBody**](EntitySearchBody.md)| Search request body with filter, pagination, and sorting options | 
 **origin** | **str**|  | [optional] [default to ALL]
 **x_gdc_validate_relations** | **bool**|  | [optional] [default to False]

### Return type

[**JsonApiUserDataFilterOutList**](JsonApiUserDataFilterOutList.md)

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

# **update_entity_user_data_filters**
> JsonApiUserDataFilterOutDocument update_entity_user_data_filters(workspace_id, object_id, json_api_user_data_filter_in_document, filter=filter, include=include)

Put a User Data Filter

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_user_data_filter_in_document import JsonApiUserDataFilterInDocument
from gooddata_api_client.models.json_api_user_data_filter_out_document import JsonApiUserDataFilterOutDocument
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
    api_instance = gooddata_api_client.UserDataFilterControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    object_id = 'object_id_example' # str | 
    json_api_user_data_filter_in_document = gooddata_api_client.JsonApiUserDataFilterInDocument() # JsonApiUserDataFilterInDocument | 
    filter = 'title==someString;description==someString;user.id==321;userGroup.id==321' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    include = ['user,userGroup,facts,attributes,labels,metrics,datasets'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)

    try:
        # Put a User Data Filter
        api_response = api_instance.update_entity_user_data_filters(workspace_id, object_id, json_api_user_data_filter_in_document, filter=filter, include=include)
        print("The response of UserDataFilterControllerApi->update_entity_user_data_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataFilterControllerApi->update_entity_user_data_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **object_id** | **str**|  | 
 **json_api_user_data_filter_in_document** | [**JsonApiUserDataFilterInDocument**](JsonApiUserDataFilterInDocument.md)|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 
 **include** | [**List[str]**](str.md)| Array of included collections or individual relationships. Includes are separated by commas (e.g. include&#x3D;entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \&quot;ALL\&quot; is present, all possible includes are used (include&#x3D;ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. | [optional] 

### Return type

[**JsonApiUserDataFilterOutDocument**](JsonApiUserDataFilterOutDocument.md)

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

