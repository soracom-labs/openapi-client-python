# api.GroupApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupApi.md#create_group) | **POST** /groups | Create Group.
[**delete_configuration_namespace**](GroupApi.md#delete_configuration_namespace) | **DELETE** /groups/{group_id}/configuration/{namespace} | Delete Group Configuration Namespace.
[**delete_configuration_parameter**](GroupApi.md#delete_configuration_parameter) | **DELETE** /groups/{group_id}/configuration/{namespace}/{name} | Delete Group Configuration Parameters.
[**delete_group**](GroupApi.md#delete_group) | **DELETE** /groups/{group_id} | Delete Group.
[**delete_group_tag**](GroupApi.md#delete_group_tag) | **DELETE** /groups/{group_id}/tags/{tag_name} | Delete Group Tag.
[**get_group**](GroupApi.md#get_group) | **GET** /groups/{group_id} | Get Group.
[**list_groups**](GroupApi.md#list_groups) | **GET** /groups | List Groups.
[**list_subscribers_in_group**](GroupApi.md#list_subscribers_in_group) | **GET** /groups/{group_id}/subscribers | List Subscribers in a group.
[**put_configuration_parameters**](GroupApi.md#put_configuration_parameters) | **PUT** /groups/{group_id}/configuration/{namespace} | Update Group Configuration Parameters.
[**put_group_tags**](GroupApi.md#put_group_tags) | **PUT** /groups/{group_id}/tags | Update Group Tags.


# **create_group**
> Group create_group(create_group_request)

Create Group.

Create a new group.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import group_api
from api.model.group import Group
from api.model.create_group_request import CreateGroupRequest
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
    api_instance = group_api.GroupApi(api_client)
    create_group_request = CreateGroupRequest(
        tags=TagSet(
            key="key_example",
        ),
    ) # CreateGroupRequest | Tags for group to be created.

    # example passing only required values which don't have defaults set
    try:
        # Create Group.
        api_response = api_instance.create_group(create_group_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GroupApi->create_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_group_request** | [**CreateGroupRequest**](CreateGroupRequest.md)| Tags for group to be created. |

### Return type

[**Group**](Group.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_configuration_namespace**
> delete_configuration_namespace(group_id, namespace)

Delete Group Configuration Namespace.

Delete a namespace for the specified group.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import group_api
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "group_id_example" # str | Target group.
    namespace = "SoracomAir" # str | Namespace to be deleted.

    # example passing only required values which don't have defaults set
    try:
        # Delete Group Configuration Namespace.
        api_instance.delete_configuration_namespace(group_id, namespace)
    except api.ApiException as e:
        print("Exception when calling GroupApi->delete_configuration_namespace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Target group. |
 **namespace** | **str**| Namespace to be deleted. |

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
**204** | The namespace was successfully deleted. |  -  |
**400** | The specified namespace does not exist. |  -  |
**404** | The specified group does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_configuration_parameter**
> delete_configuration_parameter(group_id, namespace, name)

Delete Group Configuration Parameters.

Delete parameters for the specified group.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import group_api
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "group_id_example" # str | Target group.
    namespace = "SoracomAir" # str | Namespace of target parameters.
    name = "name_example" # str | Parameter name to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().)

    # example passing only required values which don't have defaults set
    try:
        # Delete Group Configuration Parameters.
        api_instance.delete_configuration_parameter(group_id, namespace, name)
    except api.ApiException as e:
        print("Exception when calling GroupApi->delete_configuration_parameter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Target group. |
 **namespace** | **str**| Namespace of target parameters. |
 **name** | **str**| Parameter name to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().) |

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
**204** | The parameter was successfully deleted. |  -  |
**404** | The specified group does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id)

Delete Group.

Deletes the specified group by group ID

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import group_api
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "group_id_example" # str | Target group ID.

    # example passing only required values which don't have defaults set
    try:
        # Delete Group.
        api_instance.delete_group(group_id)
    except api.ApiException as e:
        print("Exception when calling GroupApi->delete_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Target group ID. |

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
**204** | Deletion of specified group complete. |  -  |
**404** | The specified group does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_tag**
> delete_group_tag(group_id, tag_name)

Delete Group Tag.

Deletes tag from the specified group.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import group_api
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "group_id_example" # str | Target group ID.
    tag_name = "tag_name_example" # str | Tag name to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().)

    # example passing only required values which don't have defaults set
    try:
        # Delete Group Tag.
        api_instance.delete_group_tag(group_id, tag_name)
    except api.ApiException as e:
        print("Exception when calling GroupApi->delete_group_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Target group ID. |
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
**204** | Tag deletion complete. |  -  |
**404** | The specified subscriber or the tag does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> Group get_group(group_id)

Get Group.

Returns the group specified by the group ID.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import group_api
from api.model.group import Group
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "group_id_example" # str | Target group ID.

    # example passing only required values which don't have defaults set
    try:
        # Get Group.
        api_response = api_instance.get_group(group_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GroupApi->get_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Target group ID. |

### Return type

[**Group**](Group.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The specified group. |  -  |
**404** | The specified group does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> [Group] list_groups()

List Groups.

Returns a list of groups.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import group_api
from api.model.group import Group
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
    api_instance = group_api.GroupApi(api_client)
    tag_name = "tag_name_example" # str | Tag name of the group. Filters through all groups that exactly match the tag name. When tag_name is specified, tag_value is required. (optional)
    tag_value = "tag_value_example" # str | Tag value of the groups. (optional)
    tag_value_match_mode = "exact" # str | Tag match mode. (optional) if omitted the server will use the default value of "exact"
    limit = 1 # int | Maximum number of results per response page. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The last Group ID retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next group onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Groups.
        api_response = api_instance.list_groups(tag_name=tag_name, tag_value=tag_value, tag_value_match_mode=tag_value_match_mode, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GroupApi->list_groups: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| Tag name of the group. Filters through all groups that exactly match the tag name. When tag_name is specified, tag_value is required. | [optional]
 **tag_value** | **str**| Tag value of the groups. | [optional]
 **tag_value_match_mode** | **str**| Tag match mode. | [optional] if omitted the server will use the default value of "exact"
 **limit** | **int**| Maximum number of results per response page. | [optional]
 **last_evaluated_key** | **str**| The last Group ID retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next group onward. | [optional]

### Return type

[**[Group]**](Group.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of groups. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscribers_in_group**
> Group list_subscribers_in_group(group_id)

List Subscribers in a group.

Returns a list of subscribers that belong to the specified group by group ID.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import group_api
from api.model.group import Group
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "group_id_example" # str | Target group ID.
    limit = 1 # int | Maximum number of results per response page. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The IMSI of the last subscriber retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next subscriber onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Subscribers in a group.
        api_response = api_instance.list_subscribers_in_group(group_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GroupApi->list_subscribers_in_group: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Subscribers in a group.
        api_response = api_instance.list_subscribers_in_group(group_id, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GroupApi->list_subscribers_in_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Target group ID. |
 **limit** | **int**| Maximum number of results per response page. | [optional]
 **last_evaluated_key** | **str**| The IMSI of the last subscriber retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next subscriber onward. | [optional]

### Return type

[**Group**](Group.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Target group ID |  -  |
**404** | The specified group does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_configuration_parameters**
> Group put_configuration_parameters(group_id, namespace, group_configuration_update_request)

Update Group Configuration Parameters.

Adds/updates parameters for the specified group.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import group_api
from api.model.group import Group
from api.model.group_configuration_update_request import GroupConfigurationUpdateRequest
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "group_id_example" # str | Target group.
    namespace = "SoracomAir" # str | Target configuration.
    group_configuration_update_request = [
        GroupConfigurationUpdateRequest(
            key="key_example",
            value="value_example",
        ),
    ] # [GroupConfigurationUpdateRequest] | Array of values for target object to be updated.

    # example passing only required values which don't have defaults set
    try:
        # Update Group Configuration Parameters.
        api_response = api_instance.put_configuration_parameters(group_id, namespace, group_configuration_update_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GroupApi->put_configuration_parameters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Target group. |
 **namespace** | **str**| Target configuration. |
 **group_configuration_update_request** | [**[GroupConfigurationUpdateRequest]**](GroupConfigurationUpdateRequest.md)| Array of values for target object to be updated. |

### Return type

[**Group**](Group.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The group after the update. |  -  |
**404** | The specified group does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_group_tags**
> Subscriber put_group_tags(group_id, tag_update_request)

Update Group Tags.

Adds/updates tags of specified configuration group.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import group_api
from api.model.tag_update_request import TagUpdateRequest
from api.model.subscriber import Subscriber
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
    api_instance = group_api.GroupApi(api_client)
    group_id = "group_id_example" # str | Target group ID.
    tag_update_request = [
        TagUpdateRequest(
            tag_name="tag_name_example",
            tag_value="tag_value_example",
        ),
    ] # [TagUpdateRequest] | Array of values for tags to be updated.

    # example passing only required values which don't have defaults set
    try:
        # Update Group Tags.
        api_response = api_instance.put_group_tags(group_id, tag_update_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling GroupApi->put_group_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| Target group ID. |
 **tag_update_request** | [**[TagUpdateRequest]**](TagUpdateRequest.md)| Array of values for tags to be updated. |

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

