# api.DataEntryApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_data_entry**](DataEntryApi.md#delete_data_entry) | **DELETE** /data/{resource_type}/{resource_id}/{time} | Deletes a data entry
[**get_data_entries**](DataEntryApi.md#get_data_entries) | **GET** /data/{resource_type}/{resource_id} | Get data sent from a resource.
[**get_data_entry**](DataEntryApi.md#get_data_entry) | **GET** /data/{resource_type}/{resource_id}/{time} | Gets a data entry
[**list_data_source_resources**](DataEntryApi.md#list_data_source_resources) | **GET** /data/resources | Get the list of data source resources


# **delete_data_entry**
> delete_data_entry(resource_type, resource_id, time)

Deletes a data entry

Deletes a data entry identified with resource ID and timestamp

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import data_entry_api
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
    api_instance = data_entry_api.DataEntryApi(api_client)
    resource_type = "Subscriber" # str | Type of data source resource
    resource_id = "resource_id_example" # str | ID of data source resource
    time = 1 # int | Timestamp of the target data entry to delete (unixtime in milliseconds).

    # example passing only required values which don't have defaults set
    try:
        # Deletes a data entry
        api_instance.delete_data_entry(resource_type, resource_id, time)
    except api.ApiException as e:
        print("Exception when calling DataEntryApi->delete_data_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Type of data source resource |
 **resource_id** | **str**| ID of data source resource |
 **time** | **int**| Timestamp of the target data entry to delete (unixtime in milliseconds). |

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
**204** | The data entry has been successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_entries**
> [DataEntry] get_data_entries(resource_type, resource_id)

Get data sent from a resource.

Returns a list of data entries sent from a resource that match certain criteria. If the total number of entries does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import data_entry_api
from api.model.data_entry import DataEntry
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
    api_instance = data_entry_api.DataEntryApi(api_client)
    resource_type = "Subscriber" # str | Type of data source resource
    resource_id = "resource_id_example" # str | ID of data source resource
    _from = 1 # int | Start time for the data entries search range (unixtime in milliseconds). (optional)
    to = 1 # int | End time for the data entries search range (unixtime in milliseconds). (optional)
    sort = "desc" # str | Sort order of the data entries. Either descending (latest data entry first) or ascending (oldest data entry first). (optional) if omitted the server will use the default value of "desc"
    limit = 1 # int | Maximum number of data entries to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The value of `time` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get data sent from a resource.
        api_response = api_instance.get_data_entries(resource_type, resource_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DataEntryApi->get_data_entries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data sent from a resource.
        api_response = api_instance.get_data_entries(resource_type, resource_id, _from=_from, to=to, sort=sort, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DataEntryApi->get_data_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Type of data source resource |
 **resource_id** | **str**| ID of data source resource |
 **_from** | **int**| Start time for the data entries search range (unixtime in milliseconds). | [optional]
 **to** | **int**| End time for the data entries search range (unixtime in milliseconds). | [optional]
 **sort** | **str**| Sort order of the data entries. Either descending (latest data entry first) or ascending (oldest data entry first). | [optional] if omitted the server will use the default value of "desc"
 **limit** | **int**| Maximum number of data entries to retrieve. | [optional]
 **last_evaluated_key** | **str**| The value of &#x60;time&#x60; in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. | [optional]

### Return type

[**[DataEntry]**](DataEntry.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of data entries. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_entry**
> get_data_entry(resource_type, resource_id, time)

Gets a data entry

Gets a data entry identified with resource ID and timestamp

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import data_entry_api
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
    api_instance = data_entry_api.DataEntryApi(api_client)
    resource_type = "Subscriber" # str | Type of data source resource
    resource_id = "resource_id_example" # str | ID of data source resource
    time = 1 # int | Timestamp of the target data entry to get (unixtime in milliseconds).

    # example passing only required values which don't have defaults set
    try:
        # Gets a data entry
        api_instance.get_data_entry(resource_type, resource_id, time)
    except api.ApiException as e:
        print("Exception when calling DataEntryApi->get_data_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Type of data source resource |
 **resource_id** | **str**| ID of data source resource |
 **time** | **int**| Timestamp of the target data entry to get (unixtime in milliseconds). |

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
**200** | The data entry specified with resource ID and timestamp |  -  |
**404** | No such entry found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_data_source_resources**
> [DataSourceResourceMetadata] list_data_source_resources()

Get the list of data source resources

Returns a list of data source resources that have sent data from resources that belong to the operator. If the total number of entries does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import data_entry_api
from api.model.data_source_resource_metadata import DataSourceResourceMetadata
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
    api_instance = data_entry_api.DataEntryApi(api_client)
    resource_type = "Subscriber" # str | Type of data source resource (optional)
    limit = 1 # int | Maximum number of data entries to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The value of `resourceId` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the list of data source resources
        api_response = api_instance.list_data_source_resources(resource_type=resource_type, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DataEntryApi->list_data_source_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Type of data source resource | [optional]
 **limit** | **int**| Maximum number of data entries to retrieve. | [optional]
 **last_evaluated_key** | **str**| The value of &#x60;resourceId&#x60; in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. | [optional]

### Return type

[**[DataSourceResourceMetadata]**](DataSourceResourceMetadata.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of data source resources. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

