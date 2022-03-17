# api.DeviceApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device**](DeviceApi.md#create_device) | **POST** /devices | Creates a new Device
[**delete_device**](DeviceApi.md#delete_device) | **DELETE** /devices/{device_id} | Delete Device
[**delete_device_tag**](DeviceApi.md#delete_device_tag) | **DELETE** /devices/{device_id}/tags/{tag_name} | Delete device tag
[**execute_device_resource**](DeviceApi.md#execute_device_resource) | **POST** /devices/{device_id}/{object}/{instance}/{resource}/execute | Executes a resource of a device
[**get_data_from_device**](DeviceApi.md#get_data_from_device) | **GET** /devices/{device_id}/data | Get data sent from a device.
[**get_device**](DeviceApi.md#get_device) | **GET** /devices/{device_id} | Returns a Device identified by device ID
[**list_devices**](DeviceApi.md#list_devices) | **GET** /devices | Returns a list of Devices
[**observe_device_resource**](DeviceApi.md#observe_device_resource) | **POST** /devices/{device_id}/{object}/{instance}/{resource}/observe | Triggers observation of the specified resource of a device
[**observe_device_resources**](DeviceApi.md#observe_device_resources) | **POST** /devices/{device_id}/{object}/{instance}/observe | Triggers observation of resources under an object instance of a device
[**put_device_tags**](DeviceApi.md#put_device_tags) | **PUT** /devices/{device_id}/tags | Updates device tags
[**read_device_resource**](DeviceApi.md#read_device_resource) | **GET** /devices/{device_id}/{object}/{instance}/{resource} | Get the specified resource of a device
[**read_device_resources**](DeviceApi.md#read_device_resources) | **GET** /devices/{device_id}/{object}/{instance} | Get resources under an object instance of a device
[**set_device_group**](DeviceApi.md#set_device_group) | **POST** /devices/{device_id}/set_group | Lets a device join a group
[**unobserve_device_resource**](DeviceApi.md#unobserve_device_resource) | **POST** /devices/{device_id}/{object}/{instance}/{resource}/unobserve | Stops observation of a resource of a device
[**unobserve_device_resources**](DeviceApi.md#unobserve_device_resources) | **POST** /devices/{device_id}/{object}/{instance}/unobserve | Stops observation of resources under an object instance of a device
[**unset_device_group**](DeviceApi.md#unset_device_group) | **POST** /devices/{device_id}/unset_group | Lets a device leave from a group
[**write_device_resource**](DeviceApi.md#write_device_resource) | **PUT** /devices/{device_id}/{object}/{instance}/{resource} | Write value to a resource of a device


# **create_device**
> Device create_device(device)

Creates a new Device

Creates a new Device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
from api.model.device import Device
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
    api_instance = device_api.DeviceApi(api_client)
    device = Device(
        device_id="device_id_example",
        endpoint="endpoint_example",
        firmware_version="firmware_version_example",
        group_id="group_id_example",
        ip_address="ip_address_example",
        last_modified_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        last_registration_update=dateutil_parser('1970-01-01T00:00:00.00Z'),
        manufacturer="manufacturer_example",
        model_number="model_number_example",
        objects={},
        online=False,
        operator_id="operator_id_example",
        registration_id="registration_id_example",
        registration_life_time=1,
        serial_number="serial_number_example",
        tags={
            "key": "key_example",
        },
    ) # Device | Device to create

    # example passing only required values which don't have defaults set
    try:
        # Creates a new Device
        api_response = api_instance.create_device(device)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->create_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device** | [**Device**](Device.md)| Device to create |

### Return type

[**Device**](Device.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Device created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device**
> delete_device(device_id)

Delete Device

Delete Device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Device to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete Device
        api_instance.delete_device(device_id)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->delete_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device to delete |

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
**204** | Device deleted |  -  |
**404** | No such device found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_tag**
> delete_device_tag(device_id, tag_name)

Delete device tag

Delete device tag

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Device to update
    tag_name = "tag_name_example" # str | Name of tag to delete

    # example passing only required values which don't have defaults set
    try:
        # Delete device tag
        api_instance.delete_device_tag(device_id, tag_name)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->delete_device_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device to update |
 **tag_name** | **str**| Name of tag to delete |

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
**204** | Device tag deleted |  -  |
**404** | No such device or tag found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_device_resource**
> execute_device_resource(device_id, object, instance, resource)

Executes a resource of a device

Executes a resource of a device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
from api.model.inline_object1 import InlineObject1
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Target device
    object = "object_example" # str | Object ID
    instance = "instance_example" # str | Instance ID
    resource = "resource_example" # str | Resource ID
    inline_object1 = InlineObject1(
        value="value_example",
    ) # InlineObject1 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Executes a resource of a device
        api_instance.execute_device_resource(device_id, object, instance, resource)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->execute_device_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Executes a resource of a device
        api_instance.execute_device_resource(device_id, object, instance, resource, inline_object1=inline_object1)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->execute_device_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device |
 **object** | **str**| Object ID |
 **instance** | **str**| Instance ID |
 **resource** | **str**| Resource ID |
 **inline_object1** | [**InlineObject1**](InlineObject1.md)|  | [optional]

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
**202** | Execution request is accepted |  -  |
**400** | Resource is not executable |  -  |
**404** | Resource is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_from_device**
> [DataEntry] get_data_from_device(device_id)

Get data sent from a device.

Returns a list of data entries sent from a device that match certain criteria. If the total number of entries does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID of the target subscriber that generated data entries.
    _from = 1 # int | Start time for the data entries search range (unixtime in milliseconds). (optional)
    to = 1 # int | End time for the data entries search range (unixtime in milliseconds). (optional)
    sort = "desc" # str | Sort order of the data entries. Either descending (latest data entry first) or ascending (oldest data entry first). (optional) if omitted the server will use the default value of "desc"
    limit = 1 # int | Maximum number of data entries to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The value of `time` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get data sent from a device.
        api_response = api_instance.get_data_from_device(device_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->get_data_from_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data sent from a device.
        api_response = api_instance.get_data_from_device(device_id, _from=_from, to=to, sort=sort, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->get_data_from_device: %s\n" % e)
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

# **get_device**
> Device get_device(device_id)

Returns a Device identified by device ID

Returns a Device identified by device ID

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
from api.model.device import Device
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Device ID
    model = False # bool | Whether or not to add model information (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Returns a Device identified by device ID
        api_response = api_instance.get_device(device_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->get_device: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a Device identified by device ID
        api_response = api_instance.get_device(device_id, model=model)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->get_device: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device ID |
 **model** | **bool**| Whether or not to add model information | [optional] if omitted the server will use the default value of False

### Return type

[**Device**](Device.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Device identified by device ID |  -  |
**404** | No such device found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_devices**
> [Device] list_devices()

Returns a list of Devices

Returns a list of Devices

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
from api.model.device import Device
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
    api_instance = device_api.DeviceApi(api_client)
    tag_name = "tag_name_example" # str | Tag name (optional)
    tag_value = "tag_value_example" # str | Tag value (optional)
    tag_value_match_mode = "tag_value_match_mode_example" # str | Tag value match mode (exact | prefix) (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | ID of the last Device in the previous page (optional)
    limit = -1 # int | Max number of Devices in a response (optional) if omitted the server will use the default value of -1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of Devices
        api_response = api_instance.list_devices(tag_name=tag_name, tag_value=tag_value, tag_value_match_mode=tag_value_match_mode, last_evaluated_key=last_evaluated_key, limit=limit)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->list_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| Tag name | [optional]
 **tag_value** | **str**| Tag value | [optional]
 **tag_value_match_mode** | **str**| Tag value match mode (exact | prefix) | [optional]
 **last_evaluated_key** | **str**| ID of the last Device in the previous page | [optional]
 **limit** | **int**| Max number of Devices in a response | [optional] if omitted the server will use the default value of -1

### Return type

[**[Device]**](Device.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of Devices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observe_device_resource**
> observe_device_resource(device_id, object, instance, resource)

Triggers observation of the specified resource of a device

Triggers observation of the specified resource of a device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Target device
    object = "object_example" # str | Object ID
    instance = "instance_example" # str | Instance ID
    resource = "resource_example" # str | Resource ID
    model = False # bool | Whether or not to add model information (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Triggers observation of the specified resource of a device
        api_instance.observe_device_resource(device_id, object, instance, resource)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->observe_device_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Triggers observation of the specified resource of a device
        api_instance.observe_device_resource(device_id, object, instance, resource, model=model)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->observe_device_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device |
 **object** | **str**| Object ID |
 **instance** | **str**| Instance ID |
 **resource** | **str**| Resource ID |
 **model** | **bool**| Whether or not to add model information | [optional] if omitted the server will use the default value of False

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
**202** | Observation started. |  -  |
**400** | Resource is not readable |  -  |
**404** | Resource is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **observe_device_resources**
> observe_device_resources(device_id, object, instance)

Triggers observation of resources under an object instance of a device

Triggers observation of resources under an object instance of a device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Target device
    object = "object_example" # str | Object ID
    instance = "instance_example" # str | Instance ID
    model = False # bool | Whether or not to add model information (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Triggers observation of resources under an object instance of a device
        api_instance.observe_device_resources(device_id, object, instance)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->observe_device_resources: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Triggers observation of resources under an object instance of a device
        api_instance.observe_device_resources(device_id, object, instance, model=model)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->observe_device_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device |
 **object** | **str**| Object ID |
 **instance** | **str**| Instance ID |
 **model** | **bool**| Whether or not to add model information | [optional] if omitted the server will use the default value of False

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
**202** | Observation started. |  -  |
**400** | Resource is not readable |  -  |
**404** | Resource is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_device_tags**
> Device put_device_tags(device_id, tag_update_request)

Updates device tags

Updates device tags

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
from api.model.tag_update_request import TagUpdateRequest
from api.model.device import Device
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Device to update
    tag_update_request = [
        TagUpdateRequest(
            tag_name="tag_name_example",
            tag_value="tag_value_example",
        ),
    ] # [TagUpdateRequest] | Array of values for tags to be updated.

    # example passing only required values which don't have defaults set
    try:
        # Updates device tags
        api_response = api_instance.put_device_tags(device_id, tag_update_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->put_device_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device to update |
 **tag_update_request** | [**[TagUpdateRequest]**](TagUpdateRequest.md)| Array of values for tags to be updated. |

### Return type

[**Device**](Device.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Device updated |  -  |
**404** | No such device found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_device_resource**
> ResourceInstance read_device_resource(device_id, object, instance, resource)

Get the specified resource of a device

Get the specified resource of a device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
from api.model.resource_instance import ResourceInstance
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Target device
    object = "object_example" # str | Object ID
    instance = "instance_example" # str | Instance ID
    resource = "resource_example" # str | Resource ID
    model = False # bool | Whether or not to add model information (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get the specified resource of a device
        api_response = api_instance.read_device_resource(device_id, object, instance, resource)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->read_device_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get the specified resource of a device
        api_response = api_instance.read_device_resource(device_id, object, instance, resource, model=model)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->read_device_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device |
 **object** | **str**| Object ID |
 **instance** | **str**| Instance ID |
 **resource** | **str**| Resource ID |
 **model** | **bool**| Whether or not to add model information | [optional] if omitted the server will use the default value of False

### Return type

[**ResourceInstance**](ResourceInstance.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resource |  -  |
**400** | Resource is not readable |  -  |
**404** | Resource is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_device_resources**
> ObjectInstance read_device_resources(device_id, object, instance)

Get resources under an object instance of a device

Get resources under an object instance of a device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
from api.model.object_instance import ObjectInstance
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Target device
    object = "object_example" # str | Object ID
    instance = "instance_example" # str | Instance ID
    model = False # bool | Whether or not to add model information (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Get resources under an object instance of a device
        api_response = api_instance.read_device_resources(device_id, object, instance)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->read_device_resources: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get resources under an object instance of a device
        api_response = api_instance.read_device_resources(device_id, object, instance, model=model)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->read_device_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device |
 **object** | **str**| Object ID |
 **instance** | **str**| Instance ID |
 **model** | **bool**| Whether or not to add model information | [optional] if omitted the server will use the default value of False

### Return type

[**ObjectInstance**](ObjectInstance.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Resources under the specified object instance |  -  |
**400** | Object instance is not readable |  -  |
**404** | Object instance is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_device_group**
> Device set_device_group(device_id)

Lets a device join a group

Lets a device join a group

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
from api.model.inline_object2 import InlineObject2
from api.model.device import Device
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Device to update
    inline_object2 = InlineObject2(
        group_id="group_id_example",
    ) # InlineObject2 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Lets a device join a group
        api_response = api_instance.set_device_group(device_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->set_device_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Lets a device join a group
        api_response = api_instance.set_device_group(device_id, inline_object2=inline_object2)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->set_device_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device to update |
 **inline_object2** | [**InlineObject2**](InlineObject2.md)|  | [optional]

### Return type

[**Device**](Device.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Device updated |  -  |
**404** | No such device found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unobserve_device_resource**
> unobserve_device_resource(device_id, object, instance, resource)

Stops observation of a resource of a device

Stops observation of a resource of a device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Target device
    object = "object_example" # str | Object ID
    instance = "instance_example" # str | Instance ID
    resource = "resource_example" # str | Resource ID

    # example passing only required values which don't have defaults set
    try:
        # Stops observation of a resource of a device
        api_instance.unobserve_device_resource(device_id, object, instance, resource)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->unobserve_device_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device |
 **object** | **str**| Object ID |
 **instance** | **str**| Instance ID |
 **resource** | **str**| Resource ID |

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
**204** | Observation cancelled |  -  |
**404** | Resource is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unobserve_device_resources**
> unobserve_device_resources(device_id, object, instance)

Stops observation of resources under an object instance of a device

Stops observation of resources under an object instance of a device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Target device
    object = "object_example" # str | Object ID
    instance = "instance_example" # str | Instance ID

    # example passing only required values which don't have defaults set
    try:
        # Stops observation of resources under an object instance of a device
        api_instance.unobserve_device_resources(device_id, object, instance)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->unobserve_device_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device |
 **object** | **str**| Object ID |
 **instance** | **str**| Instance ID |

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
**204** | Observation cancelled |  -  |
**404** | Resource is not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_device_group**
> Device unset_device_group(device_id)

Lets a device leave from a group

Lets a device leave from a group

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
from api.model.device import Device
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Device to update

    # example passing only required values which don't have defaults set
    try:
        # Lets a device leave from a group
        api_response = api_instance.unset_device_group(device_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->unset_device_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Device to update |

### Return type

[**Device**](Device.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Device updated |  -  |
**404** | No such device found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **write_device_resource**
> write_device_resource(device_id, object, instance, resource, inline_object)

Write value to a resource of a device

Write value to a resource of a device

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_api
from api.model.inline_object import InlineObject
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
    api_instance = device_api.DeviceApi(api_client)
    device_id = "device_id_example" # str | Target device
    object = "object_example" # str | Object ID
    instance = "instance_example" # str | Instance ID
    resource = "resource_example" # str | Resource ID
    inline_object = InlineObject(
        value="value_example",
    ) # InlineObject | 

    # example passing only required values which don't have defaults set
    try:
        # Write value to a resource of a device
        api_instance.write_device_resource(device_id, object, instance, resource, inline_object)
    except api.ApiException as e:
        print("Exception when calling DeviceApi->write_device_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_id** | **str**| Target device |
 **object** | **str**| Object ID |
 **instance** | **str**| Instance ID |
 **resource** | **str**| Resource ID |
 **inline_object** | [**InlineObject**](InlineObject.md)|  |

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
**202** | Updating resource is accepted |  -  |
**400** | Specified Resource does not support write (Including case of connection error such as offline device) |  -  |
**404** | Resource is not found |  -  |
**500** | Error response from the device. (It includes the case where the LwM2M response message is error from the device, and the error message from the device is included in the response &#39;message&#39;.) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

