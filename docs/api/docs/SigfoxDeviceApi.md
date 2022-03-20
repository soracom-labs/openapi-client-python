# soracom_api.SigfoxDeviceApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sigfox_device_tag**](SigfoxDeviceApi.md#delete_sigfox_device_tag) | **DELETE** /sigfox_devices/{device_id}/tags/{tag_name} | Delete Sigfox device Tag.
[**disable_termination_on_sigfox_device**](SigfoxDeviceApi.md#disable_termination_on_sigfox_device) | **POST** /sigfox_devices/{device_id}/disable_termination | Disable Termination of Sigfox device.
[**enable_termination_on_sigfox_device**](SigfoxDeviceApi.md#enable_termination_on_sigfox_device) | **POST** /sigfox_devices/{device_id}/enable_termination | Enable Termination of Sigfox device.
[**get_data_from_sigfox_device**](SigfoxDeviceApi.md#get_data_from_sigfox_device) | **GET** /sigfox_devices/{device_id}/data | Get data sent from a Sigfox device.
[**get_sigfox_device**](SigfoxDeviceApi.md#get_sigfox_device) | **GET** /sigfox_devices/{device_id} | Get Sigfox device.
[**list_sigfox_devices**](SigfoxDeviceApi.md#list_sigfox_devices) | **GET** /sigfox_devices | List Sigfox devices.
[**put_sigfox_device_tags**](SigfoxDeviceApi.md#put_sigfox_device_tags) | **PUT** /sigfox_devices/{device_id}/tags | Bulk Insert or Update Sigfox device Tags.
[**register_sigfox_device**](SigfoxDeviceApi.md#register_sigfox_device) | **POST** /sigfox_devices/{device_id}/register | Register a Sigfox device.
[**send_data_to_sigfox_device**](SigfoxDeviceApi.md#send_data_to_sigfox_device) | **POST** /sigfox_devices/{device_id}/data | Send data to a Sigfox device.
[**set_sigfox_device_group**](SigfoxDeviceApi.md#set_sigfox_device_group) | **POST** /sigfox_devices/{device_id}/set_group | Set Group of Sigfox device.
[**terminate_sigfox_device**](SigfoxDeviceApi.md#terminate_sigfox_device) | **POST** /sigfox_devices/{device_id}/terminate | Terminate Sigfox device.
[**unset_sigfox_device_group**](SigfoxDeviceApi.md#unset_sigfox_device_group) | **POST** /sigfox_devices/{device_id}/unset_group | Unset Group of Sigfox device.


# **delete_sigfox_device_tag**
> delete_sigfox_device_tag(device_id, tag_name)

Delete Sigfox device Tag.

Deletes a tag from the specified Sigfox device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    device_id = "device_id_example" # str | device ID of the target Sigfox device.
    tag_name = "tag_name_example" # str | Tag name to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().)

    # example passing only required values which don't have defaults set
    try:
        # Delete Sigfox device Tag.
        api_instance.delete_sigfox_device_tag(device_id, tag_name)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->delete_sigfox_device_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| device ID of the target Sigfox device. |
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
**404** | The specified Sigfox device or the tag does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_termination_on_sigfox_device**
> SigfoxDevice disable_termination_on_sigfox_device(device_id)

Disable Termination of Sigfox device.

Disables termination of specified Sigfox device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
from soracom_api.model.sigfox_device import SigfoxDevice
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target Sigfox device.

    # example passing only required values which don't have defaults set
    try:
        # Disable Termination of Sigfox device.
        api_response = api_instance.disable_termination_on_sigfox_device(device_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->disable_termination_on_sigfox_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target Sigfox device. |

### Return type

[**SigfoxDevice**](SigfoxDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Sigfox device&#39;s detailed information after the update. |  -  |
**404** | The specified Sigfox device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_termination_on_sigfox_device**
> SigfoxDevice enable_termination_on_sigfox_device(device_id)

Enable Termination of Sigfox device.

Enables termination of specified Sigfox device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
from soracom_api.model.sigfox_device import SigfoxDevice
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target Sigfox device.

    # example passing only required values which don't have defaults set
    try:
        # Enable Termination of Sigfox device.
        api_response = api_instance.enable_termination_on_sigfox_device(device_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->enable_termination_on_sigfox_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target Sigfox device. |

### Return type

[**SigfoxDevice**](SigfoxDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Sigfox device&#39;s detailed information after the update. |  -  |
**404** | The specified Sigfox device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_from_sigfox_device**
> [DataEntry] get_data_from_sigfox_device(device_id)

Get data sent from a Sigfox device.

Returns a list of data entries sent from a Sigfox device that match certain criteria. If the total number of entries does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
from soracom_api.model.data_entry import DataEntry
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target subscriber that generated data entries.
    _from = 1 # int | Start time for the data entries search range (unixtime in milliseconds). (optional)
    to = 1 # int | End time for the data entries search range (unixtime in milliseconds). (optional)
    sort = "desc" # str | Sort order of the data entries. Either descending (latest data entry first) or ascending (oldest data entry first). (optional) if omitted the server will use the default value of "desc"
    limit = 1 # int | Maximum number of data entries to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The value of `time` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get data sent from a Sigfox device.
        api_response = api_instance.get_data_from_sigfox_device(device_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->get_data_from_sigfox_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data sent from a Sigfox device.
        api_response = api_instance.get_data_from_sigfox_device(device_id, _from=_from, to=to, sort=sort, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->get_data_from_sigfox_device: %s\n" % e)
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

# **get_sigfox_device**
> SigfoxDevice get_sigfox_device(device_id)

Get Sigfox device.

Returns information about the specified Sigfox device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
from soracom_api.model.sigfox_device import SigfoxDevice
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target Sigfox device.

    # example passing only required values which don't have defaults set
    try:
        # Get Sigfox device.
        api_response = api_instance.get_sigfox_device(device_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->get_sigfox_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target Sigfox device. |

### Return type

[**SigfoxDevice**](SigfoxDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Sigfox device&#39;s detailed information. |  -  |
**404** | The specified Sigfox device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sigfox_devices**
> [SigfoxDevice] list_sigfox_devices()

List Sigfox devices.

Returns a list of Sigfox devices that match certain criteria. If the total number of Sigfox devices does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
from soracom_api.model.sigfox_device import SigfoxDevice
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    tag_name = "tag_name_example" # str | Tag name for filtering the search (exact match). (optional)
    tag_value = "tag_value_example" # str | Tag search string for filtering the search. Required when `tag_name` has been specified. (optional)
    tag_value_match_mode = "exact" # str | Tag match mode. (optional) if omitted the server will use the default value of "exact"
    limit = 1 # int | Maximum number of Sigfox devices to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The device ID of the last device retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next device onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Sigfox devices.
        api_response = api_instance.list_sigfox_devices(tag_name=tag_name, tag_value=tag_value, tag_value_match_mode=tag_value_match_mode, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->list_sigfox_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| Tag name for filtering the search (exact match). | [optional]
 **tag_value** | **str**| Tag search string for filtering the search. Required when &#x60;tag_name&#x60; has been specified. | [optional]
 **tag_value_match_mode** | **str**| Tag match mode. | [optional] if omitted the server will use the default value of "exact"
 **limit** | **int**| Maximum number of Sigfox devices to retrieve. | [optional]
 **last_evaluated_key** | **str**| The device ID of the last device retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next device onward. | [optional]

### Return type

[**[SigfoxDevice]**](SigfoxDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Sigfox devices. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sigfox_device_tags**
> SigfoxDevice put_sigfox_device_tags(device_id, tag_update_request)

Bulk Insert or Update Sigfox device Tags.

Inserts/updates tags for the specified Sigfox device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
from soracom_api.model.tag_update_request import TagUpdateRequest
from soracom_api.model.sigfox_device import SigfoxDevice
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target Sigfox device.
    tag_update_request = [
        TagUpdateRequest(
            tag_name="tag_name_example",
            tag_value="tag_value_example",
        ),
    ] # [TagUpdateRequest] | Array of tags to be inserted/updated.

    # example passing only required values which don't have defaults set
    try:
        # Bulk Insert or Update Sigfox device Tags.
        api_response = api_instance.put_sigfox_device_tags(device_id, tag_update_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->put_sigfox_device_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target Sigfox device. |
 **tag_update_request** | [**[TagUpdateRequest]**](TagUpdateRequest.md)| Array of tags to be inserted/updated. |

### Return type

[**SigfoxDevice**](SigfoxDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Sigfox device&#39;s detailed information after the update. |  -  |
**404** | The specified Sigfox device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_sigfox_device**
> SigfoxDevice register_sigfox_device(device_id, sigfox_registration_request)

Register a Sigfox device.

Registers a Sigfox device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
from soracom_api.model.sigfox_device import SigfoxDevice
from soracom_api.model.sigfox_registration_request import SigfoxRegistrationRequest
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target sigfox device to register
    sigfox_registration_request = SigfoxRegistrationRequest(
        registration_secret="registration_secret_example",
        tags={
            "key": "key_example",
        },
    ) # SigfoxRegistrationRequest | Sigfox device registration request

    # example passing only required values which don't have defaults set
    try:
        # Register a Sigfox device.
        api_response = api_instance.register_sigfox_device(device_id, sigfox_registration_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->register_sigfox_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target sigfox device to register |
 **sigfox_registration_request** | [**SigfoxRegistrationRequest**](SigfoxRegistrationRequest.md)| Sigfox device registration request |

### Return type

[**SigfoxDevice**](SigfoxDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sigfox device successfully registered |  -  |
**400** | PAC code is missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_data_to_sigfox_device**
> send_data_to_sigfox_device(device_id, sigfox_data)

Send data to a Sigfox device.

Sends data to the specified Sigfox device. The data will be stored until the device sends a next uplink message. If another message destined for the same Sigfox device ID is already waiting to be sent, the existing message will be discarded, and the new message will be sent instead.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
from soracom_api.model.sigfox_data import SigfoxData
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    device_id = "device_id_example" # str | ID of the recipient device.
    sigfox_data = SigfoxData(
        data="data_example",
    ) # SigfoxData | Binary data encoded as a hexadecimal string. Length of original binary data must be 8 octets (16 characters when encoded as a hexadecimal string).

    # example passing only required values which don't have defaults set
    try:
        # Send data to a Sigfox device.
        api_instance.send_data_to_sigfox_device(device_id, sigfox_data)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->send_data_to_sigfox_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| ID of the recipient device. |
 **sigfox_data** | [**SigfoxData**](SigfoxData.md)| Binary data encoded as a hexadecimal string. Length of original binary data must be 8 octets (16 characters when encoded as a hexadecimal string). |

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
**204** | Data has been received by server and waiting for the recipient device to retrieve. |  -  |
**404** | No such device found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_sigfox_device_group**
> SigfoxDevice set_sigfox_device_group(device_id, group)

Set Group of Sigfox device.

Sets or overwrites a group for the specified Sigfox device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
from soracom_api.model.sigfox_device import SigfoxDevice
from soracom_api.model.group import Group
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target Sigfox device.
    group = Group(
        configuration={},
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
        # Set Group of Sigfox device.
        api_response = api_instance.set_sigfox_device_group(device_id, group)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->set_sigfox_device_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target Sigfox device. |
 **group** | [**Group**](Group.md)| Group (may include ID only). |

### Return type

[**SigfoxDevice**](SigfoxDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Sigfox device&#39;s detailed information after the update. |  -  |
**404** | The specified Sigfox device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_sigfox_device**
> SigfoxDevice terminate_sigfox_device(device_id)

Terminate Sigfox device.

Terminates the specified Sigfox device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
from soracom_api.model.sigfox_device import SigfoxDevice
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target Sigfox device.
    delete_immediately = False # bool | If the Sigfox device is deleted immediately (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Terminate Sigfox device.
        api_response = api_instance.terminate_sigfox_device(device_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->terminate_sigfox_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Terminate Sigfox device.
        api_response = api_instance.terminate_sigfox_device(device_id, delete_immediately=delete_immediately)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->terminate_sigfox_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target Sigfox device. |
 **delete_immediately** | **bool**| If the Sigfox device is deleted immediately | [optional] if omitted the server will use the default value of False

### Return type

[**SigfoxDevice**](SigfoxDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Sigfox device&#39;s detailed information after the update. |  -  |
**404** | The specified Sigfox device does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_sigfox_device_group**
> SigfoxDevice unset_sigfox_device_group(device_id)

Unset Group of Sigfox device.

Removes the group configuration from the specified Sigfox device.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sigfox_device_api
from soracom_api.model.sigfox_device import SigfoxDevice
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
    api_instance = sigfox_device_api.SigfoxDeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target Sigfox device.

    # example passing only required values which don't have defaults set
    try:
        # Unset Group of Sigfox device.
        api_response = api_instance.unset_sigfox_device_group(device_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SigfoxDeviceApi->unset_sigfox_device_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID of the target Sigfox device. |

### Return type

[**SigfoxDevice**](SigfoxDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Sigfox device&#39;s detailed information after the update. |  -  |
**404** | The specified Sigfox device does not exist or the Sigfox device does not belong to a group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

