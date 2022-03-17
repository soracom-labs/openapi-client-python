# api.LogApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_logs**](LogApi.md#get_logs) | **GET** /logs | Get Logs.


# **get_logs**
> [LogEntry] get_logs()

Get Logs.

Returns a list of log entries that match certain criteria. If the total number of entries does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import log_api
from api.model.log_entry import LogEntry
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = api.Configuration(
    host = "https://api.soracom.io/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: api_key
configuration.api_key['api_key'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_key'] = 'Bearer'

# Configure API key authorization: api_token
configuration.api_key['api_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api_token'] = 'Bearer'

# Enter a context with an instance of the API client
with api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = log_api.LogApi(api_client)
    resource_type = "Subscriber" # str | Type of the target resource to query log entries. (optional)
    resource_id = "resource_id_example" # str | Identity of the target resource to query log entries. (optional)
    service = "Air" # str | Service name to filter log entries. (optional)
    _from = 1 # int | Start time for the log search range (unixtime). (optional)
    to = 1 # int | End time for the log search range (unixtime). (optional)
    limit = 1 # int | Maximum number of log entries to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The value of `time` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Logs.
        api_response = api_instance.get_logs(resource_type=resource_type, resource_id=resource_id, service=service, _from=_from, to=to, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LogApi->get_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Type of the target resource to query log entries. | [optional]
 **resource_id** | **str**| Identity of the target resource to query log entries. | [optional]
 **service** | **str**| Service name to filter log entries. | [optional]
 **_from** | **int**| Start time for the log search range (unixtime). | [optional]
 **to** | **int**| End time for the log search range (unixtime). | [optional]
 **limit** | **int**| Maximum number of log entries to retrieve. | [optional]
 **last_evaluated_key** | **str**| The value of &#x60;time&#x60; in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. | [optional]

### Return type

[**[LogEntry]**](LogEntry.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of log entries. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

