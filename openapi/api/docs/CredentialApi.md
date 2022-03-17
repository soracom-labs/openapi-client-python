# api.CredentialApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credential**](CredentialApi.md#create_credential) | **POST** /credentials/{credentials_id} | Create a credential.
[**delete_credential**](CredentialApi.md#delete_credential) | **DELETE** /credentials/{credentials_id} | Delete a credential.
[**list_credentials**](CredentialApi.md#list_credentials) | **GET** /credentials | List of credentials.
[**update_credential**](CredentialApi.md#update_credential) | **PUT** /credentials/{credentials_id} | Update a credential.


# **create_credential**
> CredentialsModel create_credential(credentials_id, create_and_update_credentials_model)

Create a credential.

Creates a new credential.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import credential_api
from api.model.credentials_model import CredentialsModel
from api.model.create_and_update_credentials_model import CreateAndUpdateCredentialsModel
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
    api_instance = credential_api.CredentialApi(api_client)
    credentials_id = "credentials_id_example" # str | credentials_id
    create_and_update_credentials_model = CreateAndUpdateCredentialsModel(
        credentials={},
        description="description_example",
        type="aws-credentials",
    ) # CreateAndUpdateCredentialsModel | credentials

    # example passing only required values which don't have defaults set
    try:
        # Create a credential.
        api_response = api_instance.create_credential(credentials_id, create_and_update_credentials_model)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling CredentialApi->create_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| credentials_id |
 **create_and_update_credentials_model** | [**CreateAndUpdateCredentialsModel**](CreateAndUpdateCredentialsModel.md)| credentials |

### Return type

[**CredentialsModel**](CredentialsModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_credential**
> delete_credential(credentials_id)

Delete a credential.

Deletes a credential.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import credential_api
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
    api_instance = credential_api.CredentialApi(api_client)
    credentials_id = "credentials_id_example" # str | Credentials ID

    # example passing only required values which don't have defaults set
    try:
        # Delete a credential.
        api_instance.delete_credential(credentials_id)
    except api.ApiException as e:
        print("Exception when calling CredentialApi->delete_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| Credentials ID |

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_credentials**
> [CredentialsModel] list_credentials()

List of credentials.

Returns a list of credentials.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import credential_api
from api.model.credentials_model import CredentialsModel
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
    api_instance = credential_api.CredentialApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List of credentials.
        api_response = api_instance.list_credentials()
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling CredentialApi->list_credentials: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[CredentialsModel]**](CredentialsModel.md)

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

# **update_credential**
> CredentialsModel update_credential(credentials_id, create_and_update_credentials_model)

Update a credential.

Updates a credential.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import credential_api
from api.model.credentials_model import CredentialsModel
from api.model.create_and_update_credentials_model import CreateAndUpdateCredentialsModel
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
    api_instance = credential_api.CredentialApi(api_client)
    credentials_id = "credentials_id_example" # str | credentials_id
    create_and_update_credentials_model = CreateAndUpdateCredentialsModel(
        credentials={},
        description="description_example",
        type="aws-credentials",
    ) # CreateAndUpdateCredentialsModel | credentials

    # example passing only required values which don't have defaults set
    try:
        # Update a credential.
        api_response = api_instance.update_credential(credentials_id, create_and_update_credentials_model)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling CredentialApi->update_credential: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials_id** | **str**| credentials_id |
 **create_and_update_credentials_model** | [**CreateAndUpdateCredentialsModel**](CreateAndUpdateCredentialsModel.md)| credentials |

### Return type

[**CredentialsModel**](CredentialsModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json;charset=UTF-8
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | There was an error in the request or the specified token has already expired. (In the latter case, you will need to use the /auth API to do authentication once again.) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

