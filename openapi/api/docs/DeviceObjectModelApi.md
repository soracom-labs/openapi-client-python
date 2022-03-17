# api.DeviceObjectModelApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_object_model**](DeviceObjectModelApi.md#create_device_object_model) | **POST** /device_object_models | Creates a new device object model
[**delete_device_object_model**](DeviceObjectModelApi.md#delete_device_object_model) | **DELETE** /device_object_models/{model_id} | Deletes a device object model
[**get_device_object_model**](DeviceObjectModelApi.md#get_device_object_model) | **GET** /device_object_models/{model_id} | Gets a device object model
[**list_device_object_models**](DeviceObjectModelApi.md#list_device_object_models) | **GET** /device_object_models | Returns a list of device object models
[**set_device_object_model_scope**](DeviceObjectModelApi.md#set_device_object_model_scope) | **POST** /device_object_models/{model_id}/set_scope | Sets scope for a device object model
[**update_device_object_model**](DeviceObjectModelApi.md#update_device_object_model) | **POST** /device_object_models/{model_id} | Updates a device object model


# **create_device_object_model**
> DeviceObjectModel create_device_object_model(device_object_model)

Creates a new device object model

Creates a new device object model

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_object_model_api
from api.model.device_object_model import DeviceObjectModel
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
    api_instance = device_object_model_api.DeviceObjectModelApi(api_client)
    device_object_model = DeviceObjectModel(
        created_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        format="xml",
        last_modified_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        object_id="object_id_example",
        object_name="object_name_example",
        operator_id="operator_id_example",
        scope="scope_example",
    ) # DeviceObjectModel | Device object model definition in either XML or JSON format.

    # example passing only required values which don't have defaults set
    try:
        # Creates a new device object model
        api_response = api_instance.create_device_object_model(device_object_model)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceObjectModelApi->create_device_object_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **device_object_model** | [**DeviceObjectModel**](DeviceObjectModel.md)| Device object model definition in either XML or JSON format. |

### Return type

[**DeviceObjectModel**](DeviceObjectModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Device object model created |  -  |
**400** | Failed to parse device object model definition |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_device_object_model**
> delete_device_object_model(model_id)

Deletes a device object model

Deletes a device object model

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_object_model_api
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
    api_instance = device_object_model_api.DeviceObjectModelApi(api_client)
    model_id = "model_id_example" # str | Device object model ID

    # example passing only required values which don't have defaults set
    try:
        # Deletes a device object model
        api_instance.delete_device_object_model(model_id)
    except api.ApiException as e:
        print("Exception when calling DeviceObjectModelApi->delete_device_object_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| Device object model ID |

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
**204** | Successfully deleted |  -  |
**404** | No such device object model found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_device_object_model**
> DeviceObjectModel get_device_object_model(model_id)

Gets a device object model

Gets a device object model

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_object_model_api
from api.model.device_object_model import DeviceObjectModel
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
    api_instance = device_object_model_api.DeviceObjectModelApi(api_client)
    model_id = "model_id_example" # str | Device object model ID

    # example passing only required values which don't have defaults set
    try:
        # Gets a device object model
        api_response = api_instance.get_device_object_model(model_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceObjectModelApi->get_device_object_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| Device object model ID |

### Return type

[**DeviceObjectModel**](DeviceObjectModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Device object model |  -  |
**404** | No such device object model found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_device_object_models**
> [DeviceObjectModel] list_device_object_models()

Returns a list of device object models

Returns a list of device object models

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_object_model_api
from api.model.device_object_model import DeviceObjectModel
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
    api_instance = device_object_model_api.DeviceObjectModelApi(api_client)
    last_evaluated_key = "last_evaluated_key_example" # str | ID of the last device object model in the previous page (optional)
    limit = -1 # int | Max number of device object models in a response (optional) if omitted the server will use the default value of -1

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of device object models
        api_response = api_instance.list_device_object_models(last_evaluated_key=last_evaluated_key, limit=limit)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceObjectModelApi->list_device_object_models: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **last_evaluated_key** | **str**| ID of the last device object model in the previous page | [optional]
 **limit** | **int**| Max number of device object models in a response | [optional] if omitted the server will use the default value of -1

### Return type

[**[DeviceObjectModel]**](DeviceObjectModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of device object models |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_device_object_model_scope**
> DeviceObjectModel set_device_object_model_scope(model_id, set_device_object_model_scope_request)

Sets scope for a device object model

Sets scope for a device object model

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_object_model_api
from api.model.set_device_object_model_scope_request import SetDeviceObjectModelScopeRequest
from api.model.device_object_model import DeviceObjectModel
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
    api_instance = device_object_model_api.DeviceObjectModelApi(api_client)
    model_id = "model_id_example" # str | Target device object model ID
    set_device_object_model_scope_request = SetDeviceObjectModelScopeRequest(
        scope="scope_example",
    ) # SetDeviceObjectModelScopeRequest | Scope value that is applied to the target device object model

    # example passing only required values which don't have defaults set
    try:
        # Sets scope for a device object model
        api_response = api_instance.set_device_object_model_scope(model_id, set_device_object_model_scope_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceObjectModelApi->set_device_object_model_scope: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| Target device object model ID |
 **set_device_object_model_scope_request** | [**SetDeviceObjectModelScopeRequest**](SetDeviceObjectModelScopeRequest.md)| Scope value that is applied to the target device object model |

### Return type

[**DeviceObjectModel**](DeviceObjectModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Scope is set to the target device object model |  -  |
**404** | No such device object model found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_device_object_model**
> DeviceObjectModel update_device_object_model(model_id, device_object_model)

Updates a device object model

Updates a device object model

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import device_object_model_api
from api.model.device_object_model import DeviceObjectModel
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
    api_instance = device_object_model_api.DeviceObjectModelApi(api_client)
    model_id = "model_id_example" # str | Device object model ID
    device_object_model = DeviceObjectModel(
        created_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        format="xml",
        last_modified_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        object_id="object_id_example",
        object_name="object_name_example",
        operator_id="operator_id_example",
        scope="scope_example",
    ) # DeviceObjectModel | Device object model definition in either XML or JSON format.

    # example passing only required values which don't have defaults set
    try:
        # Updates a device object model
        api_response = api_instance.update_device_object_model(model_id, device_object_model)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling DeviceObjectModelApi->update_device_object_model: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_id** | **str**| Device object model ID |
 **device_object_model** | [**DeviceObjectModel**](DeviceObjectModel.md)| Device object model definition in either XML or JSON format. |

### Return type

[**DeviceObjectModel**](DeviceObjectModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json, application/xml
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Device object model updated |  -  |
**400** | Failed to parse device object model definition |  -  |
**404** | No such device object model found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

