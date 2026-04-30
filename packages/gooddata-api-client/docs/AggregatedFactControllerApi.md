# gooddata_api_client.AggregatedFactControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_entities_aggregated_facts**](AggregatedFactControllerApi.md#get_all_entities_aggregated_facts) | **GET** /api/v1/entities/workspaces/{workspaceId}/aggregatedFacts | Get all Aggregated Facts
[**get_entity_aggregated_facts**](AggregatedFactControllerApi.md#get_entity_aggregated_facts) | **GET** /api/v1/entities/workspaces/{workspaceId}/aggregatedFacts/{objectId} | Get an Aggregated Fact
[**search_entities_aggregated_facts**](AggregatedFactControllerApi.md#search_entities_aggregated_facts) | **POST** /api/v1/entities/workspaces/{workspaceId}/aggregatedFacts/search | The search endpoint (beta)


# **get_all_entities_aggregated_facts**
> JsonApiAggregatedFactOutList get_all_entities_aggregated_facts(workspace_id, origin=origin, filter=filter, include=include, page=page, size=size, sort=sort, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)

Get all Aggregated Facts

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_aggregated_fact_out_list import JsonApiAggregatedFactOutList
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
    api_instance = gooddata_api_client.AggregatedFactControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    origin = ALL # str |  (optional) (default to ALL)
    filter = 'description==someString;tags==v1,v2,v3;dataset.id==321;sourceFact.id==321' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    include = ['dataset,sourceFact'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    x_gdc_validate_relations = False # bool |  (optional) (default to False)
    meta_include = ['metaInclude=origin,page,all'] # List[str] | Include Meta objects. (optional)

    try:
        # Get all Aggregated Facts
        api_response = api_instance.get_all_entities_aggregated_facts(workspace_id, origin=origin, filter=filter, include=include, page=page, size=size, sort=sort, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)
        print("The response of AggregatedFactControllerApi->get_all_entities_aggregated_facts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AggregatedFactControllerApi->get_all_entities_aggregated_facts: %s\n" % e)
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

[**JsonApiAggregatedFactOutList**](JsonApiAggregatedFactOutList.md)

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

# **get_entity_aggregated_facts**
> JsonApiAggregatedFactOutDocument get_entity_aggregated_facts(workspace_id, object_id, filter=filter, include=include, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)

Get an Aggregated Fact

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_aggregated_fact_out_document import JsonApiAggregatedFactOutDocument
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
    api_instance = gooddata_api_client.AggregatedFactControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    object_id = 'object_id_example' # str | 
    filter = 'description==someString;tags==v1,v2,v3;dataset.id==321;sourceFact.id==321' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    include = ['dataset,sourceFact'] # List[str] | Array of included collections or individual relationships. Includes are separated by commas (e.g. include=entity1s,entity2s). Collection include represents the inclusion of every relationship between this entity and the given collection. Relationship include represents the inclusion of the particular relationships only. If single parameter \"ALL\" is present, all possible includes are used (include=ALL).  __WARNING:__ Individual include types (collection, relationship or ALL) cannot be combined together. (optional)
    x_gdc_validate_relations = False # bool |  (optional) (default to False)
    meta_include = ['metaInclude=origin,all'] # List[str] | Include Meta objects. (optional)

    try:
        # Get an Aggregated Fact
        api_response = api_instance.get_entity_aggregated_facts(workspace_id, object_id, filter=filter, include=include, x_gdc_validate_relations=x_gdc_validate_relations, meta_include=meta_include)
        print("The response of AggregatedFactControllerApi->get_entity_aggregated_facts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AggregatedFactControllerApi->get_entity_aggregated_facts: %s\n" % e)
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

[**JsonApiAggregatedFactOutDocument**](JsonApiAggregatedFactOutDocument.md)

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

# **search_entities_aggregated_facts**
> JsonApiAggregatedFactOutList search_entities_aggregated_facts(workspace_id, entity_search_body, origin=origin, x_gdc_validate_relations=x_gdc_validate_relations)

The search endpoint (beta)

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.entity_search_body import EntitySearchBody
from gooddata_api_client.models.json_api_aggregated_fact_out_list import JsonApiAggregatedFactOutList
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
    api_instance = gooddata_api_client.AggregatedFactControllerApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    entity_search_body = gooddata_api_client.EntitySearchBody() # EntitySearchBody | Search request body with filter, pagination, and sorting options
    origin = ALL # str |  (optional) (default to ALL)
    x_gdc_validate_relations = False # bool |  (optional) (default to False)

    try:
        # The search endpoint (beta)
        api_response = api_instance.search_entities_aggregated_facts(workspace_id, entity_search_body, origin=origin, x_gdc_validate_relations=x_gdc_validate_relations)
        print("The response of AggregatedFactControllerApi->search_entities_aggregated_facts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AggregatedFactControllerApi->search_entities_aggregated_facts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **entity_search_body** | [**EntitySearchBody**](EntitySearchBody.md)| Search request body with filter, pagination, and sorting options | 
 **origin** | **str**|  | [optional] [default to ALL]
 **x_gdc_validate_relations** | **bool**|  | [optional] [default to False]

### Return type

[**JsonApiAggregatedFactOutList**](JsonApiAggregatedFactOutList.md)

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

