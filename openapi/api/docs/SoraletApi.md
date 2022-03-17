# api.SoraletApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_soralet**](SoraletApi.md#create_soralet) | **POST** /soralets | Create a Soralet.
[**delete_soralet**](SoraletApi.md#delete_soralet) | **DELETE** /soralets/{soralet_id} | Delete Soralet.
[**delete_soralet_version**](SoraletApi.md#delete_soralet_version) | **DELETE** /soralets/{soralet_id}/versions/{version} | Delete a Soralet version.
[**get_soralet**](SoraletApi.md#get_soralet) | **GET** /soralets/{soralet_id} | Get a Soralet.
[**get_soralet_logs**](SoraletApi.md#get_soralet_logs) | **GET** /soralets/{soralet_id}/logs | Get log messages from Soralet.
[**list_soralet_versions**](SoraletApi.md#list_soralet_versions) | **GET** /soralets/{soralet_id}/versions | List versions of Soralet.
[**list_soralets**](SoraletApi.md#list_soralets) | **GET** /soralets | List Soralets.
[**test_soralet**](SoraletApi.md#test_soralet) | **POST** /soralets/{soralet_id}/test | Execute Soralet with arguments.
[**upload_soralet_code**](SoraletApi.md#upload_soralet_code) | **POST** /soralets/{soralet_id}/versions | Upload code and create a new version.


# **create_soralet**
> create_soralet(create_soralet_request)

Create a Soralet.

Create a Soralet.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import soralet_api
from api.model.create_soralet_request import CreateSoraletRequest
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
    api_instance = soralet_api.SoraletApi(api_client)
    create_soralet_request = CreateSoraletRequest(
        description="description_example",
        soralet_id="soralet_id_example",
    ) # CreateSoraletRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Create a Soralet.
        api_instance.create_soralet(create_soralet_request)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->create_soralet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_soralet_request** | [**CreateSoraletRequest**](CreateSoraletRequest.md)| request |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new Soralet. |  -  |
**400** | The specified Soralet already exists or the specified soralet_id was invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_soralet**
> delete_soralet(soralet_id)

Delete Soralet.

Delete the specified Soralet.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import soralet_api
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
    api_instance = soralet_api.SoraletApi(api_client)
    soralet_id = "soralet_id_example" # str | The identifier of Soralet.

    # example passing only required values which don't have defaults set
    try:
        # Delete Soralet.
        api_instance.delete_soralet(soralet_id)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->delete_soralet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soralet_id** | **str**| The identifier of Soralet. |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted the specified Soralet. |  -  |
**404** | The specified Soralet is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_soralet_version**
> delete_soralet_version(soralet_id, version)

Delete a Soralet version.

Delete the specified Soralet version.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import soralet_api
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
    api_instance = soralet_api.SoraletApi(api_client)
    soralet_id = "soralet_id_example" # str | The identifier of Soralet.
    version = 1 # int | Soralet version.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Soralet version.
        api_instance.delete_soralet_version(soralet_id, version)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->delete_soralet_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soralet_id** | **str**| The identifier of Soralet. |
 **version** | **int**| Soralet version. |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted the specified Soralet version. |  -  |
**404** | The specified Soralet version is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_soralet**
> Soralet get_soralet(soralet_id)

Get a Soralet.

Returns a Soralet.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import soralet_api
from api.model.soralet import Soralet
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
    api_instance = soralet_api.SoraletApi(api_client)
    soralet_id = "soralet_id_example" # str | The identifier of Soralet.

    # example passing only required values which don't have defaults set
    try:
        # Get a Soralet.
        api_response = api_instance.get_soralet(soralet_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->get_soralet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soralet_id** | **str**| The identifier of Soralet. |

### Return type

[**Soralet**](Soralet.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**404** | The specified Soralet is not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_soralet_logs**
> [SoraletLog] get_soralet_logs(soralet_id)

Get log messages from Soralet.

Returns a list of log messages from the specified Soralet.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import soralet_api
from api.model.soralet_log import SoraletLog
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
    api_instance = soralet_api.SoraletApi(api_client)
    soralet_id = "soralet_id_example" # str | The identifier of Soralet.
    sort = "desc" # str | Sort order (optional) if omitted the server will use the default value of "desc"
    limit = 1 # int | The maximum number of items in a response. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The identifier of the last log message retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next log message onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get log messages from Soralet.
        api_response = api_instance.get_soralet_logs(soralet_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->get_soralet_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get log messages from Soralet.
        api_response = api_instance.get_soralet_logs(soralet_id, sort=sort, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->get_soralet_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soralet_id** | **str**| The identifier of Soralet. |
 **sort** | **str**| Sort order | [optional] if omitted the server will use the default value of "desc"
 **limit** | **int**| The maximum number of items in a response. | [optional]
 **last_evaluated_key** | **str**| The identifier of the last log message retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next log message onward. | [optional]

### Return type

[**[SoraletLog]**](SoraletLog.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_soralet_versions**
> [SoraletVersion] list_soralet_versions(soralet_id)

List versions of Soralet.

Returns a list of Soralet versions.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import soralet_api
from api.model.soralet_version import SoraletVersion
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
    api_instance = soralet_api.SoraletApi(api_client)
    soralet_id = "soralet_id_example" # str | The identifier of Soralet.
    sort = "desc" # str | Sort order (optional) if omitted the server will use the default value of "desc"
    limit = 1 # int | The maximum number of items in a response. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The identifier of the last version retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next version onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List versions of Soralet.
        api_response = api_instance.list_soralet_versions(soralet_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->list_soralet_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List versions of Soralet.
        api_response = api_instance.list_soralet_versions(soralet_id, sort=sort, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->list_soralet_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soralet_id** | **str**| The identifier of Soralet. |
 **sort** | **str**| Sort order | [optional] if omitted the server will use the default value of "desc"
 **limit** | **int**| The maximum number of items in a response. | [optional]
 **last_evaluated_key** | **str**| The identifier of the last version retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next version onward. | [optional]

### Return type

[**[SoraletVersion]**](SoraletVersion.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_soralets**
> [Soralet] list_soralets()

List Soralets.

Returns a list of Soralets.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import soralet_api
from api.model.soralet import Soralet
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
    api_instance = soralet_api.SoraletApi(api_client)
    sort = "asc" # str | Sort order (optional) if omitted the server will use the default value of "asc"
    limit = 1 # int | The maximum number of items in a response (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The identifier of the last Soralet retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next Soralet onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Soralets.
        api_response = api_instance.list_soralets(sort=sort, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->list_soralets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sort** | **str**| Sort order | [optional] if omitted the server will use the default value of "asc"
 **limit** | **int**| The maximum number of items in a response | [optional]
 **last_evaluated_key** | **str**| The identifier of the last Soralet retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next Soralet onward. | [optional]

### Return type

[**[Soralet]**](Soralet.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_soralet**
> ExecuteSoraletResponse test_soralet(soralet_id, execute_soralet_request)

Execute Soralet with arguments.

Execute the specified Soralet with the specified arguments.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import soralet_api
from api.model.execute_soralet_response import ExecuteSoraletResponse
from api.model.execute_soralet_request import ExecuteSoraletRequest
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
    api_instance = soralet_api.SoraletApi(api_client)
    soralet_id = "soralet_id_example" # str | The identifier of Soralet.
    execute_soralet_request = ExecuteSoraletRequest(
        content_type="content_type_example",
        direction="uplink",
        encoding_type="text",
        payload="payload_example",
        source={
            "key": SoraletDataSource(
                resource_id="resource_id_example",
                resource_type="resource_type_example",
            ),
        },
        userdata="userdata_example",
        version="version_example",
    ) # ExecuteSoraletRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Execute Soralet with arguments.
        api_response = api_instance.test_soralet(soralet_id, execute_soralet_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->test_soralet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soralet_id** | **str**| The identifier of Soralet. |
 **execute_soralet_request** | [**ExecuteSoraletRequest**](ExecuteSoraletRequest.md)| request |

### Return type

[**ExecuteSoraletResponse**](ExecuteSoraletResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_soralet_code**
> SoraletVersion upload_soralet_code(soralet_id, body)

Upload code and create a new version.

Upload code and create a new version.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import soralet_api
from api.model.soralet_version import SoraletVersion
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
    api_instance = soralet_api.SoraletApi(api_client)
    soralet_id = "soralet_id_example" # str | The identifier of Soralet.
    body = open('/path/to/file', 'rb') # file_type | 
    content_type = "content-type_example" # str | Content type of the file to upload (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload code and create a new version.
        api_response = api_instance.upload_soralet_code(soralet_id, body)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->upload_soralet_code: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload code and create a new version.
        api_response = api_instance.upload_soralet_code(soralet_id, body, content_type=content_type)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling SoraletApi->upload_soralet_code: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **soralet_id** | **str**| The identifier of Soralet. |
 **body** | **file_type**|  |
 **content_type** | **str**| Content type of the file to upload | [optional]

### Return type

[**SoraletVersion**](SoraletVersion.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new version. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

