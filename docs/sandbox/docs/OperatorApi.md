# soracom_sandbox.OperatorApi

All URIs are relative to *https://api-sandbox.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sandbox_delete_operator**](OperatorApi.md#sandbox_delete_operator) | **DELETE** /sandbox/operators/{operator_id} | Deletes an operator
[**sandbox_get_signup_token**](OperatorApi.md#sandbox_get_signup_token) | **POST** /sandbox/operators/token/{email} | Gets a signup token
[**sandbox_initialize_operator**](OperatorApi.md#sandbox_initialize_operator) | **POST** /sandbox/init | Creates an operator account.


# **sandbox_delete_operator**
> sandbox_delete_operator(operator_id)

Deletes an operator

Deletes the specified operator.

### Example


```python
import time
import soracom_sandbox
from soracom_sandbox.api import operator_api
from pprint import pprint
# Defining the host is optional and defaults to https://api-sandbox.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_sandbox.Configuration(
    host = "https://api-sandbox.soracom.io/v1"
)


# Enter a context with an instance of the API client
with soracom_sandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # Deletes an operator
        api_instance.sandbox_delete_operator(operator_id)
    except soracom_sandbox.ApiException as e:
        print("Exception when calling OperatorApi->sandbox_delete_operator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

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
**200** | OK |  -  |
**400** | Operator does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_get_signup_token**
> SandboxGetSignupTokenResponse sandbox_get_signup_token(email, sandbox_get_signup_token_request)

Gets a signup token

Retrieves a 'signup token' for registration confirmation. Please specify a pair of AuthKeyId and AuthKey of a SAM user on the production environment to check if the caller has a valid account on it.

### Example


```python
import time
import soracom_sandbox
from soracom_sandbox.api import operator_api
from soracom_sandbox.model.sandbox_get_signup_token_request import SandboxGetSignupTokenRequest
from soracom_sandbox.model.sandbox_get_signup_token_response import SandboxGetSignupTokenResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-sandbox.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_sandbox.Configuration(
    host = "https://api-sandbox.soracom.io/v1"
)


# Enter a context with an instance of the API client
with soracom_sandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_api.OperatorApi(api_client)
    email = "email_example" # str | email
    sandbox_get_signup_token_request = SandboxGetSignupTokenRequest(
        auth_key="auth_key_example",
        auth_key_id="auth_key_id_example",
    ) # SandboxGetSignupTokenRequest | Authentication request

    # example passing only required values which don't have defaults set
    try:
        # Gets a signup token
        api_response = api_instance.sandbox_get_signup_token(email, sandbox_get_signup_token_request)
        pprint(api_response)
    except soracom_sandbox.ApiException as e:
        print("Exception when calling OperatorApi->sandbox_get_signup_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| email |
 **sandbox_get_signup_token_request** | [**SandboxGetSignupTokenRequest**](SandboxGetSignupTokenRequest.md)| Authentication request |

### Return type

[**SandboxGetSignupTokenResponse**](SandboxGetSignupTokenResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved signup token. |  -  |
**400** | Email address, AuthKeyId, or AuthKey is not correct. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_initialize_operator**
> SandboxAuthResponse sandbox_initialize_operator(sandbox_init_request)

Creates an operator account.

Performs complex signup process at once, including registering dummy payment method. Specify `email` and `password` for an operator which will be created on sandbox, `authKeyId` and `authKey` for a real operator on the production environment. An API Key and an API Token will be included in the response if successful. Use the API Key and the API Token to requests afterwards.

### Example


```python
import time
import soracom_sandbox
from soracom_sandbox.api import operator_api
from soracom_sandbox.model.sandbox_init_request import SandboxInitRequest
from soracom_sandbox.model.sandbox_auth_response import SandboxAuthResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-sandbox.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_sandbox.Configuration(
    host = "https://api-sandbox.soracom.io/v1"
)


# Enter a context with an instance of the API client
with soracom_sandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_api.OperatorApi(api_client)
    sandbox_init_request = SandboxInitRequest(
        auth_key="auth_key_example",
        auth_key_id="auth_key_id_example",
        coverage_types=[
            "coverage_types_example",
        ],
        email="email_example",
        password="password_example",
        register_payment_method=True,
    ) # SandboxInitRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Creates an operator account.
        api_response = api_instance.sandbox_initialize_operator(sandbox_init_request)
        pprint(api_response)
    except soracom_sandbox.ApiException as e:
        print("Exception when calling OperatorApi->sandbox_initialize_operator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_init_request** | [**SandboxInitRequest**](SandboxInitRequest.md)| request |

### Return type

[**SandboxAuthResponse**](SandboxAuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a sandbox operator. |  -  |
**400** | Email address, AuthKeyId, or AuthKey is not correct. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

