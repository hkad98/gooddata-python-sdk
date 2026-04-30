# gooddata_api_client.AILakeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deprovision_ai_lake_database_instance**](AILakeApi.md#deprovision_ai_lake_database_instance) | **DELETE** /api/v1/ailake/database/instances/{instanceId} | (BETA) Delete an existing AILake Database instance
[**get_ai_lake_database_instance**](AILakeApi.md#get_ai_lake_database_instance) | **GET** /api/v1/ailake/database/instances/{instanceId} | (BETA) Get the specified AILake Database instance
[**get_ai_lake_operation**](AILakeApi.md#get_ai_lake_operation) | **GET** /api/v1/ailake/operations/{operationId} | (BETA) Get Long Running Operation details
[**get_ai_lake_service_status**](AILakeApi.md#get_ai_lake_service_status) | **GET** /api/v1/ailake/services/{serviceId}/status | (BETA) Get AI Lake service status
[**list_ai_lake_database_instances**](AILakeApi.md#list_ai_lake_database_instances) | **GET** /api/v1/ailake/database/instances | (BETA) List AI Lake Database instances
[**list_ai_lake_services**](AILakeApi.md#list_ai_lake_services) | **GET** /api/v1/ailake/services | (BETA) List AI Lake services
[**provision_ai_lake_database_instance**](AILakeApi.md#provision_ai_lake_database_instance) | **POST** /api/v1/ailake/database/instances | (BETA) Create a new AILake Database instance
[**run_ai_lake_service_command**](AILakeApi.md#run_ai_lake_service_command) | **POST** /api/v1/ailake/services/{serviceId}/commands/{commandName}/run | (BETA) Run an AI Lake services command


# **deprovision_ai_lake_database_instance**
> object deprovision_ai_lake_database_instance(instance_id, operation_id=operation_id)

(BETA) Delete an existing AILake Database instance

(BETA) Deletes an existing database in the organization's AI Lake. Returns an operation-id in the operation-id header the client can use to poll for the progress.

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
    api_instance = gooddata_api_client.AILakeApi(api_client)
    instance_id = 'instance_id_example' # str | Database instance identifier. Accepts the database name (preferred) or UUID.
    operation_id = 'operation_id_example' # str |  (optional)

    try:
        # (BETA) Delete an existing AILake Database instance
        api_response = api_instance.deprovision_ai_lake_database_instance(instance_id, operation_id=operation_id)
        print("The response of AILakeApi->deprovision_ai_lake_database_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AILakeApi->deprovision_ai_lake_database_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Database instance identifier. Accepts the database name (preferred) or UUID. | 
 **operation_id** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  * operation-id - Operation ID to use for polling. <br>  * operation-location - Operation location URL that can be used for polling. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_lake_database_instance**
> DatabaseInstance get_ai_lake_database_instance(instance_id)

(BETA) Get the specified AILake Database instance

(BETA) Retrieve details of the specified AI Lake database instance in the organization's AI Lake.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.database_instance import DatabaseInstance
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
    api_instance = gooddata_api_client.AILakeApi(api_client)
    instance_id = 'instance_id_example' # str | Database instance identifier. Accepts the database name (preferred) or UUID.

    try:
        # (BETA) Get the specified AILake Database instance
        api_response = api_instance.get_ai_lake_database_instance(instance_id)
        print("The response of AILakeApi->get_ai_lake_database_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AILakeApi->get_ai_lake_database_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Database instance identifier. Accepts the database name (preferred) or UUID. | 

### Return type

[**DatabaseInstance**](DatabaseInstance.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI Lake database instance successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_lake_operation**
> GetAiLakeOperation200Response get_ai_lake_operation(operation_id)

(BETA) Get Long Running Operation details

(BETA) Retrieves details of a Long Running Operation specified by the operation-id.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.get_ai_lake_operation200_response import GetAiLakeOperation200Response
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
    api_instance = gooddata_api_client.AILakeApi(api_client)
    operation_id = 'e9fd5d74-8a1b-46bd-ac60-bd91e9206897' # str | Operation ID

    try:
        # (BETA) Get Long Running Operation details
        api_response = api_instance.get_ai_lake_operation(operation_id)
        print("The response of AILakeApi->get_ai_lake_operation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AILakeApi->get_ai_lake_operation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operation_id** | **str**| Operation ID | 

### Return type

[**GetAiLakeOperation200Response**](GetAiLakeOperation200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI Lake Long Running Operation details successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_lake_service_status**
> GetServiceStatusResponse get_ai_lake_service_status(service_id)

(BETA) Get AI Lake service status

(BETA) Returns the status of a service in the organization's AI Lake. The status is controller-specific (e.g., available commands, readiness).

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.get_service_status_response import GetServiceStatusResponse
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
    api_instance = gooddata_api_client.AILakeApi(api_client)
    service_id = 'service_id_example' # str | 

    try:
        # (BETA) Get AI Lake service status
        api_response = api_instance.get_ai_lake_service_status(service_id)
        print("The response of AILakeApi->get_ai_lake_service_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AILakeApi->get_ai_lake_service_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 

### Return type

[**GetServiceStatusResponse**](GetServiceStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI Lake service status successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ai_lake_database_instances**
> ListDatabaseInstancesResponse list_ai_lake_database_instances(size=size, offset=offset, meta_include=meta_include)

(BETA) List AI Lake Database instances

(BETA) Lists database instances in the organization's AI Lake. Supports paging via size and offset query parameters. Use metaInclude=page to get total count.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.list_database_instances_response import ListDatabaseInstancesResponse
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
    api_instance = gooddata_api_client.AILakeApi(api_client)
    size = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    meta_include = ['meta_include_example'] # List[str] |  (optional)

    try:
        # (BETA) List AI Lake Database instances
        api_response = api_instance.list_ai_lake_database_instances(size=size, offset=offset, meta_include=meta_include)
        print("The response of AILakeApi->list_ai_lake_database_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AILakeApi->list_ai_lake_database_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **meta_include** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ListDatabaseInstancesResponse**](ListDatabaseInstancesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI Lake database instances successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_ai_lake_services**
> ListServicesResponse list_ai_lake_services(size=size, offset=offset, meta_include=meta_include)

(BETA) List AI Lake services

(BETA) Lists services configured for the organization's AI Lake. Returns only non-sensitive fields (id, name). Supports paging via size and offset query parameters. Use metaInclude=page to get total count.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.list_services_response import ListServicesResponse
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
    api_instance = gooddata_api_client.AILakeApi(api_client)
    size = 50 # int |  (optional) (default to 50)
    offset = 0 # int |  (optional) (default to 0)
    meta_include = ['meta_include_example'] # List[str] |  (optional)

    try:
        # (BETA) List AI Lake services
        api_response = api_instance.list_ai_lake_services(size=size, offset=offset, meta_include=meta_include)
        print("The response of AILakeApi->list_ai_lake_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AILakeApi->list_ai_lake_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **size** | **int**|  | [optional] [default to 50]
 **offset** | **int**|  | [optional] [default to 0]
 **meta_include** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**ListServicesResponse**](ListServicesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | AI Lake services successfully retrieved |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **provision_ai_lake_database_instance**
> object provision_ai_lake_database_instance(provision_database_instance_request, operation_id=operation_id)

(BETA) Create a new AILake Database instance

(BETA) Creates a new database in the organization's AI Lake. Returns an operation-id in the operation-id header the client can use to poll for the progress.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.provision_database_instance_request import ProvisionDatabaseInstanceRequest
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
    api_instance = gooddata_api_client.AILakeApi(api_client)
    provision_database_instance_request = gooddata_api_client.ProvisionDatabaseInstanceRequest() # ProvisionDatabaseInstanceRequest | 
    operation_id = 'operation_id_example' # str |  (optional)

    try:
        # (BETA) Create a new AILake Database instance
        api_response = api_instance.provision_ai_lake_database_instance(provision_database_instance_request, operation_id=operation_id)
        print("The response of AILakeApi->provision_ai_lake_database_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AILakeApi->provision_ai_lake_database_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provision_database_instance_request** | [**ProvisionDatabaseInstanceRequest**](ProvisionDatabaseInstanceRequest.md)|  | 
 **operation_id** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  * operation-id - Operation ID to use for polling. <br>  * operation-location - Operation location URL that can be used for polling. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_ai_lake_service_command**
> object run_ai_lake_service_command(service_id, command_name, run_service_command_request, operation_id=operation_id)

(BETA) Run an AI Lake services command

(BETA) Runs a specific AI Lake service command.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.run_service_command_request import RunServiceCommandRequest
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
    api_instance = gooddata_api_client.AILakeApi(api_client)
    service_id = 'service_id_example' # str | 
    command_name = 'command_name_example' # str | 
    run_service_command_request = gooddata_api_client.RunServiceCommandRequest() # RunServiceCommandRequest | 
    operation_id = 'operation_id_example' # str |  (optional)

    try:
        # (BETA) Run an AI Lake services command
        api_response = api_instance.run_ai_lake_service_command(service_id, command_name, run_service_command_request, operation_id=operation_id)
        print("The response of AILakeApi->run_ai_lake_service_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AILakeApi->run_ai_lake_service_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  | 
 **command_name** | **str**|  | 
 **run_service_command_request** | [**RunServiceCommandRequest**](RunServiceCommandRequest.md)|  | 
 **operation_id** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  * operation-id - Operation ID to use for polling. <br>  * operation-location - Operation location URL that can be used for polling. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

