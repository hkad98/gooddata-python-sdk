# gooddata_api_client.DataSourceFilesImportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**import_csv**](DataSourceFilesImportApi.md#import_csv) | **POST** /api/v1/actions/fileStorage/dataSources/{dataSourceId}/importCsv | Import CSV


# **import_csv**
> List[ImportCsvResponse] import_csv(data_source_id, import_csv_request)

Import CSV

Import the CSV files at the given locations in the staging area to the final location.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.import_csv_request import ImportCsvRequest
from gooddata_api_client.models.import_csv_response import ImportCsvResponse
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
    api_instance = gooddata_api_client.DataSourceFilesImportApi(api_client)
    data_source_id = 'data_source_id_example' # str | 
    import_csv_request = gooddata_api_client.ImportCsvRequest() # ImportCsvRequest | 

    try:
        # Import CSV
        api_response = api_instance.import_csv(data_source_id, import_csv_request)
        print("The response of DataSourceFilesImportApi->import_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DataSourceFilesImportApi->import_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_source_id** | **str**|  | 
 **import_csv_request** | [**ImportCsvRequest**](ImportCsvRequest.md)|  | 

### Return type

[**List[ImportCsvResponse]**](ImportCsvResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful import. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

