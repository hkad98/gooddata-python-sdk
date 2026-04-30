# gooddata_api_client.AACAnalyticsModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_analytics_model_aac**](AACAnalyticsModelApi.md#get_analytics_model_aac) | **GET** /api/v1/aac/workspaces/{workspaceId}/analyticsModel | Get analytics model in AAC format
[**set_analytics_model_aac**](AACAnalyticsModelApi.md#set_analytics_model_aac) | **PUT** /api/v1/aac/workspaces/{workspaceId}/analyticsModel | Set analytics model from AAC format


# **get_analytics_model_aac**
> AacAnalyticsModel get_analytics_model_aac(workspace_id, exclude=exclude)

Get analytics model in AAC format


            Retrieve the analytics model of the workspace in Analytics as Code format.
            
            The returned format is compatible with the YAML definitions used by the 
            GoodData Analytics as Code VSCode extension. This includes metrics, 
            dashboards, visualizations, plugins, and attribute hierarchies.
        

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.aac_analytics_model import AacAnalyticsModel
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
    api_instance = gooddata_api_client.AACAnalyticsModelApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    exclude = ['exclude_example'] # List[str] |  (optional)

    try:
        # Get analytics model in AAC format
        api_response = api_instance.get_analytics_model_aac(workspace_id, exclude=exclude)
        print("The response of AACAnalyticsModelApi->get_analytics_model_aac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AACAnalyticsModelApi->get_analytics_model_aac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **exclude** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**AacAnalyticsModel**](AacAnalyticsModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved current analytics model in AAC format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_analytics_model_aac**
> set_analytics_model_aac(workspace_id, aac_analytics_model)

Set analytics model from AAC format


            Set the analytics model of the workspace using Analytics as Code format.
            
            The input format is compatible with the YAML definitions used by the 
            GoodData Analytics as Code VSCode extension. This replaces the entire 
            analytics model with the provided definition, including metrics, 
            dashboards, visualizations, plugins, and attribute hierarchies.
        

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.aac_analytics_model import AacAnalyticsModel
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
    api_instance = gooddata_api_client.AACAnalyticsModelApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    aac_analytics_model = gooddata_api_client.AacAnalyticsModel() # AacAnalyticsModel | 

    try:
        # Set analytics model from AAC format
        api_instance.set_analytics_model_aac(workspace_id, aac_analytics_model)
    except Exception as e:
        print("Exception when calling AACAnalyticsModelApi->set_analytics_model_aac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **aac_analytics_model** | [**AacAnalyticsModel**](AacAnalyticsModel.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Analytics model successfully set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

