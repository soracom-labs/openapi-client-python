# api.EmailApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_email**](EmailApi.md#delete_email) | **DELETE** /operators/{operator_id}/emails/{email_id} | Delete email address
[**get_email**](EmailApi.md#get_email) | **GET** /operators/{operator_id}/emails/{email_id} | Get email address
[**issue_add_email_token**](EmailApi.md#issue_add_email_token) | **POST** /operators/add_email_token/issue | Issue a token to add an email address
[**list_emails**](EmailApi.md#list_emails) | **GET** /operators/{operator_id}/emails | List email addresses
[**verify_add_email_token**](EmailApi.md#verify_add_email_token) | **POST** /operators/add_email_token/verify | Verify a token to add an email address


# **delete_email**
> delete_email(operator_id, email_id)

Delete email address

Deletes an email address.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import email_api
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
    api_instance = email_api.EmailApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    email_id = "email_id_example" # str | email_id

    # example passing only required values which don't have defaults set
    try:
        # Delete email address
        api_instance.delete_email(operator_id, email_id)
    except api.ApiException as e:
        print("Exception when calling EmailApi->delete_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **email_id** | **str**| email_id |

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

# **get_email**
> EmailsModel get_email(operator_id, email_id)

Get email address

Returns an email address.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import email_api
from api.model.emails_model import EmailsModel
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
    api_instance = email_api.EmailApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    email_id = "email_id_example" # str | email_id

    # example passing only required values which don't have defaults set
    try:
        # Get email address
        api_response = api_instance.get_email(operator_id, email_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling EmailApi->get_email: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **email_id** | **str**| email_id |

### Return type

[**EmailsModel**](EmailsModel.md)

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

# **issue_add_email_token**
> issue_add_email_token(issue_add_email_token_request)

Issue a token to add an email address

Sends an email with a one-time token for adding an e-mail address.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import email_api
from api.model.issue_add_email_token_request import IssueAddEmailTokenRequest
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
    api_instance = email_api.EmailApi(api_client)
    issue_add_email_token_request = IssueAddEmailTokenRequest(
        email="email_example",
        password="password_example",
    ) # IssueAddEmailTokenRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Issue a token to add an email address
        api_instance.issue_add_email_token(issue_add_email_token_request)
    except api.ApiException as e:
        print("Exception when calling EmailApi->issue_add_email_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_add_email_token_request** | [**IssueAddEmailTokenRequest**](IssueAddEmailTokenRequest.md)| request |

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

# **list_emails**
> [EmailsModel] list_emails(operator_id)

List email addresses

Returns a list of email addresses.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import email_api
from api.model.emails_model import EmailsModel
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
    api_instance = email_api.EmailApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # List email addresses
        api_response = api_instance.list_emails(operator_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling EmailApi->list_emails: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

### Return type

[**[EmailsModel]**](EmailsModel.md)

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

# **verify_add_email_token**
> verify_add_email_token(verify_add_email_token_request)

Verify a token to add an email address

Verifies the token for adding email address.

### Example


```python
import time
import api
from api.api import email_api
from api.model.verify_add_email_token_request import VerifyAddEmailTokenRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = email_api.EmailApi(api_client)
    verify_add_email_token_request = VerifyAddEmailTokenRequest(
        token="token_example",
    ) # VerifyAddEmailTokenRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Verify a token to add an email address
        api_instance.verify_add_email_token(verify_add_email_token_request)
    except api.ApiException as e:
        print("Exception when calling EmailApi->verify_add_email_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_add_email_token_request** | [**VerifyAddEmailTokenRequest**](VerifyAddEmailTokenRequest.md)| request |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

