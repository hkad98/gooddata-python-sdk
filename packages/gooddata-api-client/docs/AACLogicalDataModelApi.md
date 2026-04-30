# gooddata_api_client.AACLogicalDataModelApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logical_model_aac**](AACLogicalDataModelApi.md#get_logical_model_aac) | **GET** /api/v1/aac/workspaces/{workspaceId}/logicalModel | Get logical model in AAC format
[**set_logical_model_aac**](AACLogicalDataModelApi.md#set_logical_model_aac) | **PUT** /api/v1/aac/workspaces/{workspaceId}/logicalModel | Set logical model from AAC format


# **get_logical_model_aac**
> AacLogicalModel get_logical_model_aac(workspace_id, include_parents=include_parents)

Get logical model in AAC format


            Retrieve the logical data model of the workspace in Analytics as Code format.
            
            The returned format is compatible with the YAML definitions used by the 
            GoodData Analytics as Code VSCode extension. Use this for exporting models
            that can be directly used as YAML configuration files.
        

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.aac_logical_model import AacLogicalModel
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
    api_instance = gooddata_api_client.AACLogicalDataModelApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    include_parents = True # bool |  (optional)

    try:
        # Get logical model in AAC format
        api_response = api_instance.get_logical_model_aac(workspace_id, include_parents=include_parents)
        print("The response of AACLogicalDataModelApi->get_logical_model_aac:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AACLogicalDataModelApi->get_logical_model_aac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **include_parents** | **bool**|  | [optional] 

### Return type

[**AacLogicalModel**](AacLogicalModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieved current logical model in AAC format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_logical_model_aac**
> set_logical_model_aac(workspace_id, aac_logical_model)

Set logical model from AAC format


            Set the logical data model of the workspace using Analytics as Code format.
            
            The input format is compatible with the YAML definitions used by the 
            GoodData Analytics as Code VSCode extension. This replaces the entire 
            logical model with the provided definition.
        

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.aac_logical_model import AacLogicalModel
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
    api_instance = gooddata_api_client.AACLogicalDataModelApi(api_client)
    workspace_id = 'workspace_id_example' # str | 
    aac_logical_model = gooddata_api_client.AacLogicalModel() # AacLogicalModel | 

    try:
        # Set logical model from AAC format
        api_instance.set_logical_model_aac(workspace_id, aac_logical_model)
    except Exception as e:
        print("Exception when calling AACLogicalDataModelApi->set_logical_model_aac: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**|  | 
 **aac_logical_model** | [**AacLogicalModel**](AacLogicalModel.md)|  | 

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
**204** | Logical model successfully set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

