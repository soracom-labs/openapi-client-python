# api.LoraDeviceApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_lora_device_tag**](LoraDeviceApi.md#delete_lora_device_tag) | **DELETE** /lora_devices/{device_id}/tags/{tag_name} | Delete LoRa device Tag.
[**disable_termination_on_lora_device**](LoraDeviceApi.md#disable_termination_on_lora_device) | **POST** /lora_devices/{device_id}/disable_termination | Disable Termination of LoRa device.
[**enable_termination_on_lora_device**](LoraDeviceApi.md#enable_termination_on_lora_device) | **POST** /lora_devices/{device_id}/enable_termination | Enable Termination of LoRa device.
[**get_data_from_lora_device**](LoraDeviceApi.md#get_data_from_lora_device) | **GET** /lora_devices/{device_id}/data | Get data sent from a LoRa device.
[**get_lora_device**](LoraDeviceApi.md#get_lora_device) | **GET** /lora_devices/{device_id} | Get LoRa device.
[**list_lora_devices**](LoraDeviceApi.md#list_lora_devices) | **GET** /lora_devices | List LoRa devices.
[**put_lora_device_tags**](LoraDeviceApi.md#put_lora_device_tags) | **PUT** /lora_devices/{device_id}/tags | Bulk Insert or Update LoRa device Tags.
[**register_lora_device**](LoraDeviceApi.md#register_lora_device) | **POST** /lora_devices/{device_id}/register | Register LoRa device.
[**send_data_to_lora_device**](LoraDeviceApi.md#send_data_to_lora_device) | **POST** /lora_devices/{device_id}/data | Send data to a LoRa device.
[**set_lora_device_group**](LoraDeviceApi.md#set_lora_device_group) | **POST** /lora_devices/{device_id}/set_group | Set Group of LoRa device.
[**terminate_lora_device**](LoraDeviceApi.md#terminate_lora_device) | **POST** /lora_devices/{device_id}/terminate | Terminate LoRa device.
[**unset_lora_device_group**](LoraDeviceApi.md#unset_lora_device_group) | **POST** /lora_devices/{device_id}/unset_group | Unset Group of LoRa device.


# **delete_lora_device_tag**
> delete_lora_device_tag(device_id, tag_name)

Delete LoRa device Tag.

Deletes a tag from the specified LoRa device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    device_id = "device_id_example" # str | device ID of the target LoRa device.
    tag_name = "tag_name_example" # str | Tag name to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().)

    # example passing only required values which don't have defaults set
    try:
        # Delete LoRa device Tag.
        api_instance.delete_lora_device_tag(device_id, tag_name)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->delete_lora_device_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| device ID of the target LoRa device. |
 **tag_name** | **str**| Tag name to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().) |

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
**404** | The specified LoRa device or the tag does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_termination_on_lora_device**
> LoraDevice disable_termination_on_lora_device(device_id)

Disable Termination of LoRa device.

Disables termination of specified LoRa device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
from api.model.lora_device import LoraDevice
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target LoRa device.

    # example passing only required values which don't have defaults set
    try:
        # Disable Termination of LoRa device.
        api_response = api_instance.disable_termination_on_lora_device(device_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->disable_termination_on_lora_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target LoRa device. |

### Return type

[**LoraDevice**](LoraDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa device&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_termination_on_lora_device**
> LoraDevice enable_termination_on_lora_device(device_id)

Enable Termination of LoRa device.

Enables termination of specified LoRa device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
from api.model.lora_device import LoraDevice
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target LoRa device.

    # example passing only required values which don't have defaults set
    try:
        # Enable Termination of LoRa device.
        api_response = api_instance.enable_termination_on_lora_device(device_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->enable_termination_on_lora_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target LoRa device. |

### Return type

[**LoraDevice**](LoraDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa device&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_from_lora_device**
> [DataEntry] get_data_from_lora_device(device_id)

Get data sent from a LoRa device.

Returns a list of data entries sent from a LoRa device that match certain criteria. If the total number of entries does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target subscriber that generated data entries.
    _from = 1 # int | Start time for the data entries search range (unixtime in milliseconds). (optional)
    to = 1 # int | End time for the data entries search range (unixtime in milliseconds). (optional)
    sort = "desc" # str | Sort order of the data entries. Either descending (latest data entry first) or ascending (oldest data entry first). (optional) if omitted the server will use the default value of "desc"
    limit = 1 # int | Maximum number of data entries to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The value of `time` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get data sent from a LoRa device.
        api_response = api_instance.get_data_from_lora_device(device_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->get_data_from_lora_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data sent from a LoRa device.
        api_response = api_instance.get_data_from_lora_device(device_id, _from=_from, to=to, sort=sort, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->get_data_from_lora_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target subscriber that generated data entries. |
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

# **get_lora_device**
> LoraDevice get_lora_device(device_id)

Get LoRa device.

Returns information about the specified LoRa device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
from api.model.lora_device import LoraDevice
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target LoRa device.

    # example passing only required values which don't have defaults set
    try:
        # Get LoRa device.
        api_response = api_instance.get_lora_device(device_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->get_lora_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target LoRa device. |

### Return type

[**LoraDevice**](LoraDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa device&#39;s detailed information. |  -  |
**404** | The specified LoRa device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lora_devices**
> [LoraDevice] list_lora_devices()

List LoRa devices.

Returns a list of LoRa devices that match certain criteria. If the total number of LoRa devices does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
from api.model.lora_device import LoraDevice
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    tag_name = "tag_name_example" # str | Tag name for filtering the search (exact match). (optional)
    tag_value = "tag_value_example" # str | Tag search string for filtering the search. Required when `tag_name` has been specified. (optional)
    tag_value_match_mode = "exact" # str | Tag match mode. (optional) if omitted the server will use the default value of "exact"
    limit = 1 # int | Maximum number of LoRa devices to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The device ID of the last device retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next device onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List LoRa devices.
        api_response = api_instance.list_lora_devices(tag_name=tag_name, tag_value=tag_value, tag_value_match_mode=tag_value_match_mode, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->list_lora_devices: %s\n" % e)
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

[**[LoraDevice]**](LoraDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of LoRa devices. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_lora_device_tags**
> LoraDevice put_lora_device_tags(device_id, tag_update_request)

Bulk Insert or Update LoRa device Tags.

Inserts/updates tags for the specified LoRa device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
from api.model.tag_update_request import TagUpdateRequest
from api.model.lora_device import LoraDevice
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target LoRa device.
    tag_update_request = [
        TagUpdateRequest(
            tag_name="tag_name_example",
            tag_value="tag_value_example",
        ),
    ] # [TagUpdateRequest] | Array of tags to be inserted/updated.

    # example passing only required values which don't have defaults set
    try:
        # Bulk Insert or Update LoRa device Tags.
        api_response = api_instance.put_lora_device_tags(device_id, tag_update_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->put_lora_device_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target LoRa device. |
 **tag_update_request** | [**[TagUpdateRequest]**](TagUpdateRequest.md)| Array of tags to be inserted/updated. |

### Return type

[**LoraDevice**](LoraDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa device&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_lora_device**
> LoraDevice register_lora_device(device_id, register_lora_device_request)

Register LoRa device.

Registers a LoRa device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
from api.model.register_lora_device_request import RegisterLoraDeviceRequest
from api.model.lora_device import LoraDevice
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target LoRa device.
    register_lora_device_request = RegisterLoraDeviceRequest(
        group_id="group_id_example",
        registration_secret="registration_secret_example",
        tags={
            "key": "key_example",
        },
    ) # RegisterLoraDeviceRequest | LoRa device

    # example passing only required values which don't have defaults set
    try:
        # Register LoRa device.
        api_response = api_instance.register_lora_device(device_id, register_lora_device_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->register_lora_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target LoRa device. |
 **register_lora_device_request** | [**RegisterLoraDeviceRequest**](RegisterLoraDeviceRequest.md)| LoRa device |

### Return type

[**LoraDevice**](LoraDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | LoRa device registration complete. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_data_to_lora_device**
> send_data_to_lora_device(device_id, lora_data)

Send data to a LoRa device.

Sends data to the specified LoRa device. The data is sent to the LoRa network server, to be sent out to the device using the next available slot. If another message destined for the same LoRa device ID is already waiting to be sent, the existing message will be discarded, and the new message will be sent instead.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
from api.model.lora_data import LoraData
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    device_id = "device_id_example" # str | ID of the recipient device.
    lora_data = LoraData(
        data="data_example",
        f_port=2,
    ) # LoraData | Binary data encoded as a hexadecimal string. Maximum length of original binary data is 11 octets (22 characters when encoded as a hexadecimal string). The number of characters must be even. fPort MUST be equal to or greater than 0. 0 is used for the control plane and 1 or greater values should be used in general. It defaults to 2 to avoid the issues of some devices from some vendors and all invalid values that can not be parsed fallback to 2.

    # example passing only required values which don't have defaults set
    try:
        # Send data to a LoRa device.
        api_instance.send_data_to_lora_device(device_id, lora_data)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->send_data_to_lora_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the recipient device. |
 **lora_data** | [**LoraData**](LoraData.md)| Binary data encoded as a hexadecimal string. Maximum length of original binary data is 11 octets (22 characters when encoded as a hexadecimal string). The number of characters must be even. fPort MUST be equal to or greater than 0. 0 is used for the control plane and 1 or greater values should be used in general. It defaults to 2 to avoid the issues of some devices from some vendors and all invalid values that can not be parsed fallback to 2. |

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
**204** | Data has been received and sent to the LoRa network server for the recipient device to retrieve. |  -  |
**400** | The payload JSON data contains one or more invalid parameters. |  -  |
**404** | No such device found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_lora_device_group**
> LoraDevice set_lora_device_group(device_id, group)

Set Group of LoRa device.

Sets or overwrites a group for the specified LoRa device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
from api.model.group import Group
from api.model.lora_device import LoraDevice
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target LoRa device.
    group = Group(
        configuration=Map(
            key="key_example",
        ),
        created_time=1,
        group_id="group_id_example",
        last_modified_time=1,
        operator_id="operator_id_example",
        tags=TagSet(
            key="key_example",
        ),
    ) # Group | Group (may include ID only).

    # example passing only required values which don't have defaults set
    try:
        # Set Group of LoRa device.
        api_response = api_instance.set_lora_device_group(device_id, group)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->set_lora_device_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target LoRa device. |
 **group** | [**Group**](Group.md)| Group (may include ID only). |

### Return type

[**LoraDevice**](LoraDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa device&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_lora_device**
> LoraDevice terminate_lora_device(device_id)

Terminate LoRa device.

Terminates the specified LoRa device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
from api.model.lora_device import LoraDevice
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target LoRa device.

    # example passing only required values which don't have defaults set
    try:
        # Terminate LoRa device.
        api_response = api_instance.terminate_lora_device(device_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->terminate_lora_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target LoRa device. |

### Return type

[**LoraDevice**](LoraDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa device&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_lora_device_group**
> LoraDevice unset_lora_device_group(device_id)

Unset Group of LoRa device.

Removes the group configuration from the specified LoRa device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lora_device_api
from api.model.lora_device import LoraDevice
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
    api_instance = lora_device_api.LoraDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target LoRa device.

    # example passing only required values which don't have defaults set
    try:
        # Unset Group of LoRa device.
        api_response = api_instance.unset_lora_device_group(device_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LoraDeviceApi->unset_lora_device_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target LoRa device. |

### Return type

[**LoraDevice**](LoraDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa device&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa device does not exist or the LoRa device does not belong to a group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

