# gooddata_api_client.DataSourceFilesDeletionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_files**](DataSourceFilesDeletionApi.md#delete_files) | **POST** /api/v1/actions/fileStorage/dataSources/{dataSourceId}/deleteFiles | Delete datasource files


# **delete_files**
> delete_files(data_source_id, delete_files_request)

Delete datasource files

Delete the files in the given data source.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.delete_files_request import DeleteFilesRequest
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
    api_instance = gooddata_api_client.DataSourceFilesDeletionApi(api_client)
    data_source_id = 'data_source_id_example' # str | 
    delete_files_request = gooddata_api_client.DeleteFilesRequest() # DeleteFilesRequest | 

    try:
        # Delete datasource files
        api_instance.delete_files(data_source_id, delete_files_request)
    except Exception as e:
        print("Exception when calling DataSourceFilesDeletionApi->delete_files: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_source_id** | **str**|  | 
 **delete_files_request** | [**DeleteFilesRequest**](DeleteFilesRequest.md)|  | 

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
**204** | Successful deletion. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

