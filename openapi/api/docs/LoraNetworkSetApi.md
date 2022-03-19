# soracom_api.LoraNetworkSetApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_permission_to_lora_network_set**](LoraNetworkSetApi.md#add_permission_to_lora_network_set) | **POST** /lora_network_sets/{ns_id}/add_permission | Adds permission to a LoRa network set.
[**create_lora_network_set**](LoraNetworkSetApi.md#create_lora_network_set) | **POST** /lora_network_sets | Create a LoRa network set.
[**delete_lora_network_set**](LoraNetworkSetApi.md#delete_lora_network_set) | **DELETE** /lora_network_sets/{ns_id} | Delete LoRa network set.
[**delete_lora_network_set_tag**](LoraNetworkSetApi.md#delete_lora_network_set_tag) | **DELETE** /lora_network_sets/{ns_id}/tags/{tag_name} | Delete LoRa network set tag.
[**get_lora_network_set**](LoraNetworkSetApi.md#get_lora_network_set) | **GET** /lora_network_sets/{ns_id} | Get LoRa network set.
[**list_gateways_in_lora_network_set**](LoraNetworkSetApi.md#list_gateways_in_lora_network_set) | **GET** /lora_network_sets/{ns_id}/gateways | List LoRa Gateways in a Network Set.
[**list_lora_network_sets**](LoraNetworkSetApi.md#list_lora_network_sets) | **GET** /lora_network_sets | List LoRa Network Sets.
[**put_lora_network_set_tags**](LoraNetworkSetApi.md#put_lora_network_set_tags) | **PUT** /lora_network_sets/{ns_id}/tags | Bulk Insert or Update LoRa network set tags.
[**revoke_permission_from_lora_network_set**](LoraNetworkSetApi.md#revoke_permission_from_lora_network_set) | **POST** /lora_network_sets/{ns_id}/revoke_permission | Revokes a permission from a LoRa network set.


# **add_permission_to_lora_network_set**
> LoraNetworkSet add_permission_to_lora_network_set(ns_id, update_permission_request)

Adds permission to a LoRa network set.

Adds permission to allow another operator to use the network set.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_network_set_api
from soracom_api.model.update_permission_request import UpdatePermissionRequest
from soracom_api.model.lora_network_set import LoraNetworkSet
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
    api_instance = lora_network_set_api.LoraNetworkSetApi(api_client)
    ns_id = "ns_id_example" # str | ID of the target LoRa network set.
    update_permission_request = UpdatePermissionRequest(
        operator_id="operator_id_example",
    ) # UpdatePermissionRequest | ID of the operator to be added to the list of allowed operators.

    # example passing only required values which don't have defaults set
    try:
        # Adds permission to a LoRa network set.
        api_response = api_instance.add_permission_to_lora_network_set(ns_id, update_permission_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraNetworkSetApi->add_permission_to_lora_network_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_id** | **str**| ID of the target LoRa network set. |
 **update_permission_request** | [**UpdatePermissionRequest**](UpdatePermissionRequest.md)| ID of the operator to be added to the list of allowed operators. |

### Return type

[**LoraNetworkSet**](LoraNetworkSet.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permission added to the network set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_lora_network_set**
> LoraNetworkSet create_lora_network_set(lora_network_set)

Create a LoRa network set.

Creates a specified LoRa network set

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_network_set_api
from soracom_api.model.lora_network_set import LoraNetworkSet
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
    api_instance = lora_network_set_api.LoraNetworkSetApi(api_client)
    lora_network_set = LoraNetworkSet(
        allowed_operators=[
            "allowed_operators_example",
        ],
        created_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        last_modified_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        network_set_id="network_set_id_example",
        operator_id="operator_id_example",
        tags={
            "key": "key_example",
        },
    ) # LoraNetworkSet | Additional metadata such as tags for a LoRa network set to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a LoRa network set.
        api_response = api_instance.create_lora_network_set(lora_network_set)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraNetworkSetApi->create_lora_network_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lora_network_set** | [**LoraNetworkSet**](LoraNetworkSet.md)| Additional metadata such as tags for a LoRa network set to create. |

### Return type

[**LoraNetworkSet**](LoraNetworkSet.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A LoRa network set was created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lora_network_set**
> delete_lora_network_set(ns_id)

Delete LoRa network set.

Deletes the specified LoRa network set

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_network_set_api
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
    api_instance = lora_network_set_api.LoraNetworkSetApi(api_client)
    ns_id = "ns_id_example" # str | ID of the target LoRa network set.

    # example passing only required values which don't have defaults set
    try:
        # Delete LoRa network set.
        api_instance.delete_lora_network_set(ns_id)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraNetworkSetApi->delete_lora_network_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_id** | **str**| ID of the target LoRa network set. |

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
**204** | Successfully deleted. |  -  |
**404** | The specified LoRa network set does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lora_network_set_tag**
> delete_lora_network_set_tag(ns_id, tag_name)

Delete LoRa network set tag.

Deletes a tag from the specified LoRa network set.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_network_set_api
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
    api_instance = lora_network_set_api.LoraNetworkSetApi(api_client)
    ns_id = "ns_id_example" # str | ID of the target LoRa network set.
    tag_name = "tag_name_example" # str | Name of tag to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().)

    # example passing only required values which don't have defaults set
    try:
        # Delete LoRa network set tag.
        api_instance.delete_lora_network_set_tag(ns_id, tag_name)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraNetworkSetApi->delete_lora_network_set_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_id** | **str**| ID of the target LoRa network set. |
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
**404** | The specified LoRa network set or the tag does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lora_network_set**
> LoraNetworkSet get_lora_network_set(ns_id)

Get LoRa network set.

Returns information about the specified LoRa network set.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_network_set_api
from soracom_api.model.lora_network_set import LoraNetworkSet
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
    api_instance = lora_network_set_api.LoraNetworkSetApi(api_client)
    ns_id = "ns_id_example" # str | ID of the target LoRa network set.

    # example passing only required values which don't have defaults set
    try:
        # Get LoRa network set.
        api_response = api_instance.get_lora_network_set(ns_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraNetworkSetApi->get_lora_network_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_id** | **str**| ID of the target LoRa network set. |

### Return type

[**LoraNetworkSet**](LoraNetworkSet.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa network set&#39;s detailed information. |  -  |
**404** | The specified LoRa network set does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gateways_in_lora_network_set**
> [LoraGateway] list_gateways_in_lora_network_set(ns_id)

List LoRa Gateways in a Network Set.

Returns a list of LoRa gateways that belong to the specified network set. If the total number of LoRa gateways does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_network_set_api
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
    api_instance = lora_network_set_api.LoraNetworkSetApi(api_client)
    ns_id = "ns_id_example" # str | ID of the target LoRa network set.
    limit = 1 # int | Maximum number of LoRa gateways to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The ID of the last gateway retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next device onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List LoRa Gateways in a Network Set.
        api_response = api_instance.list_gateways_in_lora_network_set(ns_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraNetworkSetApi->list_gateways_in_lora_network_set: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List LoRa Gateways in a Network Set.
        api_response = api_instance.list_gateways_in_lora_network_set(ns_id, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraNetworkSetApi->list_gateways_in_lora_network_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_id** | **str**| ID of the target LoRa network set. |
 **limit** | **int**| Maximum number of LoRa gateways to retrieve. | [optional]
 **last_evaluated_key** | **str**| The ID of the last gateway retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next device onward. | [optional]

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
**404** | The specified network set does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lora_network_sets**
> [LoraNetworkSet] list_lora_network_sets()

List LoRa Network Sets.

Returns a list of LoRa network sets that match certain criteria. If the total number of LoRa network sets does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_network_set_api
from soracom_api.model.lora_network_set import LoraNetworkSet
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
    api_instance = lora_network_set_api.LoraNetworkSetApi(api_client)
    tag_name = "tag_name_example" # str | Tag name for filtering the search (exact match). (optional)
    tag_value = "tag_value_example" # str | Tag search string for filtering the search. Required when `tag_name` has been specified. (optional)
    tag_value_match_mode = "exact" # str | Tag match mode. (optional) if omitted the server will use the default value of "exact"
    limit = 1 # int | Maximum number of LoRa devices to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The ID of the last network set retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next device onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List LoRa Network Sets.
        api_response = api_instance.list_lora_network_sets(tag_name=tag_name, tag_value=tag_value, tag_value_match_mode=tag_value_match_mode, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraNetworkSetApi->list_lora_network_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| Tag name for filtering the search (exact match). | [optional]
 **tag_value** | **str**| Tag search string for filtering the search. Required when &#x60;tag_name&#x60; has been specified. | [optional]
 **tag_value_match_mode** | **str**| Tag match mode. | [optional] if omitted the server will use the default value of "exact"
 **limit** | **int**| Maximum number of LoRa devices to retrieve. | [optional]
 **last_evaluated_key** | **str**| The ID of the last network set retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next device onward. | [optional]

### Return type

[**[LoraNetworkSet]**](LoraNetworkSet.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of LoRa network sets. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_lora_network_set_tags**
> LoraNetworkSet put_lora_network_set_tags(ns_id, tag_update_request)

Bulk Insert or Update LoRa network set tags.

Inserts/updates tags for the specified LoRa network set.

### Example


```python
import time
import soracom_api
from soracom_api.api import lora_network_set_api
from soracom_api.model.tag_update_request import TagUpdateRequest
from soracom_api.model.lora_network_set import LoraNetworkSet
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with soracom_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lora_network_set_api.LoraNetworkSetApi(api_client)
    ns_id = "ns_id_example" # str | ID of the target LoRa network set.
    tag_update_request = [
        TagUpdateRequest(
            tag_name="tag_name_example",
            tag_value="tag_value_example",
        ),
    ] # [TagUpdateRequest] | Array of tags to be inserted/updated.

    # example passing only required values which don't have defaults set
    try:
        # Bulk Insert or Update LoRa network set tags.
        api_response = api_instance.put_lora_network_set_tags(ns_id, tag_update_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraNetworkSetApi->put_lora_network_set_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_id** | **str**| ID of the target LoRa network set. |
 **tag_update_request** | [**[TagUpdateRequest]**](TagUpdateRequest.md)| Array of tags to be inserted/updated. |

### Return type

[**LoraNetworkSet**](LoraNetworkSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The LoRa network set&#39;s detailed information after the update. |  -  |
**404** | The specified LoRa network set does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_permission_from_lora_network_set**
> LoraNetworkSet revoke_permission_from_lora_network_set(ns_id, update_permission_request)

Revokes a permission from a LoRa network set.

Revokes a permission and removes an operator from the list of allowed operators in the network set.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import lora_network_set_api
from soracom_api.model.update_permission_request import UpdatePermissionRequest
from soracom_api.model.lora_network_set import LoraNetworkSet
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
    api_instance = lora_network_set_api.LoraNetworkSetApi(api_client)
    ns_id = "ns_id_example" # str | ID of the target LoRa network set.
    update_permission_request = UpdatePermissionRequest(
        operator_id="operator_id_example",
    ) # UpdatePermissionRequest | ID of the operator to be added to the list of allowed operators.

    # example passing only required values which don't have defaults set
    try:
        # Revokes a permission from a LoRa network set.
        api_response = api_instance.revoke_permission_from_lora_network_set(ns_id, update_permission_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling LoraNetworkSetApi->revoke_permission_from_lora_network_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ns_id** | **str**| ID of the target LoRa network set. |
 **update_permission_request** | [**UpdatePermissionRequest**](UpdatePermissionRequest.md)| ID of the operator to be added to the list of allowed operators. |

### Return type

[**LoraNetworkSet**](LoraNetworkSet.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Permission revoked from the network set. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

