# api.RoleApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attach_role**](RoleApi.md#attach_role) | **POST** /operators/{operator_id}/users/{user_name}/roles | Attach Role to User.
[**create_role**](RoleApi.md#create_role) | **POST** /operators/{operator_id}/roles/{role_id} | Create Role.
[**delete_role**](RoleApi.md#delete_role) | **DELETE** /operators/{operator_id}/roles/{role_id} | Delete Role.
[**detach_role**](RoleApi.md#detach_role) | **DELETE** /operators/{operator_id}/users/{user_name}/roles/{role_id} | Detach Role from User.
[**get_role**](RoleApi.md#get_role) | **GET** /operators/{operator_id}/roles/{role_id} | Get Role.
[**list_role_attached_users**](RoleApi.md#list_role_attached_users) | **GET** /operators/{operator_id}/roles/{role_id}/users | List Role Attached Users.
[**list_roles**](RoleApi.md#list_roles) | **GET** /operators/{operator_id}/roles | List Roles.
[**list_user_roles**](RoleApi.md#list_user_roles) | **GET** /operators/{operator_id}/users/{user_name}/roles | List User Roles.
[**update_role**](RoleApi.md#update_role) | **PUT** /operators/{operator_id}/roles/{role_id} | Update Role.


# **attach_role**
> attach_role(operator_id, user_name, attach_role_request)

Attach Role to User.

Attaches a role to a user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import role_api
from api.model.attach_role_request import AttachRoleRequest
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
    api_instance = role_api.RoleApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name
    attach_role_request = AttachRoleRequest(
        role_id="role_id_example",
    ) # AttachRoleRequest | role_id

    # example passing only required values which don't have defaults set
    try:
        # Attach Role to User.
        api_instance.attach_role(operator_id, user_name, attach_role_request)
    except api.ApiException as e:
        print("Exception when calling RoleApi->attach_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |
 **attach_role_request** | [**AttachRoleRequest**](AttachRoleRequest.md)| role_id |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> CreateRoleResponse create_role(operator_id, role_id, create_or_update_role_request)

Create Role.

Adds a new role.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import role_api
from api.model.create_role_response import CreateRoleResponse
from api.model.create_or_update_role_request import CreateOrUpdateRoleRequest
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
    api_instance = role_api.RoleApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    role_id = "role_id_example" # str | role_id
    create_or_update_role_request = CreateOrUpdateRoleRequest(
        description="description_example",
        permission="permission_example",
    ) # CreateOrUpdateRoleRequest | permission

    # example passing only required values which don't have defaults set
    try:
        # Create Role.
        api_response = api_instance.create_role(operator_id, role_id, create_or_update_role_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling RoleApi->create_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **role_id** | **str**| role_id |
 **create_or_update_role_request** | [**CreateOrUpdateRoleRequest**](CreateOrUpdateRoleRequest.md)| permission |

### Return type

[**CreateRoleResponse**](CreateRoleResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(operator_id, role_id)

Delete Role.

Deletes a role.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import role_api
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
    api_instance = role_api.RoleApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    role_id = "role_id_example" # str | role_id

    # example passing only required values which don't have defaults set
    try:
        # Delete Role.
        api_instance.delete_role(operator_id, role_id)
    except api.ApiException as e:
        print("Exception when calling RoleApi->delete_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **role_id** | **str**| role_id |

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
**204** | The role was deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **detach_role**
> detach_role(operator_id, user_name, role_id)

Detach Role from User.

Detaches a role from a user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import role_api
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
    api_instance = role_api.RoleApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name
    role_id = "role_id_example" # str | role_id

    # example passing only required values which don't have defaults set
    try:
        # Detach Role from User.
        api_instance.detach_role(operator_id, user_name, role_id)
    except api.ApiException as e:
        print("Exception when calling RoleApi->detach_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |
 **role_id** | **str**| role_id |

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

# **get_role**
> RoleResponse get_role(operator_id, role_id)

Get Role.

Retrieves a role.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import role_api
from api.model.role_response import RoleResponse
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
    api_instance = role_api.RoleApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    role_id = "role_id_example" # str | role_id

    # example passing only required values which don't have defaults set
    try:
        # Get Role.
        api_response = api_instance.get_role(operator_id, role_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling RoleApi->get_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **role_id** | **str**| role_id |

### Return type

[**RoleResponse**](RoleResponse.md)

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

# **list_role_attached_users**
> [UserDetailResponse] list_role_attached_users(operator_id, role_id)

List Role Attached Users.

Retrieves a list of users attached to a role.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import role_api
from api.model.user_detail_response import UserDetailResponse
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
    api_instance = role_api.RoleApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    role_id = "role_id_example" # str | role_id

    # example passing only required values which don't have defaults set
    try:
        # List Role Attached Users.
        api_response = api_instance.list_role_attached_users(operator_id, role_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling RoleApi->list_role_attached_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **role_id** | **str**| role_id |

### Return type

[**[UserDetailResponse]**](UserDetailResponse.md)

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

# **list_roles**
> [ListRolesResponse] list_roles(operator_id)

List Roles.

Returns a list of roles.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import role_api
from api.model.list_roles_response import ListRolesResponse
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
    api_instance = role_api.RoleApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # List Roles.
        api_response = api_instance.list_roles(operator_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling RoleApi->list_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

### Return type

[**[ListRolesResponse]**](ListRolesResponse.md)

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

# **list_user_roles**
> [RoleResponse] list_user_roles(operator_id, user_name)

List User Roles.

Retrieves a list of the user's roles.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import role_api
from api.model.role_response import RoleResponse
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
    api_instance = role_api.RoleApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name

    # example passing only required values which don't have defaults set
    try:
        # List User Roles.
        api_response = api_instance.list_user_roles(operator_id, user_name)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling RoleApi->list_user_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |

### Return type

[**[RoleResponse]**](RoleResponse.md)

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

# **update_role**
> update_role(operator_id, role_id, create_or_update_role_request)

Update Role.

Edits a role.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import role_api
from api.model.create_or_update_role_request import CreateOrUpdateRoleRequest
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
    api_instance = role_api.RoleApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    role_id = "role_id_example" # str | role_id
    create_or_update_role_request = CreateOrUpdateRoleRequest(
        description="description_example",
        permission="permission_example",
    ) # CreateOrUpdateRoleRequest | permission

    # example passing only required values which don't have defaults set
    try:
        # Update Role.
        api_instance.update_role(operator_id, role_id, create_or_update_role_request)
    except api.ApiException as e:
        print("Exception when calling RoleApi->update_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **role_id** | **str**| role_id |
 **create_or_update_role_request** | [**CreateOrUpdateRoleRequest**](CreateOrUpdateRoleRequest.md)| permission |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

