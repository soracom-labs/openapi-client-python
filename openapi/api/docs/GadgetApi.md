# api.GadgetApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_gadget_tag**](GadgetApi.md#delete_gadget_tag) | **DELETE** /gadgets/{product_id}/{serial_number}/tags/{tag_name} | Delete gadget Tag.
[**disable_termination_on_gadget**](GadgetApi.md#disable_termination_on_gadget) | **POST** /gadgets/{product_id}/{serial_number}/disable_termination | Disable Termination of gadget.
[**enable_termination_on_gadget**](GadgetApi.md#enable_termination_on_gadget) | **POST** /gadgets/{product_id}/{serial_number}/enable_termination | Enable Termination of gadget.
[**get_gadget**](GadgetApi.md#get_gadget) | **GET** /gadgets/{product_id}/{serial_number} | Get gadget.
[**list_gadgets**](GadgetApi.md#list_gadgets) | **GET** /gadgets | List gadgets.
[**put_gadget_tags**](GadgetApi.md#put_gadget_tags) | **PUT** /gadgets/{product_id}/{serial_number}/tags | Bulk Insert or Update gadget Tags.
[**register_gadget**](GadgetApi.md#register_gadget) | **POST** /gadgets/{product_id}/{serial_number}/register | Register a gadget.
[**set_gadget_group**](GadgetApi.md#set_gadget_group) | **POST** /gadgets/{product_id}/{serial_number}/set_group | Set Group of gadget.
[**terminate_gadget**](GadgetApi.md#terminate_gadget) | **POST** /gadgets/{product_id}/{serial_number}/terminate | Terminate gadget.
[**unset_gadget_group**](GadgetApi.md#unset_gadget_group) | **POST** /gadgets/{product_id}/{serial_number}/unset_group | Unset Group of gadget.


# **delete_gadget_tag**
> delete_gadget_tag(product_id, serial_number, tag_name)

Delete gadget Tag.

Deletes a tag from the specified gadget.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import gadget_api
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
    api_instance = gadget_api.GadgetApi(api_client)
    product_id = "product_id_example" # str | Product ID of the target gadget.
    serial_number = "serial_number_example" # str | Serial Number of the target gadget.
    tag_name = "tag_name_example" # str | Tag name to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().)

    # example passing only required values which don't have defaults set
    try:
        # Delete gadget Tag.
        api_instance.delete_gadget_tag(product_id, serial_number, tag_name)
    except api.ApiException as e:
        print("Exception when calling GadgetApi->delete_gadget_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product ID of the target gadget. |
 **serial_number** | **str**| Serial Number of the target gadget. |
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
**404** | The specified gadget or the tag does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_termination_on_gadget**
> Gadget disable_termination_on_gadget(product_id, serial_number)

Disable Termination of gadget.

Disables termination of specified gadget.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import gadget_api
from api.model.gadget import Gadget
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
    api_instance = gadget_api.GadgetApi(api_client)
    product_id = "product_id_example" # str | Product ID of the target gadget.
    serial_number = "serial_number_example" # str | Serial Number of the target gadget.

    # example passing only required values which don't have defaults set
    try:
        # Disable Termination of gadget.
        api_response = api_instance.disable_termination_on_gadget(product_id, serial_number)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GadgetApi->disable_termination_on_gadget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product ID of the target gadget. |
 **serial_number** | **str**| Serial Number of the target gadget. |

### Return type

[**Gadget**](Gadget.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The gadget&#39;s detailed information after the update. |  -  |
**404** | The specified gadget does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_termination_on_gadget**
> Gadget enable_termination_on_gadget(product_id, serial_number)

Enable Termination of gadget.

Enables termination of specified gadget.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import gadget_api
from api.model.gadget import Gadget
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
    api_instance = gadget_api.GadgetApi(api_client)
    product_id = "product_id_example" # str | Product ID of the target gadget.
    serial_number = "serial_number_example" # str | Serial Number of the target gadget.

    # example passing only required values which don't have defaults set
    try:
        # Enable Termination of gadget.
        api_response = api_instance.enable_termination_on_gadget(product_id, serial_number)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GadgetApi->enable_termination_on_gadget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product ID of the target gadget. |
 **serial_number** | **str**| Serial Number of the target gadget. |

### Return type

[**Gadget**](Gadget.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The gadget&#39;s detailed information after the update. |  -  |
**404** | The specified gadget does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_gadget**
> Gadget get_gadget(product_id, serial_number)

Get gadget.

Returns information about the specified gadget.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import gadget_api
from api.model.gadget import Gadget
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
    api_instance = gadget_api.GadgetApi(api_client)
    product_id = "product_id_example" # str | Product ID of the target gadget.
    serial_number = "serial_number_example" # str | Serial Number of the target gadget.

    # example passing only required values which don't have defaults set
    try:
        # Get gadget.
        api_response = api_instance.get_gadget(product_id, serial_number)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GadgetApi->get_gadget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product ID of the target gadget. |
 **serial_number** | **str**| Serial Number of the target gadget. |

### Return type

[**Gadget**](Gadget.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The gadget&#39;s detailed information. |  -  |
**404** | The specified gadget does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gadgets**
> [Gadget] list_gadgets()

List gadgets.

Returns a list of gadgets that match certain criteria. If the total number of gadgets does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import gadget_api
from api.model.gadget import Gadget
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
    api_instance = gadget_api.GadgetApi(api_client)
    product_id = "product_id_example" # str | Product ID for filtering the search. (optional)
    tag_name = "tag_name_example" # str | Tag name for filtering the search (exact match). (optional)
    tag_value = "tag_value_example" # str | Tag search string for filtering the search. Required when `tag_name` has been specified. (optional)
    tag_value_match_mode = "exact" # str | Tag match mode. (optional) if omitted the server will use the default value of "exact"
    limit = 1 # int | Maximum number of gadgets to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The ID ({product_id}/{serial_number}) of the last gadget retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next device onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List gadgets.
        api_response = api_instance.list_gadgets(product_id=product_id, tag_name=tag_name, tag_value=tag_value, tag_value_match_mode=tag_value_match_mode, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GadgetApi->list_gadgets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product ID for filtering the search. | [optional]
 **tag_name** | **str**| Tag name for filtering the search (exact match). | [optional]
 **tag_value** | **str**| Tag search string for filtering the search. Required when &#x60;tag_name&#x60; has been specified. | [optional]
 **tag_value_match_mode** | **str**| Tag match mode. | [optional] if omitted the server will use the default value of "exact"
 **limit** | **int**| Maximum number of gadgets to retrieve. | [optional]
 **last_evaluated_key** | **str**| The ID ({product_id}/{serial_number}) of the last gadget retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next device onward. | [optional]

### Return type

[**[Gadget]**](Gadget.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Gadgets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_gadget_tags**
> Gadget put_gadget_tags(product_id, serial_number, tag_update_request)

Bulk Insert or Update gadget Tags.

Inserts/updates tags for the specified gadget.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import gadget_api
from api.model.tag_update_request import TagUpdateRequest
from api.model.gadget import Gadget
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
    api_instance = gadget_api.GadgetApi(api_client)
    product_id = "product_id_example" # str | Product ID of the target gadget.
    serial_number = "serial_number_example" # str | Serial Number of the target gadget.
    tag_update_request = [
        TagUpdateRequest(
            tag_name="tag_name_example",
            tag_value="tag_value_example",
        ),
    ] # [TagUpdateRequest] | Array of tags to be inserted/updated.

    # example passing only required values which don't have defaults set
    try:
        # Bulk Insert or Update gadget Tags.
        api_response = api_instance.put_gadget_tags(product_id, serial_number, tag_update_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GadgetApi->put_gadget_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product ID of the target gadget. |
 **serial_number** | **str**| Serial Number of the target gadget. |
 **tag_update_request** | [**[TagUpdateRequest]**](TagUpdateRequest.md)| Array of tags to be inserted/updated. |

### Return type

[**Gadget**](Gadget.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The gadget&#39;s detailed information after the update. |  -  |
**404** | The specified gadget does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_gadget**
> Gadget register_gadget(product_id, serial_number, gadget_registration_request)

Register a gadget.

Registers a gadget

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import gadget_api
from api.model.gadget_registration_request import GadgetRegistrationRequest
from api.model.gadget import Gadget
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
    api_instance = gadget_api.GadgetApi(api_client)
    product_id = "product_id_example" # str | Product ID of the target gadget.
    serial_number = "serial_number_example" # str | Serial Number of the target gadget.
    gadget_registration_request = GadgetRegistrationRequest(
        tags={
            "key": "key_example",
        },
    ) # GadgetRegistrationRequest | Gadget registration request

    # example passing only required values which don't have defaults set
    try:
        # Register a gadget.
        api_response = api_instance.register_gadget(product_id, serial_number, gadget_registration_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GadgetApi->register_gadget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product ID of the target gadget. |
 **serial_number** | **str**| Serial Number of the target gadget. |
 **gadget_registration_request** | [**GadgetRegistrationRequest**](GadgetRegistrationRequest.md)| Gadget registration request |

### Return type

[**Gadget**](Gadget.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gadget successfully registered |  -  |
**404** | No such resource found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_gadget_group**
> Gadget set_gadget_group(product_id, serial_number, group)

Set Group of gadget.

Sets or overwrites a group for the specified gadget.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import gadget_api
from api.model.group import Group
from api.model.gadget import Gadget
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
    api_instance = gadget_api.GadgetApi(api_client)
    product_id = "product_id_example" # str | Product ID of the target gadget.
    serial_number = "serial_number_example" # str | Serial Number of the target gadget.
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
        # Set Group of gadget.
        api_response = api_instance.set_gadget_group(product_id, serial_number, group)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GadgetApi->set_gadget_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product ID of the target gadget. |
 **serial_number** | **str**| Serial Number of the target gadget. |
 **group** | [**Group**](Group.md)| Group (may include ID only). |

### Return type

[**Gadget**](Gadget.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The gadget&#39;s detailed information after the update. |  -  |
**404** | The specified gadget does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_gadget**
> Gadget terminate_gadget(product_id, serial_number)

Terminate gadget.

Terminates the specified gadget

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import gadget_api
from api.model.gadget import Gadget
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
    api_instance = gadget_api.GadgetApi(api_client)
    product_id = "product_id_example" # str | Product ID of the target gadget.
    serial_number = "serial_number_example" # str | Serial Number of the target gadget.

    # example passing only required values which don't have defaults set
    try:
        # Terminate gadget.
        api_response = api_instance.terminate_gadget(product_id, serial_number)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GadgetApi->terminate_gadget: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product ID of the target gadget. |
 **serial_number** | **str**| Serial Number of the target gadget. |

### Return type

[**Gadget**](Gadget.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The gadget&#39;s detailed information after the update. |  -  |
**404** | The specified gadget does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_gadget_group**
> Gadget unset_gadget_group(product_id, serial_number)

Unset Group of gadget.

Removes the group configuration from the specified gadget.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import gadget_api
from api.model.gadget import Gadget
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
    api_instance = gadget_api.GadgetApi(api_client)
    product_id = "product_id_example" # str | Product ID of the target gadget.
    serial_number = "serial_number_example" # str | Serial Number of the target gadget.

    # example passing only required values which don't have defaults set
    try:
        # Unset Group of gadget.
        api_response = api_instance.unset_gadget_group(product_id, serial_number)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GadgetApi->unset_gadget_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| Product ID of the target gadget. |
 **serial_number** | **str**| Serial Number of the target gadget. |

### Return type

[**Gadget**](Gadget.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The gadget&#39;s detailed information after the update. |  -  |
**404** | The specified gadget does not exist or the gadget does not belong to a group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

