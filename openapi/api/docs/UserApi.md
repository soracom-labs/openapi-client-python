# api.UserApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /operators/{operator_id}/users/{user_name} | Create User.
[**create_user_password**](UserApi.md#create_user_password) | **POST** /operators/{operator_id}/users/{user_name}/password | Create Password.
[**delete_user**](UserApi.md#delete_user) | **DELETE** /operators/{operator_id}/users/{user_name} | Delete User.
[**delete_user_auth_key**](UserApi.md#delete_user_auth_key) | **DELETE** /operators/{operator_id}/users/{user_name}/auth_keys/{auth_key_id} | Delete User AuthKey.
[**delete_user_password**](UserApi.md#delete_user_password) | **DELETE** /operators/{operator_id}/users/{user_name}/password | Delete Password.
[**enable_user_mfa**](UserApi.md#enable_user_mfa) | **POST** /operators/{operator_id}/users/{user_name}/mfa | Enable SAM user&#39;s MFA
[**generate_user_auth_key**](UserApi.md#generate_user_auth_key) | **POST** /operators/{operator_id}/users/{user_name}/auth_keys | Generate AuthKey.
[**get_default_permissions**](UserApi.md#get_default_permissions) | **GET** /operators/{operator_id}/users/default_permissions | Get the default permissions
[**get_user**](UserApi.md#get_user) | **GET** /operators/{operator_id}/users/{user_name} | Get User.
[**get_user_auth_key**](UserApi.md#get_user_auth_key) | **GET** /operators/{operator_id}/users/{user_name}/auth_keys/{auth_key_id} | Get AuthKey.
[**get_user_mfa_status**](UserApi.md#get_user_mfa_status) | **GET** /operators/{operator_id}/users/{user_name}/mfa | Get SAM user&#39;s MFA status
[**get_user_permission**](UserApi.md#get_user_permission) | **GET** /operators/{operator_id}/users/{user_name}/permission | Get User Permission.
[**has_user_password**](UserApi.md#has_user_password) | **GET** /operators/{operator_id}/users/{user_name}/password | Has User Password.
[**list_user_auth_keys**](UserApi.md#list_user_auth_keys) | **GET** /operators/{operator_id}/users/{user_name}/auth_keys | List User AuthKeys.
[**list_users**](UserApi.md#list_users) | **GET** /operators/{operator_id}/users | List Users.
[**revoke_user_mfa**](UserApi.md#revoke_user_mfa) | **DELETE** /operators/{operator_id}/users/{user_name}/mfa | Revoke SAM user&#39;s MFA
[**update_default_permissions**](UserApi.md#update_default_permissions) | **PUT** /operators/{operator_id}/users/default_permissions | Update the default permissions
[**update_user**](UserApi.md#update_user) | **PUT** /operators/{operator_id}/users/{user_name} | Update User.
[**update_user_password**](UserApi.md#update_user_password) | **PUT** /operators/{operator_id}/users/{user_name}/password | Update Password.
[**update_user_permission**](UserApi.md#update_user_permission) | **PUT** /operators/{operator_id}/users/{user_name}/permission | Update Permission to User.
[**verify_user_mfa**](UserApi.md#verify_user_mfa) | **POST** /operators/{operator_id}/users/{user_name}/mfa/verify | Verify SAM user&#39;s MFA OTP code when MFA activation phase


# **create_user**
> create_user(operator_id, user_name, create_user_request)

Create User.

Adds a new SAM user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.create_user_request import CreateUserRequest
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name
    create_user_request = CreateUserRequest(
        description="description_example",
    ) # CreateUserRequest | description

    # example passing only required values which don't have defaults set
    try:
        # Create User.
        api_instance.create_user(operator_id, user_name, create_user_request)
    except api.ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)| description |

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
**201** | A new user was added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_password**
> create_user_password(operator_id, user_name, create_user_password_request)

Create Password.

Creates a password for the SAM user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.create_user_password_request import CreateUserPasswordRequest
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name
    create_user_password_request = CreateUserPasswordRequest(
        password="password_example",
    ) # CreateUserPasswordRequest | password

    # example passing only required values which don't have defaults set
    try:
        # Create Password.
        api_instance.create_user_password(operator_id, user_name, create_user_password_request)
    except api.ApiException as e:
        print("Exception when calling UserApi->create_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |
 **create_user_password_request** | [**CreateUserPasswordRequest**](CreateUserPasswordRequest.md)| password |

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
**201** | Password for the SAM user was registered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(operator_id, user_name)

Delete User.

Deletes the SAM user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.api_call_error import APICallError
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name

    # example passing only required values which don't have defaults set
    try:
        # Delete User.
        api_instance.delete_user(operator_id, user_name)
    except api.ApiException as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The SAM user was deleted. |  -  |
**404** | SAM User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_auth_key**
> delete_user_auth_key(operator_id, user_name, auth_key_id)

Delete User AuthKey.

Deletes an AuthKey from the SAM user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.api_call_error import APICallError
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name
    auth_key_id = "auth_key_id_example" # str | auth_key_id

    # example passing only required values which don't have defaults set
    try:
        # Delete User AuthKey.
        api_instance.delete_user_auth_key(operator_id, user_name, auth_key_id)
    except api.ApiException as e:
        print("Exception when calling UserApi->delete_user_auth_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |
 **auth_key_id** | **str**| auth_key_id |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The AuthKey was deleted. |  -  |
**404** | AuthKey not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_password**
> delete_user_password(operator_id, user_name)

Delete Password.

Deletes the user's password.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.api_call_error import APICallError
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name

    # example passing only required values which don't have defaults set
    try:
        # Delete Password.
        api_instance.delete_user_password(operator_id, user_name)
    except api.ApiException as e:
        print("Exception when calling UserApi->delete_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The user&#39;s password was deleted. |  -  |
**404** | Password registration is required. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_user_mfa**
> EnableMFAOTPResponse enable_user_mfa(operator_id, user_name)

Enable SAM user's MFA

Enable SAM user's MFA

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.enable_mfaotp_response import EnableMFAOTPResponse
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | Operator ID
    user_name = "user_name_example" # str | SAM user name

    # example passing only required values which don't have defaults set
    try:
        # Enable SAM user's MFA
        api_response = api_instance.enable_user_mfa(operator_id, user_name)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling UserApi->enable_user_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| Operator ID |
 **user_name** | **str**| SAM user name |

### Return type

[**EnableMFAOTPResponse**](EnableMFAOTPResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_user_auth_key**
> GenerateUserAuthKeyResponse generate_user_auth_key(operator_id, user_name)

Generate AuthKey.

Generates an AuthKey for the SAM user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.generate_user_auth_key_response import GenerateUserAuthKeyResponse
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name

    # example passing only required values which don't have defaults set
    try:
        # Generate AuthKey.
        api_response = api_instance.generate_user_auth_key(operator_id, user_name)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling UserApi->generate_user_auth_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |

### Return type

[**GenerateUserAuthKeyResponse**](GenerateUserAuthKeyResponse.md)

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

# **get_default_permissions**
> GetDefaultPermissionsResponse get_default_permissions(operator_id)

Get the default permissions

Get the default permissions rule that is applied to all of the SAM users

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.get_default_permissions_response import GetDefaultPermissionsResponse
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | Operator ID

    # example passing only required values which don't have defaults set
    try:
        # Get the default permissions
        api_response = api_instance.get_default_permissions(operator_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling UserApi->get_default_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| Operator ID |

### Return type

[**GetDefaultPermissionsResponse**](GetDefaultPermissionsResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Not privileged |  -  |
**404** | Operator Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> UserDetailResponse get_user(operator_id, user_name)

Get User.

Returns a SAM user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name

    # example passing only required values which don't have defaults set
    try:
        # Get User.
        api_response = api_instance.get_user(operator_id, user_name)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |

### Return type

[**UserDetailResponse**](UserDetailResponse.md)

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

# **get_user_auth_key**
> AuthKeyResponse get_user_auth_key(operator_id, user_name, auth_key_id)

Get AuthKey.

Returns the SAM user's AuthKey.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.auth_key_response import AuthKeyResponse
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name
    auth_key_id = "auth_key_id_example" # str | auth_key_id

    # example passing only required values which don't have defaults set
    try:
        # Get AuthKey.
        api_response = api_instance.get_user_auth_key(operator_id, user_name, auth_key_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling UserApi->get_user_auth_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |
 **auth_key_id** | **str**| auth_key_id |

### Return type

[**AuthKeyResponse**](AuthKeyResponse.md)

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

# **get_user_mfa_status**
> MFAStatusOfUseResponse get_user_mfa_status(operator_id, user_name)

Get SAM user's MFA status

Get SAM user's MFA status

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.mfa_status_of_use_response import MFAStatusOfUseResponse
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | Operator ID
    user_name = "user_name_example" # str | SAM user name

    # example passing only required values which don't have defaults set
    try:
        # Get SAM user's MFA status
        api_response = api_instance.get_user_mfa_status(operator_id, user_name)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling UserApi->get_user_mfa_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| Operator ID |
 **user_name** | **str**| SAM user name |

### Return type

[**MFAStatusOfUseResponse**](MFAStatusOfUseResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_permission**
> GetUserPermissionResponse get_user_permission(operator_id, user_name)

Get User Permission.

Retrieves the SAM user's permissions.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.get_user_permission_response import GetUserPermissionResponse
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name

    # example passing only required values which don't have defaults set
    try:
        # Get User Permission.
        api_response = api_instance.get_user_permission(operator_id, user_name)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling UserApi->get_user_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |

### Return type

[**GetUserPermissionResponse**](GetUserPermissionResponse.md)

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

# **has_user_password**
> GetUserPasswordResponse has_user_password(operator_id, user_name)

Has User Password.

Retrieves whether the SAM user has a password or not.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.get_user_password_response import GetUserPasswordResponse
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name

    # example passing only required values which don't have defaults set
    try:
        # Has User Password.
        api_response = api_instance.has_user_password(operator_id, user_name)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling UserApi->has_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |

### Return type

[**GetUserPasswordResponse**](GetUserPasswordResponse.md)

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

# **list_user_auth_keys**
> [AuthKeyResponse] list_user_auth_keys(operator_id, user_name)

List User AuthKeys.

Returns the SAM user's AuthKey list.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.auth_key_response import AuthKeyResponse
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name

    # example passing only required values which don't have defaults set
    try:
        # List User AuthKeys.
        api_response = api_instance.list_user_auth_keys(operator_id, user_name)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling UserApi->list_user_auth_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |

### Return type

[**[AuthKeyResponse]**](AuthKeyResponse.md)

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

# **list_users**
> [UserDetailResponse] list_users(operator_id)

List Users.

Returns a list of SAM users.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # List Users.
        api_response = api_instance.list_users(operator_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling UserApi->list_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

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

# **revoke_user_mfa**
> revoke_user_mfa(operator_id, user_name)

Revoke SAM user's MFA

Revoke SAM user's MFA

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | Operator ID
    user_name = "user_name_example" # str | SAM user name

    # example passing only required values which don't have defaults set
    try:
        # Revoke SAM user's MFA
        api_instance.revoke_user_mfa(operator_id, user_name)
    except api.ApiException as e:
        print("Exception when calling UserApi->revoke_user_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| Operator ID |
 **user_name** | **str**| SAM user name |

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
**204** | Revoked |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_permissions**
> update_default_permissions(operator_id, update_default_permissions_request)

Update the default permissions

Update the default permissions rule that is applied to all of the SAM

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.update_default_permissions_request import UpdateDefaultPermissionsRequest
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | Operator ID
    update_default_permissions_request = UpdateDefaultPermissionsRequest(
        permissions="permissions_example",
    ) # UpdateDefaultPermissionsRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Update the default permissions
        api_instance.update_default_permissions(operator_id, update_default_permissions_request)
    except api.ApiException as e:
        print("Exception when calling UserApi->update_default_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| Operator ID |
 **update_default_permissions_request** | [**UpdateDefaultPermissionsRequest**](UpdateDefaultPermissionsRequest.md)| request |

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
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Not privileged |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> update_user(operator_id, user_name, update_user_request)

Update User.

Updates the SAM user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.api_call_error import APICallError
from api.model.update_user_request import UpdateUserRequest
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name
    update_user_request = UpdateUserRequest(
        description="description_example",
    ) # UpdateUserRequest | description

    # example passing only required values which don't have defaults set
    try:
        # Update User.
        api_instance.update_user(operator_id, user_name, update_user_request)
    except api.ApiException as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |
 **update_user_request** | [**UpdateUserRequest**](UpdateUserRequest.md)| description |

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | SAM User not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_password**
> update_user_password(operator_id, user_name, update_password_request)

Update Password.

Updates the password of the SAM user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.update_password_request import UpdatePasswordRequest
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name
    update_password_request = UpdatePasswordRequest(
        current_password="current_password_example",
        new_password="new_password_example",
    ) # UpdatePasswordRequest | password

    # example passing only required values which don't have defaults set
    try:
        # Update Password.
        api_instance.update_user_password(operator_id, user_name, update_password_request)
    except api.ApiException as e:
        print("Exception when calling UserApi->update_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |
 **update_password_request** | [**UpdatePasswordRequest**](UpdatePasswordRequest.md)| password |

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

# **update_user_permission**
> update_user_permission(operator_id, user_name, set_user_permission_request)

Update Permission to User.

Updates the SAM user's permissions.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.set_user_permission_request import SetUserPermissionRequest
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    user_name = "user_name_example" # str | user_name
    set_user_permission_request = SetUserPermissionRequest(
        description="description_example",
        permission="permission_example",
    ) # SetUserPermissionRequest | permission

    # example passing only required values which don't have defaults set
    try:
        # Update Permission to User.
        api_instance.update_user_permission(operator_id, user_name, set_user_permission_request)
    except api.ApiException as e:
        print("Exception when calling UserApi->update_user_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **user_name** | **str**| user_name |
 **set_user_permission_request** | [**SetUserPermissionRequest**](SetUserPermissionRequest.md)| permission |

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

# **verify_user_mfa**
> verify_user_mfa(operator_id, user_name, mfa_authentication_request)

Verify SAM user's MFA OTP code when MFA activation phase

Verify SAM user's MFA OTP code when MFA activation phase

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import user_api
from api.model.mfa_authentication_request import MFAAuthenticationRequest
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
    api_instance = user_api.UserApi(api_client)
    operator_id = "operator_id_example" # str | Operator ID
    user_name = "user_name_example" # str | SAM user name
    mfa_authentication_request = MFAAuthenticationRequest(
        mfa_otp_code="mfa_otp_code_example",
    ) # MFAAuthenticationRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Verify SAM user's MFA OTP code when MFA activation phase
        api_instance.verify_user_mfa(operator_id, user_name, mfa_authentication_request)
    except api.ApiException as e:
        print("Exception when calling UserApi->verify_user_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| Operator ID |
 **user_name** | **str**| SAM user name |
 **mfa_authentication_request** | [**MFAAuthenticationRequest**](MFAAuthenticationRequest.md)| request |

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
**204** | Verified |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

