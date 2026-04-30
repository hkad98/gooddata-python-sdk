# gooddata_api_client.NotificationChannelControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_entity_notification_channels**](NotificationChannelControllerApi.md#create_entity_notification_channels) | **POST** /api/v1/entities/notificationChannels | Post Notification Channel entities
[**delete_entity_notification_channels**](NotificationChannelControllerApi.md#delete_entity_notification_channels) | **DELETE** /api/v1/entities/notificationChannels/{id} | Delete Notification Channel entity
[**get_all_entities_notification_channels**](NotificationChannelControllerApi.md#get_all_entities_notification_channels) | **GET** /api/v1/entities/notificationChannels | Get all Notification Channel entities
[**get_entity_notification_channels**](NotificationChannelControllerApi.md#get_entity_notification_channels) | **GET** /api/v1/entities/notificationChannels/{id} | Get Notification Channel entity
[**patch_entity_notification_channels**](NotificationChannelControllerApi.md#patch_entity_notification_channels) | **PATCH** /api/v1/entities/notificationChannels/{id} | Patch Notification Channel entity
[**update_entity_notification_channels**](NotificationChannelControllerApi.md#update_entity_notification_channels) | **PUT** /api/v1/entities/notificationChannels/{id} | Put Notification Channel entity


# **create_entity_notification_channels**
> JsonApiNotificationChannelOutDocument create_entity_notification_channels(json_api_notification_channel_post_optional_id_document)

Post Notification Channel entities

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_notification_channel_out_document import JsonApiNotificationChannelOutDocument
from gooddata_api_client.models.json_api_notification_channel_post_optional_id_document import JsonApiNotificationChannelPostOptionalIdDocument
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
    api_instance = gooddata_api_client.NotificationChannelControllerApi(api_client)
    json_api_notification_channel_post_optional_id_document = gooddata_api_client.JsonApiNotificationChannelPostOptionalIdDocument() # JsonApiNotificationChannelPostOptionalIdDocument | 

    try:
        # Post Notification Channel entities
        api_response = api_instance.create_entity_notification_channels(json_api_notification_channel_post_optional_id_document)
        print("The response of NotificationChannelControllerApi->create_entity_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationChannelControllerApi->create_entity_notification_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_api_notification_channel_post_optional_id_document** | [**JsonApiNotificationChannelPostOptionalIdDocument**](JsonApiNotificationChannelPostOptionalIdDocument.md)|  | 

### Return type

[**JsonApiNotificationChannelOutDocument**](JsonApiNotificationChannelOutDocument.md)

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

# **delete_entity_notification_channels**
> delete_entity_notification_channels(id)

Delete Notification Channel entity

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
    api_instance = gooddata_api_client.NotificationChannelControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete Notification Channel entity
        api_instance.delete_entity_notification_channels(id)
    except Exception as e:
        print("Exception when calling NotificationChannelControllerApi->delete_entity_notification_channels: %s\n" % e)
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

# **get_all_entities_notification_channels**
> JsonApiNotificationChannelOutList get_all_entities_notification_channels(filter=filter, page=page, size=size, sort=sort, meta_include=meta_include)

Get all Notification Channel entities

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_notification_channel_out_list import JsonApiNotificationChannelOutList
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
    api_instance = gooddata_api_client.NotificationChannelControllerApi(api_client)
    filter = 'name==someString;description==someString' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)
    page = 0 # int | Zero-based page index (0..N) (optional) (default to 0)
    size = 20 # int | The size of the page to be returned (optional) (default to 20)
    sort = ['sort_example'] # List[str] | Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported. (optional)
    meta_include = ['metaInclude=page,all'] # List[str] | Include Meta objects. (optional)

    try:
        # Get all Notification Channel entities
        api_response = api_instance.get_all_entities_notification_channels(filter=filter, page=page, size=size, sort=sort, meta_include=meta_include)
        print("The response of NotificationChannelControllerApi->get_all_entities_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationChannelControllerApi->get_all_entities_notification_channels: %s\n" % e)
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

[**JsonApiNotificationChannelOutList**](JsonApiNotificationChannelOutList.md)

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

# **get_entity_notification_channels**
> JsonApiNotificationChannelOutDocument get_entity_notification_channels(id, filter=filter)

Get Notification Channel entity

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_notification_channel_out_document import JsonApiNotificationChannelOutDocument
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
    api_instance = gooddata_api_client.NotificationChannelControllerApi(api_client)
    id = 'id_example' # str | 
    filter = 'name==someString;description==someString' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)

    try:
        # Get Notification Channel entity
        api_response = api_instance.get_entity_notification_channels(id, filter=filter)
        print("The response of NotificationChannelControllerApi->get_entity_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationChannelControllerApi->get_entity_notification_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 

### Return type

[**JsonApiNotificationChannelOutDocument**](JsonApiNotificationChannelOutDocument.md)

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

# **patch_entity_notification_channels**
> JsonApiNotificationChannelOutDocument patch_entity_notification_channels(id, json_api_notification_channel_patch_document, filter=filter)

Patch Notification Channel entity

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_notification_channel_out_document import JsonApiNotificationChannelOutDocument
from gooddata_api_client.models.json_api_notification_channel_patch_document import JsonApiNotificationChannelPatchDocument
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
    api_instance = gooddata_api_client.NotificationChannelControllerApi(api_client)
    id = 'id_example' # str | 
    json_api_notification_channel_patch_document = gooddata_api_client.JsonApiNotificationChannelPatchDocument() # JsonApiNotificationChannelPatchDocument | 
    filter = 'name==someString;description==someString' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)

    try:
        # Patch Notification Channel entity
        api_response = api_instance.patch_entity_notification_channels(id, json_api_notification_channel_patch_document, filter=filter)
        print("The response of NotificationChannelControllerApi->patch_entity_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationChannelControllerApi->patch_entity_notification_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **json_api_notification_channel_patch_document** | [**JsonApiNotificationChannelPatchDocument**](JsonApiNotificationChannelPatchDocument.md)|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 

### Return type

[**JsonApiNotificationChannelOutDocument**](JsonApiNotificationChannelOutDocument.md)

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

# **update_entity_notification_channels**
> JsonApiNotificationChannelOutDocument update_entity_notification_channels(id, json_api_notification_channel_in_document, filter=filter)

Put Notification Channel entity

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.json_api_notification_channel_in_document import JsonApiNotificationChannelInDocument
from gooddata_api_client.models.json_api_notification_channel_out_document import JsonApiNotificationChannelOutDocument
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
    api_instance = gooddata_api_client.NotificationChannelControllerApi(api_client)
    id = 'id_example' # str | 
    json_api_notification_channel_in_document = gooddata_api_client.JsonApiNotificationChannelInDocument() # JsonApiNotificationChannelInDocument | 
    filter = 'name==someString;description==someString' # str | Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title=='Some Title';description=='desc'). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty=='Value 123'). (optional)

    try:
        # Put Notification Channel entity
        api_response = api_instance.update_entity_notification_channels(id, json_api_notification_channel_in_document, filter=filter)
        print("The response of NotificationChannelControllerApi->update_entity_notification_channels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationChannelControllerApi->update_entity_notification_channels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **json_api_notification_channel_in_document** | [**JsonApiNotificationChannelInDocument**](JsonApiNotificationChannelInDocument.md)|  | 
 **filter** | **str**| Filtering parameter in RSQL. See https://github.com/jirutka/rsql-parser. You can specify any object parameter and parameter of related entity (for example title&#x3D;&#x3D;&#39;Some Title&#39;;description&#x3D;&#x3D;&#39;desc&#39;). Additionally, if the entity relationship represents a polymorphic entity type, it can be casted to its subtypes (for example relatedEntity::subtype.subtypeProperty&#x3D;&#x3D;&#39;Value 123&#39;). | [optional] 

### Return type

[**JsonApiNotificationChannelOutDocument**](JsonApiNotificationChannelOutDocument.md)

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

