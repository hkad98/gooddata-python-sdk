# gooddata_api_client.SmartFunctionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_chat**](SmartFunctionsApi.md#ai_chat) | **POST** /api/v1/actions/workspaces/{workspaceId}/ai/chat | (BETA) Chat with AI
[**ai_chat_history**](SmartFunctionsApi.md#ai_chat_history) | **POST** /api/v1/actions/workspaces/{workspaceId}/ai/chatHistory | (BETA) Get Chat History
[**ai_chat_stream**](SmartFunctionsApi.md#ai_chat_stream) | **POST** /api/v1/actions/workspaces/{workspaceId}/ai/chatStream | (BETA) Chat with AI
[**ai_chat_usage**](SmartFunctionsApi.md#ai_chat_usage) | **GET** /api/v1/actions/workspaces/{workspaceId}/ai/chatUsage | Get Chat Usage
[**ai_search**](SmartFunctionsApi.md#ai_search) | **POST** /api/v1/actions/workspaces/{workspaceId}/ai/search | (BETA) Semantic Search in Metadata
[**anomaly_detection**](SmartFunctionsApi.md#anomaly_detection) | **POST** /api/v1/actions/workspaces/{workspaceId}/execution/functions/anomalyDetection/{resultId} | (EXPERIMENTAL) Smart functions - Anomaly Detection
[**anomaly_detection_result**](SmartFunctionsApi.md#anomaly_detection_result) | **GET** /api/v1/actions/workspaces/{workspaceId}/execution/functions/anomalyDetection/result/{resultId} | (EXPERIMENTAL) Smart functions - Anomaly Detection Result
[**clustering**](SmartFunctionsApi.md#clustering) | **POST** /api/v1/actions/workspaces/{workspaceId}/execution/functions/clustering/{resultId} | (EXPERIMENTAL) Smart functions - Clustering
[**clustering_result**](SmartFunctionsApi.md#clustering_result) | **GET** /api/v1/actions/workspaces/{workspaceId}/execution/functions/clustering/result/{resultId} | (EXPERIMENTAL) Smart functions - Clustering Result
[**created_by**](SmartFunctionsApi.md#created_by) | **GET** /api/v1/actions/workspaces/{workspaceId}/ai/analyticsCatalog/createdBy | Get Analytics Catalog CreatedBy Users
[**forecast**](SmartFunctionsApi.md#forecast) | **POST** /api/v1/actions/workspaces/{workspaceId}/execution/functions/forecast/{resultId} | (BETA) Smart functions - Forecast
[**forecast_result**](SmartFunctionsApi.md#forecast_result) | **GET** /api/v1/actions/workspaces/{workspaceId}/execution/functions/forecast/result/{resultId} | (BETA) Smart functions - Forecast Result
[**generate_description**](SmartFunctionsApi.md#generate_description) | **POST** /api/v1/actions/workspaces/{workspaceId}/ai/analyticsCatalog/generateDescription | Generate Description for Analytics Object
[**generate_title**](SmartFunctionsApi.md#generate_title) | **POST** /api/v1/actions/workspaces/{workspaceId}/ai/analyticsCatalog/generateTitle | Generate Title for Analytics Object
[**get_quality_issues**](SmartFunctionsApi.md#get_quality_issues) | **GET** /api/v1/actions/workspaces/{workspaceId}/ai/issues | Get Quality Issues
[**get_quality_issues_calculation_status**](SmartFunctionsApi.md#get_quality_issues_calculation_status) | **GET** /api/v1/actions/workspaces/{workspaceId}/ai/issues/status/{processId} | Get Quality Issues Calculation Status
[**list_llm_provider_models**](SmartFunctionsApi.md#list_llm_provider_models) | **POST** /api/v1/actions/ai/llmProvider/listModels | List LLM Provider Models
[**list_llm_provider_models_by_id**](SmartFunctionsApi.md#list_llm_provider_models_by_id) | **POST** /api/v1/actions/ai/llmProvider/{llmProviderId}/listModels | List LLM Provider Models By Id
[**memory_created_by_users**](SmartFunctionsApi.md#memory_created_by_users) | **GET** /api/v1/actions/workspaces/{workspaceId}/ai/memory/createdBy | Get AI Memory CreatedBy Users
[**resolve_llm_endpoints**](SmartFunctionsApi.md#resolve_llm_endpoints) | **GET** /api/v1/actions/workspaces/{workspaceId}/ai/resolveLlmEndpoints | Get Active LLM Endpoints for this workspace
[**resolve_llm_providers**](SmartFunctionsApi.md#resolve_llm_providers) | **GET** /api/v1/actions/workspaces/{workspaceId}/ai/resolveLlmProviders | Get Active LLM configuration for this workspace
[**tags**](SmartFunctionsApi.md#tags) | **GET** /api/v1/actions/workspaces/{workspaceId}/ai/analyticsCatalog/tags | Get Analytics Catalog Tags
[**test_llm_provider**](SmartFunctionsApi.md#test_llm_provider) | **POST** /api/v1/actions/ai/llmProvider/test | Test LLM Provider
[**test_llm_provider_by_id**](SmartFunctionsApi.md#test_llm_provider_by_id) | **POST** /api/v1/actions/ai/llmProvider/{llmProviderId}/test | Test LLM Provider By Id
[**trending_objects**](SmartFunctionsApi.md#trending_objects) | **GET** /api/v1/actions/workspaces/{workspaceId}/ai/analyticsCatalog/trendingObjects | Get Trending Analytics Catalog Objects
[**trigger_quality_issues_calculation**](SmartFunctionsApi.md#trigger_quality_issues_calculation) | **POST** /api/v1/actions/workspaces/{workspaceId}/ai/issues/triggerCheck | Trigger Quality Issues Calculation
[**validate_llm_endpoint**](SmartFunctionsApi.md#validate_llm_endpoint) | **POST** /api/v1/actions/ai/llmEndpoint/test | Validate LLM Endpoint
[**validate_llm_endpoint_by_id**](SmartFunctionsApi.md#validate_llm_endpoint_by_id) | **POST** /api/v1/actions/ai/llmEndpoint/{llmEndpointId}/test | Validate LLM Endpoint By Id


# **ai_chat**
> ChatResult ai_chat(workspace_id, chat_request)

(BETA) Chat with AI

(BETA) Combines multiple use cases such as search, create visualizations, ...

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.chat_request import ChatRequest
from gooddata_api_client.models.chat_result import ChatResult
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    chat_request = gooddata_api_client.ChatRequest() # ChatRequest | 

    try:
        # (BETA) Chat with AI
        api_response = api_instance.ai_chat(workspace_id, chat_request)
        print("The response of SmartFunctionsApi->ai_chat:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->ai_chat: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **chat_request** | [**ChatRequest**](ChatRequest.md)|  | 

### Return type

[**ChatResult**](ChatResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_chat_history**
> ChatHistoryResult ai_chat_history(workspace_id, chat_history_request)

(BETA) Get Chat History

(BETA) Post thread ID (and optionally interaction ID) to get full/partial chat history.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.chat_history_request import ChatHistoryRequest
from gooddata_api_client.models.chat_history_result import ChatHistoryResult
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    chat_history_request = gooddata_api_client.ChatHistoryRequest() # ChatHistoryRequest | 

    try:
        # (BETA) Get Chat History
        api_response = api_instance.ai_chat_history(workspace_id, chat_history_request)
        print("The response of SmartFunctionsApi->ai_chat_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->ai_chat_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **chat_history_request** | [**ChatHistoryRequest**](ChatHistoryRequest.md)|  | 

### Return type

[**ChatHistoryResult**](ChatHistoryResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_chat_stream**
> List[object] ai_chat_stream(workspace_id, chat_request)

(BETA) Chat with AI

(BETA) Combines multiple use cases such as search, create visualizations, ...

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.chat_request import ChatRequest
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    chat_request = gooddata_api_client.ChatRequest() # ChatRequest | 

    try:
        # (BETA) Chat with AI
        api_response = api_instance.ai_chat_stream(workspace_id, chat_request)
        print("The response of SmartFunctionsApi->ai_chat_stream:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->ai_chat_stream: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **chat_request** | [**ChatRequest**](ChatRequest.md)|  | 

### Return type

**List[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_chat_usage**
> ChatUsageResponse ai_chat_usage(workspace_id)

Get Chat Usage

Returns usage statistics of chat for a user in a workspace.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.chat_usage_response import ChatUsageResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier

    try:
        # Get Chat Usage
        api_response = api_instance.ai_chat_usage(workspace_id)
        print("The response of SmartFunctionsApi->ai_chat_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->ai_chat_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 

### Return type

[**ChatUsageResponse**](ChatUsageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_search**
> SearchResult ai_search(workspace_id, search_request)

(BETA) Semantic Search in Metadata

(BETA) Uses similarity (e.g. cosine distance) search to find top X most similar metadata objects.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.search_request import SearchRequest
from gooddata_api_client.models.search_result import SearchResult
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    search_request = gooddata_api_client.SearchRequest() # SearchRequest | 

    try:
        # (BETA) Semantic Search in Metadata
        api_response = api_instance.ai_search(workspace_id, search_request)
        print("The response of SmartFunctionsApi->ai_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->ai_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **search_request** | [**SearchRequest**](SearchRequest.md)|  | 

### Return type

[**SearchResult**](SearchResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anomaly_detection**
> SmartFunctionResponse anomaly_detection(workspace_id, result_id, anomaly_detection_request, skip_cache=skip_cache)

(EXPERIMENTAL) Smart functions - Anomaly Detection

(EXPERIMENTAL) Computes anomaly detection.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.anomaly_detection_request import AnomalyDetectionRequest
from gooddata_api_client.models.smart_function_response import SmartFunctionResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    result_id = '9bd52018570364264fcf62d373da6bed313120e8' # str | Input result ID to be used in the computation
    anomaly_detection_request = gooddata_api_client.AnomalyDetectionRequest() # AnomalyDetectionRequest | 
    skip_cache = False # bool | Ignore all caches during execution of current request. (optional) (default to False)

    try:
        # (EXPERIMENTAL) Smart functions - Anomaly Detection
        api_response = api_instance.anomaly_detection(workspace_id, result_id, anomaly_detection_request, skip_cache=skip_cache)
        print("The response of SmartFunctionsApi->anomaly_detection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->anomaly_detection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **result_id** | **str**| Input result ID to be used in the computation | 
 **anomaly_detection_request** | [**AnomalyDetectionRequest**](AnomalyDetectionRequest.md)|  | 
 **skip_cache** | **bool**| Ignore all caches during execution of current request. | [optional] [default to False]

### Return type

[**SmartFunctionResponse**](SmartFunctionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **anomaly_detection_result**
> AnomalyDetectionResult anomaly_detection_result(workspace_id, result_id, offset=offset, limit=limit)

(EXPERIMENTAL) Smart functions - Anomaly Detection Result

(EXPERIMENTAL) Gets anomalies.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.anomaly_detection_result import AnomalyDetectionResult
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    result_id = 'a9b28f9dc55f37ea9f4a5fb0c76895923591e781' # str | Result ID
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # (EXPERIMENTAL) Smart functions - Anomaly Detection Result
        api_response = api_instance.anomaly_detection_result(workspace_id, result_id, offset=offset, limit=limit)
        print("The response of SmartFunctionsApi->anomaly_detection_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->anomaly_detection_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **result_id** | **str**| Result ID | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**AnomalyDetectionResult**](AnomalyDetectionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clustering**
> SmartFunctionResponse clustering(workspace_id, result_id, clustering_request, skip_cache=skip_cache)

(EXPERIMENTAL) Smart functions - Clustering

(EXPERIMENTAL) Computes clusters for data points from the provided execution result and parameters.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.clustering_request import ClusteringRequest
from gooddata_api_client.models.smart_function_response import SmartFunctionResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    result_id = '9bd52018570364264fcf62d373da6bed313120e8' # str | Input result ID to be used in the computation
    clustering_request = gooddata_api_client.ClusteringRequest() # ClusteringRequest | 
    skip_cache = False # bool | Ignore all caches during execution of current request. (optional) (default to False)

    try:
        # (EXPERIMENTAL) Smart functions - Clustering
        api_response = api_instance.clustering(workspace_id, result_id, clustering_request, skip_cache=skip_cache)
        print("The response of SmartFunctionsApi->clustering:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->clustering: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **result_id** | **str**| Input result ID to be used in the computation | 
 **clustering_request** | [**ClusteringRequest**](ClusteringRequest.md)|  | 
 **skip_cache** | **bool**| Ignore all caches during execution of current request. | [optional] [default to False]

### Return type

[**SmartFunctionResponse**](SmartFunctionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clustering_result**
> ClusteringResult clustering_result(workspace_id, result_id, offset=offset, limit=limit)

(EXPERIMENTAL) Smart functions - Clustering Result

(EXPERIMENTAL) Gets clustering result.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.clustering_result import ClusteringResult
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    result_id = 'a9b28f9dc55f37ea9f4a5fb0c76895923591e781' # str | Result ID
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # (EXPERIMENTAL) Smart functions - Clustering Result
        api_response = api_instance.clustering_result(workspace_id, result_id, offset=offset, limit=limit)
        print("The response of SmartFunctionsApi->clustering_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->clustering_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **result_id** | **str**| Result ID | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ClusteringResult**](ClusteringResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **created_by**
> AnalyticsCatalogCreatedBy created_by(workspace_id)

Get Analytics Catalog CreatedBy Users

Returns a list of Users who created any object for this workspace

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.analytics_catalog_created_by import AnalyticsCatalogCreatedBy
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier

    try:
        # Get Analytics Catalog CreatedBy Users
        api_response = api_instance.created_by(workspace_id)
        print("The response of SmartFunctionsApi->created_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->created_by: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 

### Return type

[**AnalyticsCatalogCreatedBy**](AnalyticsCatalogCreatedBy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast**
> SmartFunctionResponse forecast(workspace_id, result_id, forecast_request, skip_cache=skip_cache)

(BETA) Smart functions - Forecast

(BETA) Computes forecasted data points from the provided execution result and parameters.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.forecast_request import ForecastRequest
from gooddata_api_client.models.smart_function_response import SmartFunctionResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    result_id = '9bd52018570364264fcf62d373da6bed313120e8' # str | Input result ID to be used in the computation
    forecast_request = gooddata_api_client.ForecastRequest() # ForecastRequest | 
    skip_cache = False # bool | Ignore all caches during execution of current request. (optional) (default to False)

    try:
        # (BETA) Smart functions - Forecast
        api_response = api_instance.forecast(workspace_id, result_id, forecast_request, skip_cache=skip_cache)
        print("The response of SmartFunctionsApi->forecast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->forecast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **result_id** | **str**| Input result ID to be used in the computation | 
 **forecast_request** | [**ForecastRequest**](ForecastRequest.md)|  | 
 **skip_cache** | **bool**| Ignore all caches during execution of current request. | [optional] [default to False]

### Return type

[**SmartFunctionResponse**](SmartFunctionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forecast_result**
> ForecastResult forecast_result(workspace_id, result_id, offset=offset, limit=limit)

(BETA) Smart functions - Forecast Result

(BETA) Gets forecast result.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.forecast_result import ForecastResult
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    result_id = 'a9b28f9dc55f37ea9f4a5fb0c76895923591e781' # str | Result ID
    offset = 56 # int |  (optional)
    limit = 56 # int |  (optional)

    try:
        # (BETA) Smart functions - Forecast Result
        api_response = api_instance.forecast_result(workspace_id, result_id, offset=offset, limit=limit)
        print("The response of SmartFunctionsApi->forecast_result:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->forecast_result: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **result_id** | **str**| Result ID | 
 **offset** | **int**|  | [optional] 
 **limit** | **int**|  | [optional] 

### Return type

[**ForecastResult**](ForecastResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_description**
> GenerateDescriptionResponse generate_description(workspace_id, generate_description_request)

Generate Description for Analytics Object

Generates a description for the specified analytics object. Returns description and a note with details if generation was not performed.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.generate_description_request import GenerateDescriptionRequest
from gooddata_api_client.models.generate_description_response import GenerateDescriptionResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    generate_description_request = gooddata_api_client.GenerateDescriptionRequest() # GenerateDescriptionRequest | 

    try:
        # Generate Description for Analytics Object
        api_response = api_instance.generate_description(workspace_id, generate_description_request)
        print("The response of SmartFunctionsApi->generate_description:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->generate_description: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **generate_description_request** | [**GenerateDescriptionRequest**](GenerateDescriptionRequest.md)|  | 

### Return type

[**GenerateDescriptionResponse**](GenerateDescriptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_title**
> GenerateTitleResponse generate_title(workspace_id, generate_title_request)

Generate Title for Analytics Object

Generates a title for the specified analytics object. Returns title and a note with details if generation was not performed.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.generate_title_request import GenerateTitleRequest
from gooddata_api_client.models.generate_title_response import GenerateTitleResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    generate_title_request = gooddata_api_client.GenerateTitleRequest() # GenerateTitleRequest | 

    try:
        # Generate Title for Analytics Object
        api_response = api_instance.generate_title(workspace_id, generate_title_request)
        print("The response of SmartFunctionsApi->generate_title:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->generate_title: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **generate_title_request** | [**GenerateTitleRequest**](GenerateTitleRequest.md)|  | 

### Return type

[**GenerateTitleResponse**](GenerateTitleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quality_issues**
> GetQualityIssuesResponse get_quality_issues(workspace_id)

Get Quality Issues

Returns metadata quality issues detected by the platform linter.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.get_quality_issues_response import GetQualityIssuesResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier

    try:
        # Get Quality Issues
        api_response = api_instance.get_quality_issues(workspace_id)
        print("The response of SmartFunctionsApi->get_quality_issues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->get_quality_issues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 

### Return type

[**GetQualityIssuesResponse**](GetQualityIssuesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quality_issues_calculation_status**
> QualityIssuesCalculationStatusResponse get_quality_issues_calculation_status(workspace_id, process_id)

Get Quality Issues Calculation Status

Returns the status of a quality issues calculation process identified by process ID.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.quality_issues_calculation_status_response import QualityIssuesCalculationStatusResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier
    process_id = 'process_id_example' # str | 

    try:
        # Get Quality Issues Calculation Status
        api_response = api_instance.get_quality_issues_calculation_status(workspace_id, process_id)
        print("The response of SmartFunctionsApi->get_quality_issues_calculation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->get_quality_issues_calculation_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 
 **process_id** | **str**|  | 

### Return type

[**QualityIssuesCalculationStatusResponse**](QualityIssuesCalculationStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_llm_provider_models**
> ListLlmProviderModelsResponse list_llm_provider_models(list_llm_provider_models_request)

List LLM Provider Models

Lists models available on an LLM provider with a full definition. For Azure AI Foundry providers, the model family will be set to UNKNOWN because the endpoint does not expose the family.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.list_llm_provider_models_request import ListLlmProviderModelsRequest
from gooddata_api_client.models.list_llm_provider_models_response import ListLlmProviderModelsResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    list_llm_provider_models_request = gooddata_api_client.ListLlmProviderModelsRequest() # ListLlmProviderModelsRequest | 

    try:
        # List LLM Provider Models
        api_response = api_instance.list_llm_provider_models(list_llm_provider_models_request)
        print("The response of SmartFunctionsApi->list_llm_provider_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->list_llm_provider_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_llm_provider_models_request** | [**ListLlmProviderModelsRequest**](ListLlmProviderModelsRequest.md)|  | 

### Return type

[**ListLlmProviderModelsResponse**](ListLlmProviderModelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_llm_provider_models_by_id**
> ListLlmProviderModelsResponse list_llm_provider_models_by_id(llm_provider_id)

List LLM Provider Models By Id

Lists models available on an existing LLM provider by its ID. For Azure AI Foundry providers, the model family will be set to UNKNOWN because the endpoint does not expose the family.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.list_llm_provider_models_response import ListLlmProviderModelsResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    llm_provider_id = 'llm_provider_id_example' # str | 

    try:
        # List LLM Provider Models By Id
        api_response = api_instance.list_llm_provider_models_by_id(llm_provider_id)
        print("The response of SmartFunctionsApi->list_llm_provider_models_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->list_llm_provider_models_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **llm_provider_id** | **str**|  | 

### Return type

[**ListLlmProviderModelsResponse**](ListLlmProviderModelsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **memory_created_by_users**
> MemoryItemCreatedByUsers memory_created_by_users(workspace_id)

Get AI Memory CreatedBy Users

Returns a list of Users who created any memory item for this workspace

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.memory_item_created_by_users import MemoryItemCreatedByUsers
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier

    try:
        # Get AI Memory CreatedBy Users
        api_response = api_instance.memory_created_by_users(workspace_id)
        print("The response of SmartFunctionsApi->memory_created_by_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->memory_created_by_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 

### Return type

[**MemoryItemCreatedByUsers**](MemoryItemCreatedByUsers.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_llm_endpoints**
> ResolvedLlmEndpoints resolve_llm_endpoints(workspace_id)

Get Active LLM Endpoints for this workspace

Will be soon removed and replaced by LlmProvider-based resolution.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.resolved_llm_endpoints import ResolvedLlmEndpoints
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier

    try:
        # Get Active LLM Endpoints for this workspace
        api_response = api_instance.resolve_llm_endpoints(workspace_id)
        print("The response of SmartFunctionsApi->resolve_llm_endpoints:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->resolve_llm_endpoints: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 

### Return type

[**ResolvedLlmEndpoints**](ResolvedLlmEndpoints.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resolve_llm_providers**
> ResolvedLlms resolve_llm_providers(workspace_id)

Get Active LLM configuration for this workspace

Resolves the active LLM configuration for the given workspace. When the ENABLE_LLM_ENDPOINT_REPLACEMENT feature flag is enabled, returns LLM Providers with their associated models. Otherwise, falls back to the legacy LLM Endpoints.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.resolved_llms import ResolvedLlms
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier

    try:
        # Get Active LLM configuration for this workspace
        api_response = api_instance.resolve_llm_providers(workspace_id)
        print("The response of SmartFunctionsApi->resolve_llm_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->resolve_llm_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 

### Return type

[**ResolvedLlms**](ResolvedLlms.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags**
> AnalyticsCatalogTags tags(workspace_id)

Get Analytics Catalog Tags

Returns a list of tags for this workspace

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.analytics_catalog_tags import AnalyticsCatalogTags
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier

    try:
        # Get Analytics Catalog Tags
        api_response = api_instance.tags(workspace_id)
        print("The response of SmartFunctionsApi->tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 

### Return type

[**AnalyticsCatalogTags**](AnalyticsCatalogTags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_llm_provider**
> TestLlmProviderResponse test_llm_provider(test_llm_provider_definition_request)

Test LLM Provider

Tests LLM provider connectivity with a full definition.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.test_llm_provider_definition_request import TestLlmProviderDefinitionRequest
from gooddata_api_client.models.test_llm_provider_response import TestLlmProviderResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    test_llm_provider_definition_request = gooddata_api_client.TestLlmProviderDefinitionRequest() # TestLlmProviderDefinitionRequest | 

    try:
        # Test LLM Provider
        api_response = api_instance.test_llm_provider(test_llm_provider_definition_request)
        print("The response of SmartFunctionsApi->test_llm_provider:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->test_llm_provider: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **test_llm_provider_definition_request** | [**TestLlmProviderDefinitionRequest**](TestLlmProviderDefinitionRequest.md)|  | 

### Return type

[**TestLlmProviderResponse**](TestLlmProviderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_llm_provider_by_id**
> TestLlmProviderResponse test_llm_provider_by_id(llm_provider_id, test_llm_provider_by_id_request=test_llm_provider_by_id_request)

Test LLM Provider By Id

Tests an existing LLM provider connectivity by its ID.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.test_llm_provider_by_id_request import TestLlmProviderByIdRequest
from gooddata_api_client.models.test_llm_provider_response import TestLlmProviderResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    llm_provider_id = 'llm_provider_id_example' # str | 
    test_llm_provider_by_id_request = gooddata_api_client.TestLlmProviderByIdRequest() # TestLlmProviderByIdRequest |  (optional)

    try:
        # Test LLM Provider By Id
        api_response = api_instance.test_llm_provider_by_id(llm_provider_id, test_llm_provider_by_id_request=test_llm_provider_by_id_request)
        print("The response of SmartFunctionsApi->test_llm_provider_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->test_llm_provider_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **llm_provider_id** | **str**|  | 
 **test_llm_provider_by_id_request** | [**TestLlmProviderByIdRequest**](TestLlmProviderByIdRequest.md)|  | [optional] 

### Return type

[**TestLlmProviderResponse**](TestLlmProviderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trending_objects**
> TrendingObjectsResult trending_objects(workspace_id)

Get Trending Analytics Catalog Objects

Returns a list of trending objects for this workspace

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.trending_objects_result import TrendingObjectsResult
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier

    try:
        # Get Trending Analytics Catalog Objects
        api_response = api_instance.trending_objects(workspace_id)
        print("The response of SmartFunctionsApi->trending_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->trending_objects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 

### Return type

[**TrendingObjectsResult**](TrendingObjectsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_quality_issues_calculation**
> TriggerQualityIssuesCalculationResponse trigger_quality_issues_calculation(workspace_id)

Trigger Quality Issues Calculation

Triggers asynchronous calculation of metadata quality issues and returns a process ID for status tracking.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.trigger_quality_issues_calculation_response import TriggerQualityIssuesCalculationResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    workspace_id = 'workspace_id_example' # str | Workspace identifier

    try:
        # Trigger Quality Issues Calculation
        api_response = api_instance.trigger_quality_issues_calculation(workspace_id)
        print("The response of SmartFunctionsApi->trigger_quality_issues_calculation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->trigger_quality_issues_calculation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| Workspace identifier | 

### Return type

[**TriggerQualityIssuesCalculationResponse**](TriggerQualityIssuesCalculationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_llm_endpoint**
> ValidateLLMEndpointResponse validate_llm_endpoint(validate_llm_endpoint_request)

Validate LLM Endpoint

Will be soon removed and replaced by testLlmProvider.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.validate_llm_endpoint_request import ValidateLLMEndpointRequest
from gooddata_api_client.models.validate_llm_endpoint_response import ValidateLLMEndpointResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    validate_llm_endpoint_request = gooddata_api_client.ValidateLLMEndpointRequest() # ValidateLLMEndpointRequest | 

    try:
        # Validate LLM Endpoint
        api_response = api_instance.validate_llm_endpoint(validate_llm_endpoint_request)
        print("The response of SmartFunctionsApi->validate_llm_endpoint:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->validate_llm_endpoint: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_llm_endpoint_request** | [**ValidateLLMEndpointRequest**](ValidateLLMEndpointRequest.md)|  | 

### Return type

[**ValidateLLMEndpointResponse**](ValidateLLMEndpointResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_llm_endpoint_by_id**
> ValidateLLMEndpointResponse validate_llm_endpoint_by_id(llm_endpoint_id, validate_llm_endpoint_by_id_request=validate_llm_endpoint_by_id_request)

Validate LLM Endpoint By Id

Will be soon removed and replaced by testLlmProviderById.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.validate_llm_endpoint_by_id_request import ValidateLLMEndpointByIdRequest
from gooddata_api_client.models.validate_llm_endpoint_response import ValidateLLMEndpointResponse
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
    api_instance = gooddata_api_client.SmartFunctionsApi(api_client)
    llm_endpoint_id = 'llm_endpoint_id_example' # str | 
    validate_llm_endpoint_by_id_request = gooddata_api_client.ValidateLLMEndpointByIdRequest() # ValidateLLMEndpointByIdRequest |  (optional)

    try:
        # Validate LLM Endpoint By Id
        api_response = api_instance.validate_llm_endpoint_by_id(llm_endpoint_id, validate_llm_endpoint_by_id_request=validate_llm_endpoint_by_id_request)
        print("The response of SmartFunctionsApi->validate_llm_endpoint_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartFunctionsApi->validate_llm_endpoint_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **llm_endpoint_id** | **str**|  | 
 **validate_llm_endpoint_by_id_request** | [**ValidateLLMEndpointByIdRequest**](ValidateLLMEndpointByIdRequest.md)|  | [optional] 

### Return type

[**ValidateLLMEndpointResponse**](ValidateLLMEndpointResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

