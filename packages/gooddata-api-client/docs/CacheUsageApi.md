# gooddata_api_client.CacheUsageApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collect_cache_usage**](CacheUsageApi.md#collect_cache_usage) | **GET** /api/v1/actions/collectCacheUsage | Collect data about the current cache usage


# **collect_cache_usage**
> CacheUsageData collect_cache_usage()

Collect data about the current cache usage

Get the detailed data about how much cache your organization is currently using, broken down by individual workspaces.

### Example


```python
import gooddata_api_client
from gooddata_api_client.models.cache_usage_data import CacheUsageData
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
    api_instance = gooddata_api_client.CacheUsageApi(api_client)

    try:
        # Collect data about the current cache usage
        api_response = api_instance.collect_cache_usage()
        print("The response of CacheUsageApi->collect_cache_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CacheUsageApi->collect_cache_usage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CacheUsageData**](CacheUsageData.md)

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

