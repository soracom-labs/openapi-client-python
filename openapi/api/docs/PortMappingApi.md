# api.PortMappingApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_port_mapping**](PortMappingApi.md#create_port_mapping) | **POST** /port_mappings | Create Port Mapping.
[**delete_port_mapping**](PortMappingApi.md#delete_port_mapping) | **DELETE** /port_mappings/{ip_address}/{port} | Delete PortMapping.
[**list_port_mappings**](PortMappingApi.md#list_port_mappings) | **GET** /port_mappings | List Port Mapping Entries.
[**list_port_mappings_for_subscriber**](PortMappingApi.md#list_port_mappings_for_subscriber) | **GET** /port_mappings/subscribers/{imsi} | Get Port Mapping entries for a subscriber.


# **create_port_mapping**
> PortMapping create_port_mapping(create_port_mapping_request)

Create Port Mapping.

Create a new port mapping.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import port_mapping_api
from api.model.create_port_mapping_request import CreatePortMappingRequest
from api.model.port_mapping import PortMapping
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
    api_instance = port_mapping_api.PortMappingApi(api_client)
    create_port_mapping_request = CreatePortMappingRequest(
        destination=PortMappingDestination(
            imsi="imsi_example",
            port=3.14,
        ),
        duration=3.14,
        source=PortMappingSource(
            ip_ranges=[
                "ip_ranges_example",
            ],
        ),
        tls_required=True,
    ) # CreatePortMappingRequest | Port mapping to be created.

    # example passing only required values which don't have defaults set
    try:
        # Create Port Mapping.
        api_response = api_instance.create_port_mapping(create_port_mapping_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling PortMappingApi->create_port_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_port_mapping_request** | [**CreatePortMappingRequest**](CreatePortMappingRequest.md)| Port mapping to be created. |

### Return type

[**PortMapping**](PortMapping.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_port_mapping**
> delete_port_mapping(ip_address, port)

Delete PortMapping.

Deletes the specified port mapping entry

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import port_mapping_api
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
    api_instance = port_mapping_api.PortMappingApi(api_client)
    ip_address = "ip_address_example" # str | IP address of the target port mapping entry
    port = "port_example" # str | Port of the target port mapping entry

    # example passing only required values which don't have defaults set
    try:
        # Delete PortMapping.
        api_instance.delete_port_mapping(ip_address, port)
    except api.ApiException as e:
        print("Exception when calling PortMappingApi->delete_port_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_address** | **str**| IP address of the target port mapping entry |
 **port** | **str**| Port of the target port mapping entry |

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
**204** | Deletion of specified port mapping entry complete. |  -  |
**404** | The specified port mapping entry does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_port_mappings**
> [PortMapping] list_port_mappings()

List Port Mapping Entries.

Returns a list of port mappings.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import port_mapping_api
from api.model.port_mapping import PortMapping
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
    api_instance = port_mapping_api.PortMappingApi(api_client)
    limit = 1 # int | Maximum number of results per response page. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The last Port Mapping ID retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next group onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Port Mapping Entries.
        api_response = api_instance.list_port_mappings(limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling PortMappingApi->list_port_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results per response page. | [optional]
 **last_evaluated_key** | **str**| The last Port Mapping ID retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next group onward. | [optional]

### Return type

[**[PortMapping]**](PortMapping.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of port mappings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_port_mappings_for_subscriber**
> PortMapping list_port_mappings_for_subscriber(imsi)

Get Port Mapping entries for a subscriber.

Returns the port mapping entries for a subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import port_mapping_api
from api.model.port_mapping import PortMapping
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
    api_instance = port_mapping_api.PortMappingApi(api_client)
    imsi = "imsi_example" # str | Target subscriber IMSI.

    # example passing only required values which don't have defaults set
    try:
        # Get Port Mapping entries for a subscriber.
        api_response = api_instance.list_port_mappings_for_subscriber(imsi)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling PortMappingApi->list_port_mappings_for_subscriber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| Target subscriber IMSI. |

### Return type

[**PortMapping**](PortMapping.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of port mapping entries for the subscriber. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

