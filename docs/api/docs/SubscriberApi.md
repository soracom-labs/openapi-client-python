# soracom_api.SubscriberApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_subscriber**](SubscriberApi.md#activate_subscriber) | **POST** /subscribers/{imsi}/activate | Activate Subscriber.
[**deactivate_subscriber**](SubscriberApi.md#deactivate_subscriber) | **POST** /subscribers/{imsi}/deactivate | Deactivate Subscriber.
[**delete_subscriber_session**](SubscriberApi.md#delete_subscriber_session) | **POST** /subscribers/{imsi}/delete_session | Delete Session
[**delete_subscriber_tag**](SubscriberApi.md#delete_subscriber_tag) | **DELETE** /subscribers/{imsi}/tags/{tag_name} | Delete Subscriber Tag.
[**delete_subscriber_transfer_token**](SubscriberApi.md#delete_subscriber_transfer_token) | **DELETE** /subscribers/transfer_token/{token} | Delete Subscribers Transfer Token.
[**disable_termination**](SubscriberApi.md#disable_termination) | **POST** /subscribers/{imsi}/disable_termination | Disable Termination of Subscriber.
[**enable_termination**](SubscriberApi.md#enable_termination) | **POST** /subscribers/{imsi}/enable_termination | Enable Termination of Subscriber.
[**export_subscribers**](SubscriberApi.md#export_subscribers) | **POST** /subscribers/export | Export all subscribers.
[**get_data_from_subscriber**](SubscriberApi.md#get_data_from_subscriber) | **GET** /subscribers/{imsi}/data | Get data sent from a subscriber.
[**get_subscriber**](SubscriberApi.md#get_subscriber) | **GET** /subscribers/{imsi} | Get Subscriber.
[**issue_subscriber_transfer_token**](SubscriberApi.md#issue_subscriber_transfer_token) | **POST** /subscribers/transfer_token/issue | Issue Subscribers Transfer Token.
[**list_session_events**](SubscriberApi.md#list_session_events) | **GET** /subscribers/{imsi}/events/sessions | List Session Events.
[**list_subscribers**](SubscriberApi.md#list_subscribers) | **GET** /subscribers | List Subscribers.
[**put_bundles**](SubscriberApi.md#put_bundles) | **PUT** /subscribers/{imsi}/bundles | Set Bundles to Subscriber.
[**put_subscriber_tags**](SubscriberApi.md#put_subscriber_tags) | **PUT** /subscribers/{imsi}/tags | Bulk Insert or Update Subscriber Tags.
[**register_subscriber**](SubscriberApi.md#register_subscriber) | **POST** /subscribers/{imsi}/register | Register Subscriber.
[**report_local_info**](SubscriberApi.md#report_local_info) | **POST** /subscribers/{imsi}/report_local_info | Triggers Subscriber to report SIM local info.
[**send_sms**](SubscriberApi.md#send_sms) | **POST** /subscribers/{imsi}/send_sms | Send SMS to Subscriber
[**send_sms_by_msisdn**](SubscriberApi.md#send_sms_by_msisdn) | **POST** /subscribers/msisdn/{msisdn}/send_sms | Send SMS to Subscriber by MSISDN
[**send_subscriber_downlink_ping**](SubscriberApi.md#send_subscriber_downlink_ping) | **POST** /subscribers/{imsi}/downlink/ping | Send ping requests to a subscriber.
[**set_expiry_time**](SubscriberApi.md#set_expiry_time) | **POST** /subscribers/{imsi}/set_expiry_time | Update Expiry Time of Subscriber.
[**set_group**](SubscriberApi.md#set_group) | **POST** /subscribers/{imsi}/set_group | Set Group to Subscriber.
[**set_imei_lock**](SubscriberApi.md#set_imei_lock) | **POST** /subscribers/{imsi}/set_imei_lock | Set IMEI lock configuration for Subscriber.
[**set_subscriber_to_standby**](SubscriberApi.md#set_subscriber_to_standby) | **POST** /subscribers/{imsi}/set_to_standby | Set Subscriber to standby mode.
[**suspend_subscriber**](SubscriberApi.md#suspend_subscriber) | **POST** /subscribers/{imsi}/suspend | Suspend Subscriber.
[**terminate_subscriber**](SubscriberApi.md#terminate_subscriber) | **POST** /subscribers/{imsi}/terminate | Terminate Subscriber.
[**unset_expiry_time**](SubscriberApi.md#unset_expiry_time) | **POST** /subscribers/{imsi}/unset_expiry_time | Delete Expiry Time of Subscriber.
[**unset_group**](SubscriberApi.md#unset_group) | **POST** /subscribers/{imsi}/unset_group | Unset Group to Subscriber.
[**unset_imei_lock**](SubscriberApi.md#unset_imei_lock) | **POST** /subscribers/{imsi}/unset_imei_lock | Unset IMEI lock configuration for Subscriber.
[**update_speed_class**](SubscriberApi.md#update_speed_class) | **POST** /subscribers/{imsi}/update_speed_class | Update Subscriber speed class.
[**verify_subscriber_transfer_token**](SubscriberApi.md#verify_subscriber_transfer_token) | **POST** /subscribers/transfer_token/verify | Verify Subscriber Transfer Token.


# **activate_subscriber**
> Subscriber activate_subscriber(imsi)

Activate Subscriber.

Activates status of specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Activate Subscriber.
        api_response = api_instance.activate_subscriber(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->activate_subscriber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_subscriber**
> Subscriber deactivate_subscriber(imsi)

Deactivate Subscriber.

Deactivates specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Deactivate Subscriber.
        api_response = api_instance.deactivate_subscriber(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->deactivate_subscriber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscriber_session**
> Subscriber delete_subscriber_session(imsi)

Delete Session

Deletes session for the specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Delete Session
        api_response = api_instance.delete_subscriber_session(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->delete_subscriber_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscriber_tag**
> delete_subscriber_tag(imsi, tag_name)

Delete Subscriber Tag.

Deletes a tag from the specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.
    tag_name = "tag_name_example" # str | Tag name to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().)

    # example passing only required values which don't have defaults set
    try:
        # Delete Subscriber Tag.
        api_instance.delete_subscriber_tag(imsi, tag_name)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->delete_subscriber_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |
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
**404** | The specified subscriber or the tag does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscriber_transfer_token**
> delete_subscriber_transfer_token(token)

Delete Subscribers Transfer Token.

Deletes the subscriber's inter-operator control transfer token, and cancels the control transfer.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    token = "token_example" # str | token

    # example passing only required values which don't have defaults set
    try:
        # Delete Subscribers Transfer Token.
        api_instance.delete_subscriber_transfer_token(token)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->delete_subscriber_transfer_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token |

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
**204** | Deletion implemented. |  -  |
**404** | The token does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_termination**
> Subscriber disable_termination(imsi)

Disable Termination of Subscriber.

Disables termination of specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Disable Termination of Subscriber.
        api_response = api_instance.disable_termination(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->disable_termination: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_termination**
> Subscriber enable_termination(imsi)

Enable Termination of Subscriber.

Enables termination of specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Enable Termination of Subscriber.
        api_response = api_instance.enable_termination(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->enable_termination: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_subscribers**
> FileExportResponse export_subscribers()

Export all subscribers.

Export all subscribers as a CSV file.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.file_export_response import FileExportResponse
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    export_mode = "sync" # str | export mode (async, sync) (optional) if omitted the server will use the default value of "sync"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export all subscribers.
        api_response = api_instance.export_subscribers(export_mode=export_mode)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->export_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_mode** | **str**| export mode (async, sync) | [optional] if omitted the server will use the default value of "sync"

### Return type

[**FileExportResponse**](FileExportResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Where to export subscribers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_from_subscriber**
> [DataEntry] get_data_from_subscriber(imsi)

Get data sent from a subscriber.

Returns a list of data entries sent from a subscriber that match certain criteria. If the total number of entries does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber that generated data entries.
    _from = 1 # int | Start time for the data entries search range (unixtime in milliseconds). (optional)
    to = 1 # int | End time for the data entries search range (unixtime in milliseconds). (optional)
    sort = "desc" # str | Sort order of the data entries. Either descending (latest data entry first) or ascending (oldest data entry first). (optional) if omitted the server will use the default value of "desc"
    limit = 1 # int | Maximum number of data entries to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The value of `time` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get data sent from a subscriber.
        api_response = api_instance.get_data_from_subscriber(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->get_data_from_subscriber: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data sent from a subscriber.
        api_response = api_instance.get_data_from_subscriber(imsi, _from=_from, to=to, sort=sort, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->get_data_from_subscriber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber that generated data entries. |
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

# **get_subscriber**
> Subscriber get_subscriber(imsi)

Get Subscriber.

Returns information about the specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Get Subscriber.
        api_response = api_instance.get_subscriber(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->get_subscriber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_subscriber_transfer_token**
> IssueSubscriberTransferTokenResponse issue_subscriber_transfer_token(issue_subscriber_transfer_token_request)

Issue Subscribers Transfer Token.

Sends the subscriber's inter-operator control transfer token to the control destination operator.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.issue_subscriber_transfer_token_request import IssueSubscriberTransferTokenRequest
from soracom_api.model.issue_subscriber_transfer_token_response import IssueSubscriberTransferTokenResponse
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    issue_subscriber_transfer_token_request = IssueSubscriberTransferTokenRequest(
        transfer_destination_operator_email="transfer_destination_operator_email_example",
        transfer_destination_operator_id="transfer_destination_operator_id_example",
        transfer_imsi=[
            "transfer_imsi_example",
        ],
    ) # IssueSubscriberTransferTokenRequest | Destination operator's email address, Operator ID, transferring IMSI

    # example passing only required values which don't have defaults set
    try:
        # Issue Subscribers Transfer Token.
        api_response = api_instance.issue_subscriber_transfer_token(issue_subscriber_transfer_token_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->issue_subscriber_transfer_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_subscriber_transfer_token_request** | [**IssueSubscriberTransferTokenRequest**](IssueSubscriberTransferTokenRequest.md)| Destination operator&#39;s email address, Operator ID, transferring IMSI |

### Return type

[**IssueSubscriberTransferTokenResponse**](IssueSubscriberTransferTokenResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_session_events**
> [SessionEvent] list_session_events(imsi)

List Session Events.

Returns the event history for the specified subscriber, including session creation, change, and deletion. If the total number of events does not fit in one page, a URL for accessing the next page is returned in the `Link` header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.session_event import SessionEvent
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.
    _from = 1 # int | Start time for the events search range (unixtime). (optional)
    to = 1 # int | End time for the events search range (unixtime). (optional)
    limit = 1 # int | Maximum number of events to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The time stamp of the last event retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next event onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Session Events.
        api_response = api_instance.list_session_events(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->list_session_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Session Events.
        api_response = api_instance.list_session_events(imsi, _from=_from, to=to, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->list_session_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |
 **_from** | **int**| Start time for the events search range (unixtime). | [optional]
 **to** | **int**| End time for the events search range (unixtime). | [optional]
 **limit** | **int**| Maximum number of events to retrieve. | [optional]
 **last_evaluated_key** | **str**| The time stamp of the last event retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next event onward. | [optional]

### Return type

[**[SessionEvent]**](SessionEvent.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of session events |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscribers**
> [Subscriber] list_subscribers()

List Subscribers.

Returns a list of subscribers that match certain criteria. If the total number of subscribers does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    tag_name = "tag_name_example" # str | Tag name for filtering the search (exact match). (optional)
    tag_value = "tag_value_example" # str | Tag search string for filtering the search. Required when `tag_name` has been specified. (optional)
    tag_value_match_mode = "exact" # str | Tag match mode. (optional) if omitted the server will use the default value of "exact"
    status_filter = "status_filter_example" # str | Status for filtering the search. Can specify multiple values delimited by `|`. Valid values include: `active`, `inactive`, `ready`, `instock`, `shipped`, `suspended`, and `terminated`. (optional)
    speed_class_filter = "speed_class_filter_example" # str | Speed class for filtering the search. Can specify multiple values delimited by `|`. Valid values include: `s1.minimum`, `s1.slow`, `s1.standard`, `s1.fast` (optional)
    serial_number_filter = "serial_number_filter_example" # str | Serial number for filtering the search. Can specify multiple values delimited by `|`. Returns subscribers with serial number starting with the specified value(s). (optional)
    limit = 1 # int | Maximum number of subscribers to retrieve. Setting a limit does not guarantee the number of subscribers returned in the response (i.e. the response may contain fewer subscribers than the specified limit). (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The IMSI of the last subscriber retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next subscriber onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Subscribers.
        api_response = api_instance.list_subscribers(tag_name=tag_name, tag_value=tag_value, tag_value_match_mode=tag_value_match_mode, status_filter=status_filter, speed_class_filter=speed_class_filter, serial_number_filter=serial_number_filter, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->list_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| Tag name for filtering the search (exact match). | [optional]
 **tag_value** | **str**| Tag search string for filtering the search. Required when &#x60;tag_name&#x60; has been specified. | [optional]
 **tag_value_match_mode** | **str**| Tag match mode. | [optional] if omitted the server will use the default value of "exact"
 **status_filter** | **str**| Status for filtering the search. Can specify multiple values delimited by &#x60;|&#x60;. Valid values include: &#x60;active&#x60;, &#x60;inactive&#x60;, &#x60;ready&#x60;, &#x60;instock&#x60;, &#x60;shipped&#x60;, &#x60;suspended&#x60;, and &#x60;terminated&#x60;. | [optional]
 **speed_class_filter** | **str**| Speed class for filtering the search. Can specify multiple values delimited by &#x60;|&#x60;. Valid values include: &#x60;s1.minimum&#x60;, &#x60;s1.slow&#x60;, &#x60;s1.standard&#x60;, &#x60;s1.fast&#x60; | [optional]
 **serial_number_filter** | **str**| Serial number for filtering the search. Can specify multiple values delimited by &#x60;|&#x60;. Returns subscribers with serial number starting with the specified value(s). | [optional]
 **limit** | **int**| Maximum number of subscribers to retrieve. Setting a limit does not guarantee the number of subscribers returned in the response (i.e. the response may contain fewer subscribers than the specified limit). | [optional]
 **last_evaluated_key** | **str**| The IMSI of the last subscriber retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next subscriber onward. | [optional]

### Return type

[**[Subscriber]**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of subscribers. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_bundles**
> Subscriber put_bundles(imsi, request_body)

Set Bundles to Subscriber.

Sets bundles to the specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.
    request_body = [
        "request_body_example",
    ] # [str] | Array of bundles to be set.

    # example passing only required values which don't have defaults set
    try:
        # Set Bundles to Subscriber.
        api_response = api_instance.put_bundles(imsi, request_body)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->put_bundles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |
 **request_body** | **[str]**| Array of bundles to be set. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_subscriber_tags**
> Subscriber put_subscriber_tags(imsi, tag_update_request)

Bulk Insert or Update Subscriber Tags.

Inserts/updates tags for the specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.tag_update_request import TagUpdateRequest
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.
    tag_update_request = [
        TagUpdateRequest(
            tag_name="tag_name_example",
            tag_value="tag_value_example",
        ),
    ] # [TagUpdateRequest] | Array of tags to be inserted/updated.

    # example passing only required values which don't have defaults set
    try:
        # Bulk Insert or Update Subscriber Tags.
        api_response = api_instance.put_subscriber_tags(imsi, tag_update_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->put_subscriber_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |
 **tag_update_request** | [**[TagUpdateRequest]**](TagUpdateRequest.md)| Array of tags to be inserted/updated. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_subscriber**
> Subscriber register_subscriber(imsi, register_subscribers_request)

Register Subscriber.

Registers a subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
from soracom_api.model.register_subscribers_request import RegisterSubscribersRequest
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.
    register_subscribers_request = RegisterSubscribersRequest(
        group_id="group_id_example",
        registration_secret="registration_secret_example",
        tags=[
            TagUpdateRequest(
                tag_name="tag_name_example",
                tag_value="tag_value_example",
            ),
        ],
    ) # RegisterSubscribersRequest | subscriber

    # example passing only required values which don't have defaults set
    try:
        # Register Subscriber.
        api_response = api_instance.register_subscriber(imsi, register_subscribers_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->register_subscriber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |
 **register_subscribers_request** | [**RegisterSubscribersRequest**](RegisterSubscribersRequest.md)| subscriber |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Subscriber registration complete. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_local_info**
> Subscriber report_local_info(imsi)

Triggers Subscriber to report SIM local info.

Triggers Subscriber to report SIM local info.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Triggers Subscriber to report SIM local info.
        api_response = api_instance.report_local_info(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->report_local_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The local info reporting has successfully been triggered. The subscriber information is asynchronously updated when the SIM reports the information back. |  -  |
**400** | The specified subscriber does not support local info reporting feature. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms**
> SmsForwardingReport send_sms(imsi, sms_forwarding_request)

Send SMS to Subscriber

Send SMS to the specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.sms_forwarding_request import SmsForwardingRequest
from soracom_api.model.sms_forwarding_report import SmsForwardingReport
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.
    sms_forwarding_request = SmsForwardingRequest(
        encoding_type=2,
        payload="payload_example",
    ) # SmsForwardingRequest | SMS forwarding request that contains message body and its encoding type.

    # example passing only required values which don't have defaults set
    try:
        # Send SMS to Subscriber
        api_response = api_instance.send_sms(imsi, sms_forwarding_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->send_sms: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |
 **sms_forwarding_request** | [**SmsForwardingRequest**](SmsForwardingRequest.md)| SMS forwarding request that contains message body and its encoding type. |

### Return type

[**SmsForwardingReport**](SmsForwardingReport.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | SMS forwarding report containing message ID. |  -  |
**400** | The specified subscriber does not support SMS API. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms_by_msisdn**
> SmsForwardingReport send_sms_by_msisdn(msisdn, sms_forwarding_request)

Send SMS to Subscriber by MSISDN

Send SMS to a subscriber specified with MSISDN.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.sms_forwarding_request import SmsForwardingRequest
from soracom_api.model.sms_forwarding_report import SmsForwardingReport
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    msisdn = "msisdn_example" # str | MSISDN of the target subscriber.
    sms_forwarding_request = SmsForwardingRequest(
        encoding_type=2,
        payload="payload_example",
    ) # SmsForwardingRequest | SMS forwarding request that contains message body and its encoding type.

    # example passing only required values which don't have defaults set
    try:
        # Send SMS to Subscriber by MSISDN
        api_response = api_instance.send_sms_by_msisdn(msisdn, sms_forwarding_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->send_sms_by_msisdn: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msisdn** | **str**| MSISDN of the target subscriber. |
 **sms_forwarding_request** | [**SmsForwardingRequest**](SmsForwardingRequest.md)| SMS forwarding request that contains message body and its encoding type. |

### Return type

[**SmsForwardingReport**](SmsForwardingReport.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | SMS forwarding report containing message ID. |  -  |
**400** | The specified subscriber does not support SMS API. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_subscriber_downlink_ping**
> DownlinkPingResponse send_subscriber_downlink_ping(imsi, downlink_ping_request)

Send ping requests to a subscriber.

Send ICMP ping requests to a subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.downlink_ping_response import DownlinkPingResponse
from soracom_api.model.downlink_ping_request import DownlinkPingRequest
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.
    downlink_ping_request = DownlinkPingRequest(
        number_of_ping_requests=1,
        timeout_seconds=1,
    ) # DownlinkPingRequest | ping options

    # example passing only required values which don't have defaults set
    try:
        # Send ping requests to a subscriber.
        api_response = api_instance.send_subscriber_downlink_ping(imsi, downlink_ping_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->send_subscriber_downlink_ping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |
 **downlink_ping_request** | [**DownlinkPingRequest**](DownlinkPingRequest.md)| ping options |

### Return type

[**DownlinkPingResponse**](DownlinkPingResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of the ping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_expiry_time**
> Subscriber set_expiry_time(imsi, expiry_time)

Update Expiry Time of Subscriber.

Updates expiry time of specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
from soracom_api.model.expiry_time import ExpiryTime
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.
    expiry_time = ExpiryTime(
        expiry_action="doNothing",
        expiry_time=1,
    ) # ExpiryTime | Expiry time after the update (unixtime: in milliseconds).

    # example passing only required values which don't have defaults set
    try:
        # Update Expiry Time of Subscriber.
        api_response = api_instance.set_expiry_time(imsi, expiry_time)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->set_expiry_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |
 **expiry_time** | [**ExpiryTime**](ExpiryTime.md)| Expiry time after the update (unixtime: in milliseconds). |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_group**
> Subscriber set_group(imsi, set_group_request)

Set Group to Subscriber.

Sets or overwrites a group for the specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
from soracom_api.model.set_group_request import SetGroupRequest
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.
    set_group_request = SetGroupRequest(
        group_id="group_id_example",
        tags=TagSet(
            key="key_example",
        ),
    ) # SetGroupRequest | Group (may include ID only).

    # example passing only required values which don't have defaults set
    try:
        # Set Group to Subscriber.
        api_response = api_instance.set_group(imsi, set_group_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->set_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |
 **set_group_request** | [**SetGroupRequest**](SetGroupRequest.md)| Group (may include ID only). |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_imei_lock**
> Subscriber set_imei_lock(imsi)

Set IMEI lock configuration for Subscriber.

Set IMEI that the subscriber should be locked to.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.set_imei_lock_request import SetImeiLockRequest
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.
    set_imei_lock_request = SetImeiLockRequest(
        imei="imei_example",
    ) # SetImeiLockRequest | IMEI lock configuration for the subscriber. (IMEI can be left blank for locking to the current IMEI of an online subscriber.) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set IMEI lock configuration for Subscriber.
        api_response = api_instance.set_imei_lock(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->set_imei_lock: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set IMEI lock configuration for Subscriber.
        api_response = api_instance.set_imei_lock(imsi, set_imei_lock_request=set_imei_lock_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->set_imei_lock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |
 **set_imei_lock_request** | [**SetImeiLockRequest**](SetImeiLockRequest.md)| IMEI lock configuration for the subscriber. (IMEI can be left blank for locking to the current IMEI of an online subscriber.) | [optional]

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**400** | Invalid IMEI string or subscriber is offline and IMEI not specified. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_subscriber_to_standby**
> Subscriber set_subscriber_to_standby(imsi)

Set Subscriber to standby mode.

Set the specified subscriber to standby mode.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Set Subscriber to standby mode.
        api_response = api_instance.set_subscriber_to_standby(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->set_subscriber_to_standby: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**400** | The specified subscriber does not support standby mode. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_subscriber**
> Subscriber suspend_subscriber(imsi)

Suspend Subscriber.

Suspends the specified subscriber

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Suspend Subscriber.
        api_response = api_instance.suspend_subscriber(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->suspend_subscriber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_subscriber**
> Subscriber terminate_subscriber(imsi)

Terminate Subscriber.

Terminates the specified subscriber

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Terminate Subscriber.
        api_response = api_instance.terminate_subscriber(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->terminate_subscriber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_expiry_time**
> unset_expiry_time(imsi)

Delete Expiry Time of Subscriber.

Deletes expiry time of specified subscriber and changes it to indefinite.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Delete Expiry Time of Subscriber.
        api_instance.unset_expiry_time(imsi)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->unset_expiry_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

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
**204** | Change of specified subscriber&#39;s expiry time to indefinite complete. |  -  |
**404** | The specified subscriber does not exist or the subscriber does not have an expiry time. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_group**
> Subscriber unset_group(imsi)

Unset Group to Subscriber.

Removes the group configuration from the specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Unset Group to Subscriber.
        api_response = api_instance.unset_group(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->unset_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist or the subscriber does not belong to a group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_imei_lock**
> Subscriber unset_imei_lock(imsi)

Unset IMEI lock configuration for Subscriber.

Remove any existing IMEI lock configuration for the subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.

    # example passing only required values which don't have defaults set
    try:
        # Unset IMEI lock configuration for Subscriber.
        api_response = api_instance.unset_imei_lock(imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->unset_imei_lock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_speed_class**
> Subscriber update_speed_class(imsi, update_speed_class_request)

Update Subscriber speed class.

Changes the speed class of the specified subscriber.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.update_speed_class_request import UpdateSpeedClassRequest
from soracom_api.model.subscriber import Subscriber
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    imsi = "imsi_example" # str | IMSI of the target subscriber.
    update_speed_class_request = UpdateSpeedClassRequest(
        speed_class="s1.minimum",
    ) # UpdateSpeedClassRequest | speed_class

    # example passing only required values which don't have defaults set
    try:
        # Update Subscriber speed class.
        api_response = api_instance.update_speed_class(imsi, update_speed_class_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->update_speed_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI of the target subscriber. |
 **update_speed_class_request** | [**UpdateSpeedClassRequest**](UpdateSpeedClassRequest.md)| speed_class |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The subscriber&#39;s detailed information after the update. |  -  |
**404** | The specified subscriber does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_subscriber_transfer_token**
> VerifySubscriberTransferTokenResponse verify_subscriber_transfer_token(verify_subscriber_transfer_token_request)

Verify Subscriber Transfer Token.

Verifies the subscriber's control transfer token, and executes the transfer. This API is called from the operator of the control destination.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import subscriber_api
from soracom_api.model.verify_subscriber_transfer_token_response import VerifySubscriberTransferTokenResponse
from soracom_api.model.verify_subscriber_transfer_token_request import VerifySubscriberTransferTokenRequest
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
    api_instance = subscriber_api.SubscriberApi(api_client)
    verify_subscriber_transfer_token_request = VerifySubscriberTransferTokenRequest(
        token="token_example",
    ) # VerifySubscriberTransferTokenRequest | Subscriber transfer token that noticed via email.

    # example passing only required values which don't have defaults set
    try:
        # Verify Subscriber Transfer Token.
        api_response = api_instance.verify_subscriber_transfer_token(verify_subscriber_transfer_token_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SubscriberApi->verify_subscriber_transfer_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_subscriber_transfer_token_request** | [**VerifySubscriberTransferTokenRequest**](VerifySubscriberTransferTokenRequest.md)| Subscriber transfer token that noticed via email. |

### Return type

[**VerifySubscriberTransferTokenResponse**](VerifySubscriberTransferTokenResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

