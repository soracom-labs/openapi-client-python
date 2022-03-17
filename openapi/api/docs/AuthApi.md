# api.AuthApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth**](AuthApi.md#auth) | **POST** /auth | Performs authentication to access to the SORACOM API.
[**issue_password_reset_token**](AuthApi.md#issue_password_reset_token) | **POST** /auth/password_reset_token/issue | Issues a password reset token for the operator.
[**verify_password_reset_token**](AuthApi.md#verify_password_reset_token) | **POST** /auth/password_reset_token/verify | Verifies the password reset token and updates password.


# **auth**
> AuthResponse auth(auth_request)

Performs authentication to access to the SORACOM API.

Performs authentication to access to the SORACOM API. To perform authentication by a root account, specify `email` and `password`. To perform authentication by an AuthKey, specify `authKeyId` and `authKey`. To perform authentication by a SAM user, specify `operatorId`, `userName` and `password`. An API Key and an API Token will be included in the response if successful. Specify the API Key and the API Token to requests afterwards

### Example


```python
import time
import api
from api.api import auth_api
from api.model.auth_request import AuthRequest
from api.model.auth_response import AuthResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    auth_request = AuthRequest(
        auth_key="auth_key_example",
        auth_key_id="auth_key_id_example",
        email="email_example",
        mfa_otp_code="mfa_otp_code_example",
        operator_id="operator_id_example",
        password="password_example",
        token_timeout_seconds=86400,
        user_name="user_name_example",
    ) # AuthRequest | Authentication request.

    # example passing only required values which don't have defaults set
    try:
        # Performs authentication to access to the SORACOM API.
        api_response = api_instance.auth(auth_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling AuthApi->auth: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_request** | [**AuthRequest**](AuthRequest.md)| Authentication request. |

### Return type

[**AuthResponse**](AuthResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication successful. |  -  |
**401** | Authentication failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_password_reset_token**
> issue_password_reset_token(issue_password_reset_token_request)

Issues a password reset token for the operator.

Generates a password reset token and send it to the operator's mail address. After receiving the password reset token, call /v1/auth/password_reset_token/verify API with the token to update operator's password.

### Example


```python
import time
import api
from api.api import auth_api
from api.model.issue_password_reset_token_request import IssuePasswordResetTokenRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    issue_password_reset_token_request = IssuePasswordResetTokenRequest(
        email="email_example",
    ) # IssuePasswordResetTokenRequest | email address

    # example passing only required values which don't have defaults set
    try:
        # Issues a password reset token for the operator.
        api_instance.issue_password_reset_token(issue_password_reset_token_request)
    except api.ApiException as e:
        print("Exception when calling AuthApi->issue_password_reset_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_password_reset_token_request** | [**IssuePasswordResetTokenRequest**](IssuePasswordResetTokenRequest.md)| email address |

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
**200** | OK. |  -  |
**400** | Invalid email address. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_password_reset_token**
> verify_password_reset_token(verify_password_reset_token_request)

Verifies the password reset token and updates password.

Updates the operator's password if the password reset token is verified.

### Example


```python
import time
import api
from api.api import auth_api
from api.model.verify_password_reset_token_request import VerifyPasswordResetTokenRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    verify_password_reset_token_request = VerifyPasswordResetTokenRequest(
        password="password_example",
        token="token_example",
    ) # VerifyPasswordResetTokenRequest | token, password

    # example passing only required values which don't have defaults set
    try:
        # Verifies the password reset token and updates password.
        api_instance.verify_password_reset_token(verify_password_reset_token_request)
    except api.ApiException as e:
        print("Exception when calling AuthApi->verify_password_reset_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_password_reset_token_request** | [**VerifyPasswordResetTokenRequest**](VerifyPasswordResetTokenRequest.md)| token, password |

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
**200** | OK. |  -  |
**400** | Invalid token. |  -  |
**404** | Token expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

