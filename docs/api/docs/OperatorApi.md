# soracom_api.OperatorApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_coverage_type**](OperatorApi.md#add_coverage_type) | **POST** /operators/{operator_id}/coverage_type/{coverage_type} | Add coverage type.
[**add_operator_contract**](OperatorApi.md#add_operator_contract) | **POST** /operators/{operator_id}/contracts | Add Operator Contract.
[**create_company_information**](OperatorApi.md#create_company_information) | **POST** /operators/{operator_id}/company_information | Create company information.
[**create_individual_information**](OperatorApi.md#create_individual_information) | **POST** /operators/{operator_id}/individual_information | Create individual information.
[**create_operator**](OperatorApi.md#create_operator) | **POST** /operators | Create Operator.
[**delete_operator_auth_key**](OperatorApi.md#delete_operator_auth_key) | **DELETE** /operators/{operator_id}/auth_keys/{auth_key_id} | Delete Operator AuthKey.
[**delete_operator_contract**](OperatorApi.md#delete_operator_contract) | **DELETE** /operators/{operator_id}/contracts/{contract_name} | Delete Operator Contract.
[**enable_mfa**](OperatorApi.md#enable_mfa) | **POST** /operators/{operator_id}/mfa | Enable Operator&#39;s MFA.
[**generate_auth_token**](OperatorApi.md#generate_auth_token) | **POST** /operators/{operator_id}/token | Generate Authentication Token.
[**generate_operator_auth_key**](OperatorApi.md#generate_operator_auth_key) | **POST** /operators/{operator_id}/auth_keys | Generate Operator AuthKey.
[**generate_support_token**](OperatorApi.md#generate_support_token) | **POST** /operators/{operator_id}/support/token | Generate Token for Support Console.
[**get_company_information**](OperatorApi.md#get_company_information) | **GET** /operators/{operator_id}/company_information | Get company information.
[**get_individual_information**](OperatorApi.md#get_individual_information) | **GET** /operators/{operator_id}/individual_information | Get individual information.
[**get_mfa_status**](OperatorApi.md#get_mfa_status) | **GET** /operators/{operator_id}/mfa | Get Operator&#39;s MFA Status.
[**get_operator**](OperatorApi.md#get_operator) | **GET** /operators/{operator_id} | Get Operator.
[**issue_mfa_revoking_token**](OperatorApi.md#issue_mfa_revoking_token) | **POST** /operators/mfa_revoke_token/issue | Issue Operator&#39;s MFA Revoke Token.
[**list_operator_auth_keys**](OperatorApi.md#list_operator_auth_keys) | **GET** /operators/{operator_id}/auth_keys | List Operator AuthKeys.
[**revoke_mfa**](OperatorApi.md#revoke_mfa) | **DELETE** /operators/{operator_id}/mfa | Revoke Operator&#39;s MFA.
[**update_company_information**](OperatorApi.md#update_company_information) | **PUT** /operators/{operator_id}/company_information | Update company information.
[**update_individual_information**](OperatorApi.md#update_individual_information) | **PUT** /operators/{operator_id}/individual_information | Update individual information.
[**update_operator_password**](OperatorApi.md#update_operator_password) | **POST** /operators/{operator_id}/password | Update Operator Password.
[**verify_mfa**](OperatorApi.md#verify_mfa) | **POST** /operators/{operator_id}/mfa/verify | Verify Operator&#39;s MFA OTP Code.
[**verify_mfa_revoking_token**](OperatorApi.md#verify_mfa_revoking_token) | **POST** /operators/mfa_revoke_token/verify | Verify Operator&#39;s MFA revoke token.
[**verify_operator**](OperatorApi.md#verify_operator) | **POST** /operators/verify | Verify Operator.


# **add_coverage_type**
> add_coverage_type(operator_id, coverage_type)

Add coverage type.

Adds the operator's coverage type.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    coverage_type = "coverage_type_example" # str | coverage_type

    # example passing only required values which don't have defaults set
    try:
        # Add coverage type.
        api_instance.add_coverage_type(operator_id, coverage_type)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->add_coverage_type: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **coverage_type** | **str**| coverage_type |

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
**201** | Created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_operator_contract**
> ContractUpdatedResponse add_operator_contract(operator_id, contract_updating_request)

Add Operator Contract.

Adds the operator's contract.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.contract_updating_request import ContractUpdatingRequest
from soracom_api.model.contract_updated_response import ContractUpdatedResponse
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    contract_updating_request = ContractUpdatingRequest(
        contract_detail={},
        contract_name="contract_name_example",
    ) # ContractUpdatingRequest | model

    # example passing only required values which don't have defaults set
    try:
        # Add Operator Contract.
        api_response = api_instance.add_operator_contract(operator_id, contract_updating_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->add_operator_contract: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **contract_updating_request** | [**ContractUpdatingRequest**](ContractUpdatingRequest.md)| model |

### Return type

[**ContractUpdatedResponse**](ContractUpdatedResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_company_information**
> create_company_information(operator_id, company_information_model)

Create company information.

Creates the operator's company information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.company_information_model import CompanyInformationModel
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    company_information_model = CompanyInformationModel(
        address_line1="address_line1_example",
        address_line2="address_line2_example",
        building="building_example",
        city="city_example",
        company_name="company_name_example",
        contact_person_name="contact_person_name_example",
        country_code="country_code_example",
        department="department_example",
        phone_number="phone_number_example",
        state="state_example",
        vat_identification_number="vat_identification_number_example",
        zip_code="zip_code_example",
    ) # CompanyInformationModel | model

    # example passing only required values which don't have defaults set
    try:
        # Create company information.
        api_instance.create_company_information(operator_id, company_information_model)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->create_company_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **company_information_model** | [**CompanyInformationModel**](CompanyInformationModel.md)| model |

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
**201** | Created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_individual_information**
> create_individual_information(operator_id, individual_information_model)

Create individual information.

Creates the operator's individual information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.individual_information_model import IndividualInformationModel
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    individual_information_model = IndividualInformationModel(
        address_line1="address_line1_example",
        address_line2="address_line2_example",
        building="building_example",
        city="city_example",
        country_code="country_code_example",
        full_name="full_name_example",
        phone_number="phone_number_example",
        state="state_example",
        zip_code="zip_code_example",
    ) # IndividualInformationModel | model

    # example passing only required values which don't have defaults set
    try:
        # Create individual information.
        api_instance.create_individual_information(operator_id, individual_information_model)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->create_individual_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **individual_information_model** | [**IndividualInformationModel**](IndividualInformationModel.md)| model |

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
**201** | Created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_operator**
> create_operator(register_operators_request)

Create Operator.

Makes a request to create a new operator. An e-mail is sent to the e-mail address specified in the parameters, containing a one-time token for verifying the operator’s registration.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.register_operators_request import RegisterOperatorsRequest
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
    api_instance = operator_api.OperatorApi(api_client)
    register_operators_request = RegisterOperatorsRequest(
        email="email_example",
        password="password_example",
    ) # RegisterOperatorsRequest | email, password

    # example passing only required values which don't have defaults set
    try:
        # Create Operator.
        api_instance.create_operator(register_operators_request)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->create_operator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_operators_request** | [**RegisterOperatorsRequest**](RegisterOperatorsRequest.md)| email, password |

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
**201** | Operator created. |  -  |
**400** | The e-mail address is already registered or the password has an incorrect format. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_operator_auth_key**
> delete_operator_auth_key(operator_id, auth_key_id)

Delete Operator AuthKey.

Deletes an AuthKey from the operator.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    auth_key_id = "auth_key_id_example" # str | auth_key_id

    # example passing only required values which don't have defaults set
    try:
        # Delete Operator AuthKey.
        api_instance.delete_operator_auth_key(operator_id, auth_key_id)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->delete_operator_auth_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **auth_key_id** | **str**| auth_key_id |

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
**204** | AuthKey was deleted. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_operator_contract**
> delete_operator_contract(operator_id, contract_name)

Delete Operator Contract.

Deletes the operator's contract.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    contract_name = "contract_name_example" # str | contract_name

    # example passing only required values which don't have defaults set
    try:
        # Delete Operator Contract.
        api_instance.delete_operator_contract(operator_id, contract_name)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->delete_operator_contract: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **contract_name** | **str**| contract_name |

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
**204** | No Content. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_mfa**
> EnableMFAOTPResponse enable_mfa(operator_id)

Enable Operator's MFA.

Enables operator's MFA. After calling this APIg, it should be verified by calling `Operator:verifyMFA` API.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.enable_mfaotp_response import EnableMFAOTPResponse
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # Enable Operator's MFA.
        api_response = api_instance.enable_mfa(operator_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->enable_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

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

# **generate_auth_token**
> GenerateTokenResponse generate_auth_token(operator_id, generate_token_request)

Generate Authentication Token.

Generates a new API token. If you insert the current API token into the header and make a request, a response is returned containing the new API token. You can then use the new API token in future requests.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.generate_token_response import GenerateTokenResponse
from soracom_api.model.generate_token_request import GenerateTokenRequest
from soracom_api.model.api_call_error import APICallError
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    generate_token_request = GenerateTokenRequest(
        token_timeout_seconds=86400,
    ) # GenerateTokenRequest | token timeout seconds

    # example passing only required values which don't have defaults set
    try:
        # Generate Authentication Token.
        api_response = api_instance.generate_auth_token(operator_id, generate_token_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->generate_auth_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **generate_token_request** | [**GenerateTokenRequest**](GenerateTokenRequest.md)| token timeout seconds |

### Return type

[**GenerateTokenResponse**](GenerateTokenResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | There was an error in the request or the specified token has already expired. (In the latter case, you will need to use the /auth API to do authentication once again.) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_operator_auth_key**
> GenerateOperatorsAuthKeyResponse generate_operator_auth_key(operator_id)

Generate Operator AuthKey.

Generates an AuthKey for the operator.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.generate_operators_auth_key_response import GenerateOperatorsAuthKeyResponse
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # Generate Operator AuthKey.
        api_response = api_instance.generate_operator_auth_key(operator_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->generate_operator_auth_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

### Return type

[**GenerateOperatorsAuthKeyResponse**](GenerateOperatorsAuthKeyResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | AuthKey was generated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_support_token**
> SupportTokenResponse generate_support_token(operator_id)

Generate Token for Support Console.

Returns a token for accessing the support console.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.support_token_response import SupportTokenResponse
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # Generate Token for Support Console.
        api_response = api_instance.generate_support_token(operator_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->generate_support_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

### Return type

[**SupportTokenResponse**](SupportTokenResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Invalid Operator Id |  -  |
**403** | Invalid token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_information**
> CompanyInformationModel get_company_information(operator_id)

Get company information.

Gets the operator's company information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.company_information_model import CompanyInformationModel
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # Get company information.
        api_response = api_instance.get_company_information(operator_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->get_company_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

### Return type

[**CompanyInformationModel**](CompanyInformationModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_individual_information**
> IndividualInformationModel get_individual_information(operator_id)

Get individual information.

Gets the operator's individual information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.individual_information_model import IndividualInformationModel
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # Get individual information.
        api_response = api_instance.get_individual_information(operator_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->get_individual_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

### Return type

[**IndividualInformationModel**](IndividualInformationModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mfa_status**
> MFAStatusOfUseResponse get_mfa_status(operator_id)

Get Operator's MFA Status.

Gets operator's MFA status. The MFA status is one of `ACTIVE`, `INACTIVE` or `UNCONFIRMED`.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.mfa_status_of_use_response import MFAStatusOfUseResponse
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # Get Operator's MFA Status.
        api_response = api_instance.get_mfa_status(operator_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->get_mfa_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

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

# **get_operator**
> GetOperatorResponse get_operator(operator_id)

Get Operator.

Returns information about the operator.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.get_operator_response import GetOperatorResponse
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # Get Operator.
        api_response = api_instance.get_operator(operator_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->get_operator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

### Return type

[**GetOperatorResponse**](GetOperatorResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Invalid Operator Id |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **issue_mfa_revoking_token**
> issue_mfa_revoking_token(mfa_issue_revoking_token_request)

Issue Operator's MFA Revoke Token.

Issues a token to revoke operator's MFA. The issued token will be sent to the operator via email.

### Example


```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.mfa_issue_revoking_token_request import MFAIssueRevokingTokenRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with soracom_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_api.OperatorApi(api_client)
    mfa_issue_revoking_token_request = MFAIssueRevokingTokenRequest(
        email="email_example",
        password="password_example",
    ) # MFAIssueRevokingTokenRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Issue Operator's MFA Revoke Token.
        api_instance.issue_mfa_revoking_token(mfa_issue_revoking_token_request)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->issue_mfa_revoking_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_issue_revoking_token_request** | [**MFAIssueRevokingTokenRequest**](MFAIssueRevokingTokenRequest.md)| request |

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
**400** | Bad request |  -  |
**404** | Operator not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_operator_auth_keys**
> [AuthKeyResponse] list_operator_auth_keys(operator_id)

List Operator AuthKeys.

Returns the operator's AuthKey list.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.auth_key_response import AuthKeyResponse
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # List Operator AuthKeys.
        api_response = api_instance.list_operator_auth_keys(operator_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->list_operator_auth_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

### Return type

[**[AuthKeyResponse]**](AuthKeyResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_mfa**
> revoke_mfa(operator_id)

Revoke Operator's MFA.

Revokes operator's MFA without backup codes.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # Revoke Operator's MFA.
        api_instance.revoke_mfa(operator_id)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->revoke_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

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

# **update_company_information**
> update_company_information(operator_id, company_information_model)

Update company information.

Updates the operator's company information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.company_information_model import CompanyInformationModel
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    company_information_model = CompanyInformationModel(
        address_line1="address_line1_example",
        address_line2="address_line2_example",
        building="building_example",
        city="city_example",
        company_name="company_name_example",
        contact_person_name="contact_person_name_example",
        country_code="country_code_example",
        department="department_example",
        phone_number="phone_number_example",
        state="state_example",
        vat_identification_number="vat_identification_number_example",
        zip_code="zip_code_example",
    ) # CompanyInformationModel | model

    # example passing only required values which don't have defaults set
    try:
        # Update company information.
        api_instance.update_company_information(operator_id, company_information_model)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->update_company_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **company_information_model** | [**CompanyInformationModel**](CompanyInformationModel.md)| model |

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
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_individual_information**
> update_individual_information(operator_id, individual_information_model)

Update individual information.

Updates the operator's individual information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.individual_information_model import IndividualInformationModel
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    individual_information_model = IndividualInformationModel(
        address_line1="address_line1_example",
        address_line2="address_line2_example",
        building="building_example",
        city="city_example",
        country_code="country_code_example",
        full_name="full_name_example",
        phone_number="phone_number_example",
        state="state_example",
        zip_code="zip_code_example",
    ) # IndividualInformationModel | model

    # example passing only required values which don't have defaults set
    try:
        # Update individual information.
        api_instance.update_individual_information(operator_id, individual_information_model)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->update_individual_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **individual_information_model** | [**IndividualInformationModel**](IndividualInformationModel.md)| model |

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
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_operator_password**
> update_operator_password(operator_id, update_password_request)

Update Operator Password.

Updates the operator's password.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.update_password_request import UpdatePasswordRequest
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    update_password_request = UpdatePasswordRequest(
        current_password="current_password_example",
        new_password="new_password_example",
    ) # UpdatePasswordRequest | current password, new password

    # example passing only required values which don't have defaults set
    try:
        # Update Operator Password.
        api_instance.update_operator_password(operator_id, update_password_request)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->update_operator_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **update_password_request** | [**UpdatePasswordRequest**](UpdatePasswordRequest.md)| current password, new password |

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
**200** | OK. |  -  |
**400** | Invalid password. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_mfa**
> OperatorMFAVerifyingResponse verify_mfa(operator_id, mfa_authentication_request)

Verify Operator's MFA OTP Code.

Verifies operator's MFA with OTP code after calling `Operator:enableMFA` API. MFA will not be activated unless the MFA OTP is verified with this API.  Backup codes are going to be returned in the response. These codes must be securely stored.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.mfa_authentication_request import MFAAuthenticationRequest
from soracom_api.model.operator_mfa_verifying_response import OperatorMFAVerifyingResponse
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
    api_instance = operator_api.OperatorApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    mfa_authentication_request = MFAAuthenticationRequest(
        mfa_otp_code="mfa_otp_code_example",
    ) # MFAAuthenticationRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Verify Operator's MFA OTP Code.
        api_response = api_instance.verify_mfa(operator_id, mfa_authentication_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->verify_mfa: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **mfa_authentication_request** | [**MFAAuthenticationRequest**](MFAAuthenticationRequest.md)| request |

### Return type

[**OperatorMFAVerifyingResponse**](OperatorMFAVerifyingResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_mfa_revoking_token**
> verify_mfa_revoking_token(mfa_revoking_token_verify_request)

Verify Operator's MFA revoke token.

Verifies the one-time token which is previously issued by calling `/operators/mfa_revoke_token/issue` API, operator's email address, password, and one of the backup codes. If verified, operator's MFA is going to be revoked.

### Example


```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.mfa_revoking_token_verify_request import MFARevokingTokenVerifyRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with soracom_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_api.OperatorApi(api_client)
    mfa_revoking_token_verify_request = MFARevokingTokenVerifyRequest(
        backup_code="backup_code_example",
        email="email_example",
        password="password_example",
        token="token_example",
    ) # MFARevokingTokenVerifyRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Verify Operator's MFA revoke token.
        api_instance.verify_mfa_revoking_token(mfa_revoking_token_verify_request)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->verify_mfa_revoking_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mfa_revoking_token_verify_request** | [**MFARevokingTokenVerifyRequest**](MFARevokingTokenVerifyRequest.md)| request |

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
**200** | Revoked |  -  |
**400** | Bad request |  -  |
**403** | Invalid username or password |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_operator**
> verify_operator(verify_operators_request)

Verify Operator.

Verifies the operator's registration. Called by setting as parameter the one-time verification token received via e-mail.

### Example


```python
import time
import soracom_api
from soracom_api.api import operator_api
from soracom_api.model.verify_operators_request import VerifyOperatorsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_api.Configuration(
    host = "https://api.soracom.io/v1"
)


# Enter a context with an instance of the API client
with soracom_api.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = operator_api.OperatorApi(api_client)
    verify_operators_request = VerifyOperatorsRequest(
        token="token_example",
    ) # VerifyOperatorsRequest | token

    # example passing only required values which don't have defaults set
    try:
        # Verify Operator.
        api_instance.verify_operator(verify_operators_request)
    except soracom_api.ApiException as e:
        print("Exception when calling OperatorApi->verify_operator: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **verify_operators_request** | [**VerifyOperatorsRequest**](VerifyOperatorsRequest.md)| token |

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
**200** | Registration successful. |  -  |
**400** | The one-time token is incorrect. |  -  |
**404** | The one-time token has expired. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

