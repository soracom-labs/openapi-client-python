# soracom_api.DiagnosticApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_diagnostic**](DiagnosticApi.md#get_diagnostic) | **GET** /diagnostics/{diagnostic_id} | Get diagnostic
[**send_diagnostic_request**](DiagnosticApi.md#send_diagnostic_request) | **POST** /diagnostics | Send diagnostic request


# **get_diagnostic**
> DiagnosticResponse get_diagnostic(diagnostic_id)

Get diagnostic

Returns a diagnostic.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import diagnostic_api
from soracom_api.model.diagnostic_response import DiagnosticResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_api.Configuration(
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
with soracom_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = diagnostic_api.DiagnosticApi(api_client)
    diagnostic_id = "diagnostic_id_example" # str | The identifier of diagnostic request.

    # example passing only required values which don't have defaults set
    try:
        # Get diagnostic
        api_response = api_instance.get_diagnostic(diagnostic_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling DiagnosticApi->get_diagnostic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagnostic_id** | **str**| The identifier of diagnostic request. |

### Return type

[**DiagnosticResponse**](DiagnosticResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**404** | The specified diagnostic_id is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_diagnostic_request**
> [DiagnosticResponse] send_diagnostic_request(diagnostic_request)

Send diagnostic request

Send a diagnostic request.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import diagnostic_api
from soracom_api.model.diagnostic_response import DiagnosticResponse
from soracom_api.model.diagnostic_request import DiagnosticRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_api.Configuration(
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
with soracom_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = diagnostic_api.DiagnosticApi(api_client)
    diagnostic_request = DiagnosticRequest(
        _from=1,
        resource_id="resource_id_example",
        resource_type="sim",
        service="Air",
        to=1,
    ) # DiagnosticRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Send diagnostic request
        api_response = api_instance.send_diagnostic_request(diagnostic_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling DiagnosticApi->send_diagnostic_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **diagnostic_request** | [**DiagnosticRequest**](DiagnosticRequest.md)| request |

### Return type

[**[DiagnosticResponse]**](DiagnosticResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully accepted a diagnostic request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

