# soracom_api.LoraGatewayApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_lora_gateway_tag**](LoraGatewayApi.md#delete_lora_gateway_tag) | **DELETE** /lora_gateways/{gateway_id}/tags/{tag_name} | Delete LoRa gateway tag.
[**disable_termination_on_lora_gateway**](LoraGatewayApi.md#disable_termination_on_lora_gateway) | **POST** /lora_gateways/{gateway_id}/disable_termination | Disable Termination of LoRa gateway.
[**enable_termination_on_lora_gateway**](LoraGatewayApi.md#enable_termination_on_lora_gateway) | **POST** /lora_gateways/{gateway_id}/enable_termination | Enable Termination of LoRa gateway.
[**get_lora_gateway**](LoraGatewayApi.md#get_lora_gateway) | **GET** /lora_gateways/{gateway_id} | Get LoRa gateway.
[**list_lora_gateways**](LoraGatewayApi.md#list_lora_gateways) | **GET** /lora_gateways | List LoRa Gateways.
[**put_lora_gateway_tags**](LoraGatewayApi.md#put_lora_gateway_tags) | **PUT** /lora_gateways/{gateway_id}/tags | Bulk Insert or Update LoRa gateway Tags.
[**set_lora_network_set**](LoraGatewayApi.md#set_lora_network_set) | **POST** /lora_gateways/{gateway_id}/set_network_set | Set Network Set ID of LoRa gateway.
[**terminate_lora_gateway**](LoraGatewayApi.md#terminate_lora_gateway) | **POST** /lora_gateways/{gateway_id}/terminate | Terminate LoRa gateway.
[**unset_lora_network_set**](LoraGatewayApi.md#unset_lora_network_set) | **POST** /lora_gateways/{gateway_id}/unset_network_set | Unset Network Set ID of LoRa gateway.


# **delete_lora_gateway_tag**
> delete_lora_gateway_tag(gateway_id, tag_name)

Delete LoRa gateway tag.

Deletes a tag from the specified LoRa gateway.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_gateway_api
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
    api_instance = lora_gateway_api.LoraGatewayApi(api_client)
    gateway_id = "gateway_id_example" # str | ID of the target LoRa gateway.
    tag_name = "tag_name_example" # str | Name of tag to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().)

    # example passing only required values which don't have defaults set
    try:
        # Delete LoRa gateway tag.
        api_instance.delete_lora_gateway_tag(gateway_id, tag_name)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraGatewayApi->delete_lora_gateway_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| ID of the target LoRa gateway. |
 **tag_name** | **str**| Name of tag to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().) |

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
**204** | Deletion of specified tag complete. |  -  |
**404** | The specified LoRa gateway or the tag does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_termination_on_lora_gateway**
> LoraGateway disable_termination_on_lora_gateway(gateway_id)

Disable Termination of LoRa gateway.

Disables termination of specified LoRa gateway.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_gateway_api
from soracom_api.model.lora_gateway import LoraGateway
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
    api_instance = lora_gateway_api.LoraGatewayApi(api_client)
    gateway_id = "gateway_id_example" # str | ID of the target LoRa gateway.

    # example passing only required values which don't have defaults set
    try:
        # Disable Termination of LoRa gateway.
        api_response = api_instance.disable_termination_on_lora_gateway(gateway_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraGatewayApi->disable_termination_on_lora_gateway: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| ID of the target LoRa gateway. |

### Return type

[**LoraGateway**](LoraGateway.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa gateway&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa gateway does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_termination_on_lora_gateway**
> LoraGateway enable_termination_on_lora_gateway(gateway_id)

Enable Termination of LoRa gateway.

Enables termination of specified LoRa gateway.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_gateway_api
from soracom_api.model.lora_gateway import LoraGateway
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
    api_instance = lora_gateway_api.LoraGatewayApi(api_client)
    gateway_id = "gateway_id_example" # str | ID of the target LoRa gateway.

    # example passing only required values which don't have defaults set
    try:
        # Enable Termination of LoRa gateway.
        api_response = api_instance.enable_termination_on_lora_gateway(gateway_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraGatewayApi->enable_termination_on_lora_gateway: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| ID of the target LoRa gateway. |

### Return type

[**LoraGateway**](LoraGateway.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa gateway&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa gateway does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lora_gateway**
> LoraGateway get_lora_gateway(gateway_id)

Get LoRa gateway.

Returns information about the specified LoRa gateway.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_gateway_api
from soracom_api.model.lora_gateway import LoraGateway
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
    api_instance = lora_gateway_api.LoraGatewayApi(api_client)
    gateway_id = "gateway_id_example" # str | Gateway ID of the target LoRa gateway.

    # example passing only required values which don't have defaults set
    try:
        # Get LoRa gateway.
        api_response = api_instance.get_lora_gateway(gateway_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraGatewayApi->get_lora_gateway: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| Gateway ID of the target LoRa gateway. |

### Return type

[**LoraGateway**](LoraGateway.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa gateway&#39;s detailed information. |  -  |
**404** | The specified LoRa gateway does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lora_gateways**
> [LoraGateway] list_lora_gateways()

List LoRa Gateways.

Returns a list of LoRa gateways that match certain criteria. If the total number of LoRa gateways does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_gateway_api
from soracom_api.model.lora_gateway import LoraGateway
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
    api_instance = lora_gateway_api.LoraGatewayApi(api_client)
    tag_name = "tag_name_example" # str | Tag name for filtering the search (exact match). (optional)
    tag_value = "tag_value_example" # str | Tag search string for filtering the search. Required when `tag_name` has been specified. (optional)
    tag_value_match_mode = "exact" # str | Tag match mode. (optional) if omitted the server will use the default value of "exact"
    limit = 1 # int | Maximum number of LoRa devices to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The device ID of the last device retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next device onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List LoRa Gateways.
        api_response = api_instance.list_lora_gateways(tag_name=tag_name, tag_value=tag_value, tag_value_match_mode=tag_value_match_mode, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraGatewayApi->list_lora_gateways: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| Tag name for filtering the search (exact match). | [optional]
 **tag_value** | **str**| Tag search string for filtering the search. Required when &#x60;tag_name&#x60; has been specified. | [optional]
 **tag_value_match_mode** | **str**| Tag match mode. | [optional] if omitted the server will use the default value of "exact"
 **limit** | **int**| Maximum number of LoRa devices to retrieve. | [optional]
 **last_evaluated_key** | **str**| The device ID of the last device retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next device onward. | [optional]

### Return type

[**[LoraGateway]**](LoraGateway.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of LoRa gateways. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_lora_gateway_tags**
> LoraGateway put_lora_gateway_tags(gateway_id, tag_update_request)

Bulk Insert or Update LoRa gateway Tags.

Inserts/updates tags for the specified LoRa gateway.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_gateway_api
from soracom_api.model.tag_update_request import TagUpdateRequest
from soracom_api.model.lora_gateway import LoraGateway
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
    api_instance = lora_gateway_api.LoraGatewayApi(api_client)
    gateway_id = "gateway_id_example" # str | ID of the target LoRa gateway.
    tag_update_request = [
        TagUpdateRequest(
            tag_name="tag_name_example",
            tag_value="tag_value_example",
        ),
    ] # [TagUpdateRequest] | Array of tags to be inserted/updated.

    # example passing only required values which don't have defaults set
    try:
        # Bulk Insert or Update LoRa gateway Tags.
        api_response = api_instance.put_lora_gateway_tags(gateway_id, tag_update_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraGatewayApi->put_lora_gateway_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| ID of the target LoRa gateway. |
 **tag_update_request** | [**[TagUpdateRequest]**](TagUpdateRequest.md)| Array of tags to be inserted/updated. |

### Return type

[**LoraGateway**](LoraGateway.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa gateway&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa gateway does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_lora_network_set**
> LoraGateway set_lora_network_set(gateway_id)

Set Network Set ID of LoRa gateway.

Sets or overwrites network set ID for the specified LoRa gateway.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_gateway_api
from soracom_api.model.lora_gateway import LoraGateway
from soracom_api.model.set_network_set_request import SetNetworkSetRequest
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
    api_instance = lora_gateway_api.LoraGatewayApi(api_client)
    gateway_id = "gateway_id_example" # str | ID of the target LoRa gateway.
    set_network_set_request = SetNetworkSetRequest(
        network_set_id="network_set_id_example",
    ) # SetNetworkSetRequest | LoRa Network Set ID. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set Network Set ID of LoRa gateway.
        api_response = api_instance.set_lora_network_set(gateway_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraGatewayApi->set_lora_network_set: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set Network Set ID of LoRa gateway.
        api_response = api_instance.set_lora_network_set(gateway_id, set_network_set_request=set_network_set_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraGatewayApi->set_lora_network_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| ID of the target LoRa gateway. |
 **set_network_set_request** | [**SetNetworkSetRequest**](SetNetworkSetRequest.md)| LoRa Network Set ID. | [optional]

### Return type

[**LoraGateway**](LoraGateway.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa gateway&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_lora_gateway**
> LoraGateway terminate_lora_gateway(gateway_id)

Terminate LoRa gateway.

Terminates the specified LoRa gateway

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_gateway_api
from soracom_api.model.lora_gateway import LoraGateway
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
    api_instance = lora_gateway_api.LoraGatewayApi(api_client)
    gateway_id = "gateway_id_example" # str | Device ID of the target LoRa gateway.

    # example passing only required values which don't have defaults set
    try:
        # Terminate LoRa gateway.
        api_response = api_instance.terminate_lora_gateway(gateway_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraGatewayApi->terminate_lora_gateway: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| Device ID of the target LoRa gateway. |

### Return type

[**LoraGateway**](LoraGateway.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa gateway&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa gateway does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_lora_network_set**
> LoraGateway unset_lora_network_set(gateway_id)

Unset Network Set ID of LoRa gateway.

Unset network set ID of the specified LoRa gateway.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_gateway_api
from soracom_api.model.lora_gateway import LoraGateway
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
    api_instance = lora_gateway_api.LoraGatewayApi(api_client)
    gateway_id = "gateway_id_example" # str | ID of the target LoRa gateway.

    # example passing only required values which don't have defaults set
    try:
        # Unset Network Set ID of LoRa gateway.
        api_response = api_instance.unset_lora_network_set(gateway_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraGatewayApi->unset_lora_network_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **gateway_id** | **str**| ID of the target LoRa gateway. |

### Return type

[**LoraGateway**](LoraGateway.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa gateway&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa gateway does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

