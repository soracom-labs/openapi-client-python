# api.FileEntryApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_directory**](FileEntryApi.md#delete_directory) | **DELETE** /files/{scope}/{path}/ | Delete specified directory in the scope.
[**delete_file**](FileEntryApi.md#delete_file) | **DELETE** /files/{scope}/{path} | Delete specified file in the scope.
[**find_files**](FileEntryApi.md#find_files) | **GET** /files | Find files with prefix query parameter in the scope
[**get_file**](FileEntryApi.md#get_file) | **GET** /files/{scope}/{path} | Download file specified by the path and the scope
[**get_file_metadata**](FileEntryApi.md#get_file_metadata) | **HEAD** /files/{scope}/{path} | Get the metadata of the file specified by the path and the scope
[**list_files**](FileEntryApi.md#list_files) | **GET** /files/{scope}/{path}/ | List files and directories on the path in the scope
[**put_file**](FileEntryApi.md#put_file) | **PUT** /files/{scope}/{path} | Upload file to the path in the scope.


# **delete_directory**
> delete_directory(path)

Delete specified directory in the scope.

Deletes the specified directory in the scope. Only `private` scope is allowed for the operation.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import file_entry_api
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
    api_instance = file_entry_api.FileEntryApi(api_client)
    path = "path_example" # str | Target directory path

    # example passing only required values which don't have defaults set
    try:
        # Delete specified directory in the scope.
        api_instance.delete_directory(path)
    except api.ApiException as e:
        print("Exception when calling FileEntryApi->delete_directory: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Target directory path |
 **scope** | **str**| Scope of the request | defaults to "private"

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
**204** | The specified directory is successfully deleted |  -  |
**400** | The specified directory is not empty |  -  |
**404** | No such directory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file**
> delete_file(path)

Delete specified file in the scope.

Deletes the specified file in the scope. Only `private` scope is allowed for the operation.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import file_entry_api
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
    api_instance = file_entry_api.FileEntryApi(api_client)
    path = "path_example" # str | Target path

    # example passing only required values which don't have defaults set
    try:
        # Delete specified file in the scope.
        api_instance.delete_file(path)
    except api.ApiException as e:
        print("Exception when calling FileEntryApi->delete_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Target path |
 **scope** | **str**| Scope of the request | defaults to "private"

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
**204** | The specified file is successfully deleted |  -  |
**404** | No such file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_files**
> [FileEntry] find_files(scope, prefix)

Find files with prefix query parameter in the scope

Returns a list of file entries which beginnings of their file paths are matched with the `prefix` query string in the ascending sorted UTF-8 bytes order of their file paths. An empty list is returned if the prefix does not match with any paths of file entries.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import file_entry_api
from api.model.file_entry import FileEntry
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
    api_instance = file_entry_api.FileEntryApi(api_client)
    scope = "private" # str | Scope of the request
    prefix = "prefix_example" # str | Prefix to match with file path
    limit = "10" # str | Num of entries (optional) if omitted the server will use the default value of "10"
    last_evaluated_key = "last_evaluated_key_example" # str | The filePath of the last file entry retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next file entry onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Find files with prefix query parameter in the scope
        api_response = api_instance.find_files(scope, prefix)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling FileEntryApi->find_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Find files with prefix query parameter in the scope
        api_response = api_instance.find_files(scope, prefix, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling FileEntryApi->find_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the request |
 **prefix** | **str**| Prefix to match with file path |
 **limit** | **str**| Num of entries | [optional] if omitted the server will use the default value of "10"
 **last_evaluated_key** | **str**| The filePath of the last file entry retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next file entry onward. | [optional]

### Return type

[**[FileEntry]**](FileEntry.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of file entries found with query parameters, which can be empty if the prefix does not match with any paths of file entries. |  -  |
**404** | The specified scope does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file**
> get_file(path)

Download file specified by the path and the scope

Redirects the client to URL for the link to download the file specified by the scope and the path. By issuing HTTP GET request to the link returned in the response, the client is able to download the file.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import file_entry_api
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
    api_instance = file_entry_api.FileEntryApi(api_client)
    path = "path_example" # str | Target path

    # example passing only required values which don't have defaults set
    try:
        # Download file specified by the path and the scope
        api_instance.get_file(path)
    except api.ApiException as e:
        print("Exception when calling FileEntryApi->get_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Target path |
 **scope** | **str**| Scope of the request | defaults to "private"

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
**302** | Client is redirected to the link to download the file. |  -  |
**404** | No such file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_metadata**
> FileEntry get_file_metadata(path)

Get the metadata of the file specified by the path and the scope

Gets metadata of the file specified by the path and the scope.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import file_entry_api
from api.model.file_entry import FileEntry
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
    api_instance = file_entry_api.FileEntryApi(api_client)
    path = "path_example" # str | Target path

    # example passing only required values which don't have defaults set
    try:
        # Get the metadata of the file specified by the path and the scope
        api_response = api_instance.get_file_metadata(path)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling FileEntryApi->get_file_metadata: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Target path |
 **scope** | **str**| Scope of the request | defaults to "private"

### Return type

[**FileEntry**](FileEntry.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Metadata of the file |  -  |
**404** | No such file |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_files**
> [FileEntry] list_files()

List files and directories on the path in the scope

Returns a list of file entries under the path in the scope. This operation works only for directories and an error will be retrurned if the file entry corresponds to the given path is not a directory. If the total number of entries does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import file_entry_api
from api.model.file_entry import FileEntry
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
    api_instance = file_entry_api.FileEntryApi(api_client)
    limit = "10" # str | Num of entries (optional) if omitted the server will use the default value of "10"
    last_evaluated_key = "last_evaluated_key_example" # str | The filename  of the last file entry retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next file entry onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List files and directories on the path in the scope
        api_response = api_instance.list_files()
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling FileEntryApi->list_files: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List files and directories on the path in the scope
        api_response = api_instance.list_files(limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling FileEntryApi->list_files: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope** | **str**| Scope of the request | defaults to "private"
 **path** | **str**| Target path | defaults to "/"
 **limit** | **str**| Num of entries | [optional] if omitted the server will use the default value of "10"
 **last_evaluated_key** | **str**| The filename  of the last file entry retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next file entry onward. | [optional]

### Return type

[**[FileEntry]**](FileEntry.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of file entries. |  -  |
**404** | No such directory |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_file**
> put_file(path, body)

Upload file to the path in the scope.

Uploads the file to the specified path in the scope. Only `private` scope is allowed for the operation.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import file_entry_api
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
    api_instance = file_entry_api.FileEntryApi(api_client)
    path = "path_example" # str | Target path
    body = open('/path/to/file', 'rb') # file_type | Content of the file to upload
    content_type = "content-type_example" # str | Content type of the file to upload (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload file to the path in the scope.
        api_instance.put_file(path, body)
    except api.ApiException as e:
        print("Exception when calling FileEntryApi->put_file: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload file to the path in the scope.
        api_instance.put_file(path, body, content_type=content_type)
    except api.ApiException as e:
        print("Exception when calling FileEntryApi->put_file: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Target path |
 **body** | **file_type**| Content of the file to upload |
 **scope** | **str**| Scope of the request | defaults to "private"
 **content_type** | **str**| Content type of the file to upload | [optional]

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
**200** | File is successfully updated with the content |  -  |
**201** | File is successfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

