# api.LagoonApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_lagoon_user**](LagoonApi.md#create_lagoon_user) | **POST** /lagoon/users | Create a SORACOM Lagoon user
[**delete_lagoon_user**](LagoonApi.md#delete_lagoon_user) | **DELETE** /lagoon/users/{lagoon_user_id} | Delete a SORACOM Lagoon user
[**get_image_link**](LagoonApi.md#get_image_link) | **GET** /lagoon/image/link | Get a custom icon image link of SORACOM Lagoon
[**get_lagoon_migration_info**](LagoonApi.md#get_lagoon_migration_info) | **GET** /lagoon/migration | Get the version migration information for SORACOM Lagoon
[**initialize_lagoon_dashboard_permissions**](LagoonApi.md#initialize_lagoon_dashboard_permissions) | **POST** /lagoon/dashboards/{dashboard_id}/permissions/init | Update permissions to the initial state for a dashboard of SORACOM Lagoon
[**list_lagoon_dashboards_permissions**](LagoonApi.md#list_lagoon_dashboards_permissions) | **GET** /lagoon/dashboards/permissions | List permissions for all SORACOM Lagoon dashboards
[**list_lagoon_license_pack_status**](LagoonApi.md#list_lagoon_license_pack_status) | **GET** /lagoon/license_packs | Get the status of active SORACOM Lagoon license packs
[**list_lagoon_users**](LagoonApi.md#list_lagoon_users) | **GET** /lagoon/users | List SORACOM Lagoon users that belong to operator
[**migrate_lagoon**](LagoonApi.md#migrate_lagoon) | **POST** /lagoon/migration | Migrate SORACOM Lagoon version
[**register_lagoon**](LagoonApi.md#register_lagoon) | **POST** /lagoon/register | Register (activate) SORACOM Lagoon
[**terminate_lagoon**](LagoonApi.md#terminate_lagoon) | **POST** /lagoon/terminate | Terminate (deactivate) SORACOM Lagoon
[**update_lagoon_dashboard_permissions**](LagoonApi.md#update_lagoon_dashboard_permissions) | **PUT** /lagoon/dashboards/{dashboard_id}/permissions | Update permissions for a dashboard of SORACOM Lagoon
[**update_lagoon_license_pack**](LagoonApi.md#update_lagoon_license_pack) | **PUT** /lagoon/license_packs | Update the quantities for license packs of SORACOM Lagoon
[**update_lagoon_plan**](LagoonApi.md#update_lagoon_plan) | **PUT** /lagoon/plan | Update the plan of SORACOM Lagoon
[**update_lagoon_user_email**](LagoonApi.md#update_lagoon_user_email) | **PUT** /lagoon/users/{lagoon_user_id}/email | Update email address of a SORACOM Lagoon user
[**update_lagoon_user_password**](LagoonApi.md#update_lagoon_user_password) | **PUT** /lagoon/users/{lagoon_user_id}/password | Update password of a SORACOM Lagoon user
[**update_lagoon_user_permission**](LagoonApi.md#update_lagoon_user_permission) | **PUT** /lagoon/users/{lagoon_user_id}/permission | Update permission of a SORACOM Lagoon user


# **create_lagoon_user**
> LagoonUserCreationResponse create_lagoon_user(lagoon_user_creation_request)

Create a SORACOM Lagoon user

Create a SORACOM Lagoon user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_user_creation_response import LagoonUserCreationResponse
from api.model.lagoon_user_creation_request import LagoonUserCreationRequest
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
    api_instance = lagoon_api.LagoonApi(api_client)
    lagoon_user_creation_request = LagoonUserCreationRequest(
        role="Viewer",
        user_email="user_email_example",
        user_password="user_password_example",
    ) # LagoonUserCreationRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Create a SORACOM Lagoon user
        api_response = api_instance.create_lagoon_user(lagoon_user_creation_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->create_lagoon_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lagoon_user_creation_request** | [**LagoonUserCreationRequest**](LagoonUserCreationRequest.md)| request |

### Return type

[**LagoonUserCreationResponse**](LagoonUserCreationResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_lagoon_user**
> delete_lagoon_user(lagoon_user_id)

Delete a SORACOM Lagoon user

Delete a SORACOM Lagoon user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lagoon_api
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
    api_instance = lagoon_api.LagoonApi(api_client)
    lagoon_user_id = 1 # int | Target ID of the lagoon user

    # example passing only required values which don't have defaults set
    try:
        # Delete a SORACOM Lagoon user
        api_instance.delete_lagoon_user(lagoon_user_id)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->delete_lagoon_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lagoon_user_id** | **int**| Target ID of the lagoon user |

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
**204** | Deleted |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_image_link**
> str get_image_link()

Get a custom icon image link of SORACOM Lagoon

Get a custom icon image link of SORACOM Lagoon

### Example


```python
import time
import api
from api.api import lagoon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lagoon_api.LagoonApi(api_client)
    classic = True # bool | If the value is true, a request will be issued to Lagoon Classic. This is only valid if both Lagoon and Lagoon Classic are enabled. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a custom icon image link of SORACOM Lagoon
        api_response = api_instance.get_image_link(classic=classic)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->get_image_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classic** | **bool**| If the value is true, a request will be issued to Lagoon Classic. This is only valid if both Lagoon and Lagoon Classic are enabled. | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_lagoon_migration_info**
> get_lagoon_migration_info(lagoon_plan_changing_request)

Get the version migration information for SORACOM Lagoon

Get the version migration information for SORACOM Lagoon. Only the root account can operate this.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_plan_changing_request import LagoonPlanChangingRequest
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
    api_instance = lagoon_api.LagoonApi(api_client)
    lagoon_plan_changing_request = LagoonPlanChangingRequest(
        plan="maker",
    ) # LagoonPlanChangingRequest | req

    # example passing only required values which don't have defaults set
    try:
        # Get the version migration information for SORACOM Lagoon
        api_instance.get_lagoon_migration_info(lagoon_plan_changing_request)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->get_lagoon_migration_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lagoon_plan_changing_request** | [**LagoonPlanChangingRequest**](LagoonPlanChangingRequest.md)| req |

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

# **initialize_lagoon_dashboard_permissions**
> initialize_lagoon_dashboard_permissions(dashboard_id)

Update permissions to the initial state for a dashboard of SORACOM Lagoon

Update permissions to the initial state for a dashboard of SORACOM Lagoon

### Example


```python
import time
import api
from api.api import lagoon_api
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lagoon_api.LagoonApi(api_client)
    dashboard_id = 1 # int | dashboard_id
    classic = True # bool | If the value is true, a request will be issued to Lagoon Classic. This is only valid if both Lagoon and Lagoon Classic are enabled. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update permissions to the initial state for a dashboard of SORACOM Lagoon
        api_instance.initialize_lagoon_dashboard_permissions(dashboard_id)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->initialize_lagoon_dashboard_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update permissions to the initial state for a dashboard of SORACOM Lagoon
        api_instance.initialize_lagoon_dashboard_permissions(dashboard_id, classic=classic)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->initialize_lagoon_dashboard_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| dashboard_id |
 **classic** | **bool**| If the value is true, a request will be issued to Lagoon Classic. This is only valid if both Lagoon and Lagoon Classic are enabled. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Updated |  -  |
**400** | Bad request |  -  |
**403** | Unauthorized operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lagoon_dashboards_permissions**
> [LagoonDashboardPermissionsResponse] list_lagoon_dashboards_permissions()

List permissions for all SORACOM Lagoon dashboards

List permissions for all SORACOM Lagoon dashboards

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_dashboard_permissions_response import LagoonDashboardPermissionsResponse
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
    api_instance = lagoon_api.LagoonApi(api_client)
    classic = True # bool | If the value is true, a request will be issued to Lagoon Classic. This is only valid if both Lagoon and Lagoon Classic are enabled. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List permissions for all SORACOM Lagoon dashboards
        api_response = api_instance.list_lagoon_dashboards_permissions(classic=classic)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->list_lagoon_dashboards_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classic** | **bool**| If the value is true, a request will be issued to Lagoon Classic. This is only valid if both Lagoon and Lagoon Classic are enabled. | [optional]

### Return type

[**[LagoonDashboardPermissionsResponse]**](LagoonDashboardPermissionsResponse.md)

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

# **list_lagoon_license_pack_status**
> [LagoonLicensePackStatusResponse] list_lagoon_license_pack_status()

Get the status of active SORACOM Lagoon license packs

Get the status of active SORACOM Lagoon license packs

### Example


```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_license_pack_status_response import LagoonLicensePackStatusResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lagoon_api.LagoonApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the status of active SORACOM Lagoon license packs
        api_response = api_instance.list_lagoon_license_pack_status()
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->list_lagoon_license_pack_status: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[LagoonLicensePackStatusResponse]**](LagoonLicensePackStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_lagoon_users**
> [LagoonUser] list_lagoon_users()

List SORACOM Lagoon users that belong to operator

List SORACOM Lagoon users that belong to operator.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_user import LagoonUser
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
    api_instance = lagoon_api.LagoonApi(api_client)
    classic = True # bool | If the value is true, a request will be issued to Lagoon Classic. This is only valid if both Lagoon and Lagoon Classic are enabled. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List SORACOM Lagoon users that belong to operator
        api_response = api_instance.list_lagoon_users(classic=classic)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->list_lagoon_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **classic** | **bool**| If the value is true, a request will be issued to Lagoon Classic. This is only valid if both Lagoon and Lagoon Classic are enabled. | [optional]

### Return type

[**[LagoonUser]**](LagoonUser.md)

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

# **migrate_lagoon**
> migrate_lagoon(lagoon_migration_from_classic_request)

Migrate SORACOM Lagoon version

Migrate SORACOM Lagoon version. Only the root account can operate this.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_migration_from_classic_request import LagoonMigrationFromClassicRequest
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
    api_instance = lagoon_api.LagoonApi(api_client)
    lagoon_migration_from_classic_request = LagoonMigrationFromClassicRequest(
        dashboard_ids=[
            "dashboard_ids_example",
        ],
    ) # LagoonMigrationFromClassicRequest | req

    # example passing only required values which don't have defaults set
    try:
        # Migrate SORACOM Lagoon version
        api_instance.migrate_lagoon(lagoon_migration_from_classic_request)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->migrate_lagoon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lagoon_migration_from_classic_request** | [**LagoonMigrationFromClassicRequest**](LagoonMigrationFromClassicRequest.md)| req |

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

# **register_lagoon**
> LagoonRegistrationResponse register_lagoon(lagoon_registration_request)

Register (activate) SORACOM Lagoon

Register (activate) SORACOM Lagoon. This API is only allowed to operate by root account.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_registration_request import LagoonRegistrationRequest
from api.model.lagoon_registration_response import LagoonRegistrationResponse
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
    api_instance = lagoon_api.LagoonApi(api_client)
    lagoon_registration_request = LagoonRegistrationRequest(
        plan="free",
        user_password="user_password_example",
    ) # LagoonRegistrationRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Register (activate) SORACOM Lagoon
        api_response = api_instance.register_lagoon(lagoon_registration_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->register_lagoon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lagoon_registration_request** | [**LagoonRegistrationRequest**](LagoonRegistrationRequest.md)| request |

### Return type

[**LagoonRegistrationResponse**](LagoonRegistrationResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Registered |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_lagoon**
> terminate_lagoon()

Terminate (deactivate) SORACOM Lagoon

Terminate (deactivate) SORACOM Lagoon.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lagoon_api
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
    api_instance = lagoon_api.LagoonApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Terminate (deactivate) SORACOM Lagoon
        api_instance.terminate_lagoon()
    except api.ApiException as e:
        print("Exception when calling LagoonApi->terminate_lagoon: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**204** | Terminated |  -  |
**400** | Bad request |  -  |
**404** | Operator not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lagoon_dashboard_permissions**
> update_lagoon_dashboard_permissions(dashboard_id, lagoon_dashboard_permissions_updating_request)

Update permissions for a dashboard of SORACOM Lagoon

Update permissions for a dashboard of SORACOM Lagoon

### Example


```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_dashboard_permissions_updating_request import LagoonDashboardPermissionsUpdatingRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lagoon_api.LagoonApi(api_client)
    dashboard_id = 1 # int | dashboard_id
    lagoon_dashboard_permissions_updating_request = LagoonDashboardPermissionsUpdatingRequest(
        permissions=[
            LagoonDashboardPermissionsUpdatingRequestPermissions(
                permission="permission_example",
                user_id=1,
            ),
        ],
    ) # LagoonDashboardPermissionsUpdatingRequest | req
    classic = True # bool | If the value is true, a request will be issued to Lagoon Classic. This is only valid if both Lagoon and Lagoon Classic are enabled. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update permissions for a dashboard of SORACOM Lagoon
        api_instance.update_lagoon_dashboard_permissions(dashboard_id, lagoon_dashboard_permissions_updating_request)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->update_lagoon_dashboard_permissions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update permissions for a dashboard of SORACOM Lagoon
        api_instance.update_lagoon_dashboard_permissions(dashboard_id, lagoon_dashboard_permissions_updating_request, classic=classic)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->update_lagoon_dashboard_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| dashboard_id |
 **lagoon_dashboard_permissions_updating_request** | [**LagoonDashboardPermissionsUpdatingRequest**](LagoonDashboardPermissionsUpdatingRequest.md)| req |
 **classic** | **bool**| If the value is true, a request will be issued to Lagoon Classic. This is only valid if both Lagoon and Lagoon Classic are enabled. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Updated |  -  |
**400** | Bad request |  -  |
**403** | Unauthorized operation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lagoon_license_pack**
> update_lagoon_license_pack(lagoon_license_packs_updating_request)

Update the quantities for license packs of SORACOM Lagoon

Update the quantities for license packs of SORACOM Lagoon. This API is only allowed to operate by root account.

### Example


```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_license_packs_updating_request import LagoonLicensePacksUpdatingRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lagoon_api.LagoonApi(api_client)
    lagoon_license_packs_updating_request = LagoonLicensePacksUpdatingRequest(
        license_pack_quantities=[
            LagoonLicensePacksUpdatingRequestLicensePackQuantities(
                desired_quantity=1,
                license_pack_name="license_pack_name_example",
            ),
        ],
    ) # LagoonLicensePacksUpdatingRequest | req

    # example passing only required values which don't have defaults set
    try:
        # Update the quantities for license packs of SORACOM Lagoon
        api_instance.update_lagoon_license_pack(lagoon_license_packs_updating_request)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->update_lagoon_license_pack: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lagoon_license_packs_updating_request** | [**LagoonLicensePacksUpdatingRequest**](LagoonLicensePacksUpdatingRequest.md)| req |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Updated |  -  |
**400** | Bad request |  -  |
**404** | Operator Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lagoon_plan**
> update_lagoon_plan(lagoon_plan_changing_request)

Update the plan of SORACOM Lagoon

Update the plan of SORACOM Lagoon. This API is only allowed to operate by root account.

### Example


```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_plan_changing_request import LagoonPlanChangingRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = lagoon_api.LagoonApi(api_client)
    lagoon_plan_changing_request = LagoonPlanChangingRequest(
        plan="maker",
    ) # LagoonPlanChangingRequest | req

    # example passing only required values which don't have defaults set
    try:
        # Update the plan of SORACOM Lagoon
        api_instance.update_lagoon_plan(lagoon_plan_changing_request)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->update_lagoon_plan: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lagoon_plan_changing_request** | [**LagoonPlanChangingRequest**](LagoonPlanChangingRequest.md)| req |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Updated |  -  |
**400** | Bad request |  -  |
**404** | Operator Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lagoon_user_email**
> update_lagoon_user_email(lagoon_user_id, lagoon_user_email_updating_request)

Update email address of a SORACOM Lagoon user

Update email address of a SORACOM Lagoon user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_user_email_updating_request import LagoonUserEmailUpdatingRequest
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
    api_instance = lagoon_api.LagoonApi(api_client)
    lagoon_user_id = 1 # int | Target ID of the lagoon user
    lagoon_user_email_updating_request = LagoonUserEmailUpdatingRequest(
        user_email="user_email_example",
    ) # LagoonUserEmailUpdatingRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Update email address of a SORACOM Lagoon user
        api_instance.update_lagoon_user_email(lagoon_user_id, lagoon_user_email_updating_request)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->update_lagoon_user_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lagoon_user_id** | **int**| Target ID of the lagoon user |
 **lagoon_user_email_updating_request** | [**LagoonUserEmailUpdatingRequest**](LagoonUserEmailUpdatingRequest.md)| request |

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
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lagoon_user_password**
> update_lagoon_user_password(lagoon_user_id, lagoon_user_password_updating_request)

Update password of a SORACOM Lagoon user

Update password of a SORACOM Lagoon user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_user_password_updating_request import LagoonUserPasswordUpdatingRequest
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
    api_instance = lagoon_api.LagoonApi(api_client)
    lagoon_user_id = 1 # int | Target ID of the lagoon user
    lagoon_user_password_updating_request = LagoonUserPasswordUpdatingRequest(
        new_password="new_password_example",
        old_password="old_password_example",
    ) # LagoonUserPasswordUpdatingRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Update password of a SORACOM Lagoon user
        api_instance.update_lagoon_user_password(lagoon_user_id, lagoon_user_password_updating_request)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->update_lagoon_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lagoon_user_id** | **int**| Target ID of the lagoon user |
 **lagoon_user_password_updating_request** | [**LagoonUserPasswordUpdatingRequest**](LagoonUserPasswordUpdatingRequest.md)| request |

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
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lagoon_user_permission**
> update_lagoon_user_permission(lagoon_user_id, lagoon_user_permission_updating_request)

Update permission of a SORACOM Lagoon user

Update permission of a SORACOM Lagoon user.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import lagoon_api
from api.model.lagoon_user_permission_updating_request import LagoonUserPermissionUpdatingRequest
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
    api_instance = lagoon_api.LagoonApi(api_client)
    lagoon_user_id = 1 # int | Target ID of the lagoon user
    lagoon_user_permission_updating_request = LagoonUserPermissionUpdatingRequest(
        role="Viewer",
    ) # LagoonUserPermissionUpdatingRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Update permission of a SORACOM Lagoon user
        api_instance.update_lagoon_user_permission(lagoon_user_id, lagoon_user_permission_updating_request)
    except api.ApiException as e:
        print("Exception when calling LagoonApi->update_lagoon_user_permission: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lagoon_user_id** | **int**| Target ID of the lagoon user |
 **lagoon_user_permission_updating_request** | [**LagoonUserPermissionUpdatingRequest**](LagoonUserPermissionUpdatingRequest.md)| request |

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
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

