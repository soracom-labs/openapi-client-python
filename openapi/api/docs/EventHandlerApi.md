# api.EventHandlerApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_event_handler**](EventHandlerApi.md#create_event_handler) | **POST** /event_handlers | Create Event Handler.
[**delete_event_handler**](EventHandlerApi.md#delete_event_handler) | **DELETE** /event_handlers/{handler_id} | Delete Event Handler.
[**delete_ignore_event_handler**](EventHandlerApi.md#delete_ignore_event_handler) | **DELETE** /event_handlers/{handler_id}/subscribers/{imsi}/ignore | Delete Ignore Event Handler.
[**get_event_handler**](EventHandlerApi.md#get_event_handler) | **GET** /event_handlers/{handler_id} | Get Event Handler.
[**list_event_handlers**](EventHandlerApi.md#list_event_handlers) | **GET** /event_handlers | List Event Handlers.
[**list_event_handlers_by_subscriber**](EventHandlerApi.md#list_event_handlers_by_subscriber) | **GET** /event_handlers/subscribers/{imsi} | List Event Handlers related to Subscriber.
[**set_ignore_event_handler**](EventHandlerApi.md#set_ignore_event_handler) | **POST** /event_handlers/{handler_id}/subscribers/{imsi}/ignore | Ignore Event Handler.
[**update_event_handler**](EventHandlerApi.md#update_event_handler) | **PUT** /event_handlers/{handler_id} | Update Event Handler.


# **create_event_handler**
> EventHandlerModel create_event_handler(create_event_handler_request)

Create Event Handler.

Creates a new event handler. Please see also https://developers.soracom.io/en/docs/air/event-handler/

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import event_handler_api
from api.model.event_handler_model import EventHandlerModel
from api.model.create_event_handler_request import CreateEventHandlerRequest
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
    api_instance = event_handler_api.EventHandlerApi(api_client)
    create_event_handler_request = CreateEventHandlerRequest(
        action_config_list=[
            ActionConfig(
                properties=ActionConfigProperty(
                    access_key="access_key_example",
                    body="body_example",
                    content_type="content_type_example",
                    endpoint="endpoint_example",
                    execution_date_time_const="IMMEDIATELY",
                    execution_offset_minutes="execution_offset_minutes_example",
                    function_name="function_name_example",
                    headers={},
                    http_method="GET",
                    message="message_example",
                    parameter1="parameter1_example",
                    parameter2="parameter2_example",
                    parameter3="parameter3_example",
                    parameter4="parameter4_example",
                    parameter5="parameter5_example",
                    secret_access_key="secret_access_key_example",
                    speed_class="s1.minimum",
                    title="title_example",
                    to="to_example",
                    url="url_example",
                ),
                type="ChangeSpeedClassAction",
            ),
        ],
        description="description_example",
        name="name_example",
        rule_config=RuleConfig(
            properties=RuleConfigProperty(
                inactive_timeout_date_const="IMMEDIATELY",
                inactive_timeout_offset_minutes="inactive_timeout_offset_minutes_example",
                limit_total_traffic_mega_byte="limit_total_traffic_mega_byte_example",
                run_once_among_target=True,
                target_ota_status="started",
                target_speed_class="s1.minimum",
                target_status="ready",
            ),
            type="SubscriberDailyTrafficRule",
        ),
        status="inactive",
        target_group_id="target_group_id_example",
        target_imsi="target_imsi_example",
        target_operator_id="target_operator_id_example",
        target_sim_id="target_sim_id_example",
    ) # CreateEventHandlerRequest | event handler settings

    # example passing only required values which don't have defaults set
    try:
        # Create Event Handler.
        api_response = api_instance.create_event_handler(create_event_handler_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling EventHandlerApi->create_event_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_event_handler_request** | [**CreateEventHandlerRequest**](CreateEventHandlerRequest.md)| event handler settings |

### Return type

[**EventHandlerModel**](EventHandlerModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_handler**
> delete_event_handler(handler_id)

Delete Event Handler.

Deletes the specified event handler.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import event_handler_api
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
    api_instance = event_handler_api.EventHandlerApi(api_client)
    handler_id = "handler_id_example" # str | handler ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Event Handler.
        api_instance.delete_event_handler(handler_id)
    except api.ApiException as e:
        print("Exception when calling EventHandlerApi->delete_event_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handler_id** | **str**| handler ID |

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
**204** | OK. |  -  |
**404** | EventHandler not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_ignore_event_handler**
> delete_ignore_event_handler(imsi, handler_id)

Delete Ignore Event Handler.

Deletes the setting for ignoring the specified event handler of the specified IMSI.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import event_handler_api
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
    api_instance = event_handler_api.EventHandlerApi(api_client)
    imsi = "imsi_example" # str | imsi
    handler_id = "handler_id_example" # str | handler_id

    # example passing only required values which don't have defaults set
    try:
        # Delete Ignore Event Handler.
        api_instance.delete_ignore_event_handler(imsi, handler_id)
    except api.ApiException as e:
        print("Exception when calling EventHandlerApi->delete_ignore_event_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| imsi |
 **handler_id** | **str**| handler_id |

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
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_handler**
> EventHandlerModel get_event_handler(handler_id)

Get Event Handler.

Returns information about the specified event handler.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import event_handler_api
from api.model.event_handler_model import EventHandlerModel
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
    api_instance = event_handler_api.EventHandlerApi(api_client)
    handler_id = "handler_id_example" # str | handler ID

    # example passing only required values which don't have defaults set
    try:
        # Get Event Handler.
        api_response = api_instance.get_event_handler(handler_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling EventHandlerApi->get_event_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handler_id** | **str**| handler ID |

### Return type

[**EventHandlerModel**](EventHandlerModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**404** | Handler not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_event_handlers**
> [EventHandlerModel] list_event_handlers()

List Event Handlers.

Returns a list of event handlers.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import event_handler_api
from api.model.event_handler_model import EventHandlerModel
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
    api_instance = event_handler_api.EventHandlerApi(api_client)
    target = "operator" # str | target (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Event Handlers.
        api_response = api_instance.list_event_handlers(target=target)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling EventHandlerApi->list_event_handlers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **target** | **str**| target | [optional]

### Return type

[**[EventHandlerModel]**](EventHandlerModel.md)

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

# **list_event_handlers_by_subscriber**
> [EventHandlerModel] list_event_handlers_by_subscriber(imsi)

List Event Handlers related to Subscriber.

Returns a list of event handlers related to the specified IMSI.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import event_handler_api
from api.model.event_handler_model import EventHandlerModel
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
    api_instance = event_handler_api.EventHandlerApi(api_client)
    imsi = "imsi_example" # str | imsi

    # example passing only required values which don't have defaults set
    try:
        # List Event Handlers related to Subscriber.
        api_response = api_instance.list_event_handlers_by_subscriber(imsi)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling EventHandlerApi->list_event_handlers_by_subscriber: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| imsi |

### Return type

[**[EventHandlerModel]**](EventHandlerModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_ignore_event_handler**
> set_ignore_event_handler(imsi, handler_id)

Ignore Event Handler.

Adds a setting for ignoring the specified event handler of the specified IMSI.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import event_handler_api
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
    api_instance = event_handler_api.EventHandlerApi(api_client)
    imsi = "imsi_example" # str | imsi
    handler_id = "handler_id_example" # str | handler_id

    # example passing only required values which don't have defaults set
    try:
        # Ignore Event Handler.
        api_instance.set_ignore_event_handler(imsi, handler_id)
    except api.ApiException as e:
        print("Exception when calling EventHandlerApi->set_ignore_event_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| imsi |
 **handler_id** | **str**| handler_id |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_event_handler**
> update_event_handler(handler_id, body)

Update Event Handler.

Updates the specified event handler. Please see also https://developers.soracom.io/en/docs/air/event-handler/

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import event_handler_api
from api.model.create_event_handler_request import CreateEventHandlerRequest
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
    api_instance = event_handler_api.EventHandlerApi(api_client)
    handler_id = "handler_id_example" # str | handler ID
    body = CreateEventHandlerRequest(
        action_config_list=[
            ActionConfig(
                properties=ActionConfigProperty(
                    access_key="access_key_example",
                    body="body_example",
                    content_type="content_type_example",
                    endpoint="endpoint_example",
                    execution_date_time_const="IMMEDIATELY",
                    execution_offset_minutes="execution_offset_minutes_example",
                    function_name="function_name_example",
                    headers={},
                    http_method="GET",
                    message="message_example",
                    parameter1="parameter1_example",
                    parameter2="parameter2_example",
                    parameter3="parameter3_example",
                    parameter4="parameter4_example",
                    parameter5="parameter5_example",
                    secret_access_key="secret_access_key_example",
                    speed_class="s1.minimum",
                    title="title_example",
                    to="to_example",
                    url="url_example",
                ),
                type="ChangeSpeedClassAction",
            ),
        ],
        description="description_example",
        name="name_example",
        rule_config=RuleConfig(
            properties=RuleConfigProperty(
                inactive_timeout_date_const="IMMEDIATELY",
                inactive_timeout_offset_minutes="inactive_timeout_offset_minutes_example",
                limit_total_traffic_mega_byte="limit_total_traffic_mega_byte_example",
                run_once_among_target=True,
                target_ota_status="started",
                target_speed_class="s1.minimum",
                target_status="ready",
            ),
            type="SubscriberDailyTrafficRule",
        ),
        status="inactive",
        target_group_id="target_group_id_example",
        target_imsi="target_imsi_example",
        target_operator_id="target_operator_id_example",
        target_sim_id="target_sim_id_example",
    ) # CreateEventHandlerRequest | event handler settings

    # example passing only required values which don't have defaults set
    try:
        # Update Event Handler.
        api_instance.update_event_handler(handler_id, body)
    except api.ApiException as e:
        print("Exception when calling EventHandlerApi->update_event_handler: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **handler_id** | **str**| handler ID |
 **body** | [**CreateEventHandlerRequest**](CreateEventHandlerRequest.md)| event handler settings |

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
**200** | OK. |  -  |
**400** | Invalid handlerId. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

