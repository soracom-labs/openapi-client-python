# soracom_api.SystemNotificationApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_system_notification**](SystemNotificationApi.md#delete_system_notification) | **DELETE** /operators/{operator_id}/system_notifications/{type} | Delete system notification
[**get_system_notification**](SystemNotificationApi.md#get_system_notification) | **GET** /operators/{operator_id}/system_notifications/{type} | Get system notification
[**list_system_notifications**](SystemNotificationApi.md#list_system_notifications) | **GET** /operators/{operator_id}/system_notifications | List system notifications
[**set_system_notification**](SystemNotificationApi.md#set_system_notification) | **POST** /operators/{operator_id}/system_notifications/{type} | Set system notification


# **delete_system_notification**
> delete_system_notification(operator_id, type)

Delete system notification

Deletes a system notification.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import system_notification_api
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
    api_instance = system_notification_api.SystemNotificationApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    type = "recovery" # str | system notification type

    # example passing only required values which don't have defaults set
    try:
        # Delete system notification
        api_instance.delete_system_notification(operator_id, type)
    except soracom_api.ApiException as e:
        print("Exception when calling SystemNotificationApi->delete_system_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **type** | **str**| system notification type |

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
**204** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_notification**
> SystemNotificationsModel get_system_notification(operator_id, type)

Get system notification

Returns a system notification.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import system_notification_api
from soracom_api.model.system_notifications_model import SystemNotificationsModel
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
    api_instance = system_notification_api.SystemNotificationApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    type = "primary" # str | system notification type

    # example passing only required values which don't have defaults set
    try:
        # Get system notification
        api_response = api_instance.get_system_notification(operator_id, type)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SystemNotificationApi->get_system_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **type** | **str**| system notification type |

### Return type

[**SystemNotificationsModel**](SystemNotificationsModel.md)

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

# **list_system_notifications**
> [SystemNotificationsModel] list_system_notifications(operator_id)

List system notifications

Returns a list of system notifications.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import system_notification_api
from soracom_api.model.system_notifications_model import SystemNotificationsModel
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
    api_instance = system_notification_api.SystemNotificationApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # List system notifications
        api_response = api_instance.list_system_notifications(operator_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SystemNotificationApi->list_system_notifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

### Return type

[**[SystemNotificationsModel]**](SystemNotificationsModel.md)

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

# **set_system_notification**
> SystemNotificationsModel set_system_notification(operator_id, type, set_system_notifications_request)

Set system notification

Sets a system notification.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import system_notification_api
from soracom_api.model.set_system_notifications_request import SetSystemNotificationsRequest
from soracom_api.model.system_notifications_model import SystemNotificationsModel
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
    api_instance = system_notification_api.SystemNotificationApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    type = "primary" # str | system notification type
    set_system_notifications_request = SetSystemNotificationsRequest(
        email_id_list=[
            "email_id_list_example",
        ],
        password="password_example",
    ) # SetSystemNotificationsRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Set system notification
        api_response = api_instance.set_system_notification(operator_id, type, set_system_notifications_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SystemNotificationApi->set_system_notification: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **type** | **str**| system notification type |
 **set_system_notifications_request** | [**SetSystemNotificationsRequest**](SetSystemNotificationsRequest.md)| request |

### Return type

[**SystemNotificationsModel**](SystemNotificationsModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

