# api.ShippingAddressApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipping_address**](ShippingAddressApi.md#create_shipping_address) | **POST** /operators/{operator_id}/shipping_addresses | Create shipping address.
[**delete_shipping_address**](ShippingAddressApi.md#delete_shipping_address) | **DELETE** /operators/{operator_id}/shipping_addresses/{shipping_address_id} | Delete shipping address.
[**get_shipping_address**](ShippingAddressApi.md#get_shipping_address) | **GET** /operators/{operator_id}/shipping_addresses/{shipping_address_id} | Get shipping address.
[**list_shipping_addresses**](ShippingAddressApi.md#list_shipping_addresses) | **GET** /operators/{operator_id}/shipping_addresses | List shipping addresses.
[**update_shipping_address**](ShippingAddressApi.md#update_shipping_address) | **PUT** /operators/{operator_id}/shipping_addresses/{shipping_address_id} | Update shipping address.


# **create_shipping_address**
> GetShippingAddressResponse create_shipping_address(operator_id, shipping_address_model)

Create shipping address.

Creates a new shipping address.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import shipping_address_api
from api.model.get_shipping_address_response import GetShippingAddressResponse
from api.model.shipping_address_model import ShippingAddressModel
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
    api_instance = shipping_address_api.ShippingAddressApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    shipping_address_model = ShippingAddressModel(
        address_line1="address_line1_example",
        address_line2="address_line2_example",
        building="building_example",
        city="city_example",
        company_name="company_name_example",
        country_code="country_code_example",
        department="department_example",
        email="email_example",
        full_name="full_name_example",
        phone_number="phone_number_example",
        state="state_example",
        zip_code="zip_code_example",
    ) # ShippingAddressModel | model

    # example passing only required values which don't have defaults set
    try:
        # Create shipping address.
        api_response = api_instance.create_shipping_address(operator_id, shipping_address_model)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling ShippingAddressApi->create_shipping_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **shipping_address_model** | [**ShippingAddressModel**](ShippingAddressModel.md)| model |

### Return type

[**GetShippingAddressResponse**](GetShippingAddressResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Shipping address was registered. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shipping_address**
> delete_shipping_address(operator_id, shipping_address_id)

Delete shipping address.

Deletes a shipping address.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import shipping_address_api
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
    api_instance = shipping_address_api.ShippingAddressApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    shipping_address_id = "shipping_address_id_example" # str | shipping_address_id

    # example passing only required values which don't have defaults set
    try:
        # Delete shipping address.
        api_instance.delete_shipping_address(operator_id, shipping_address_id)
    except api.ApiException as e:
        print("Exception when calling ShippingAddressApi->delete_shipping_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **shipping_address_id** | **str**| shipping_address_id |

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

# **get_shipping_address**
> GetShippingAddressResponse get_shipping_address(operator_id, shipping_address_id)

Get shipping address.

Returns a shipping address.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import shipping_address_api
from api.model.get_shipping_address_response import GetShippingAddressResponse
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
    api_instance = shipping_address_api.ShippingAddressApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    shipping_address_id = "shipping_address_id_example" # str | shipping_address_id

    # example passing only required values which don't have defaults set
    try:
        # Get shipping address.
        api_response = api_instance.get_shipping_address(operator_id, shipping_address_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling ShippingAddressApi->get_shipping_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **shipping_address_id** | **str**| shipping_address_id |

### Return type

[**GetShippingAddressResponse**](GetShippingAddressResponse.md)

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

# **list_shipping_addresses**
> ListShippingAddressResponse list_shipping_addresses(operator_id)

List shipping addresses.

Returns a list of shipping addresses.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import shipping_address_api
from api.model.list_shipping_address_response import ListShippingAddressResponse
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
    api_instance = shipping_address_api.ShippingAddressApi(api_client)
    operator_id = "operator_id_example" # str | operator_id

    # example passing only required values which don't have defaults set
    try:
        # List shipping addresses.
        api_response = api_instance.list_shipping_addresses(operator_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling ShippingAddressApi->list_shipping_addresses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |

### Return type

[**ListShippingAddressResponse**](ListShippingAddressResponse.md)

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

# **update_shipping_address**
> update_shipping_address(operator_id, shipping_address_id, shipping_address_model)

Update shipping address.

Updates a shipping address.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import shipping_address_api
from api.model.shipping_address_model import ShippingAddressModel
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
    api_instance = shipping_address_api.ShippingAddressApi(api_client)
    operator_id = "operator_id_example" # str | Operator ID
    shipping_address_id = "shipping_address_id_example" # str | shipping_address_id
    shipping_address_model = ShippingAddressModel(
        address_line1="address_line1_example",
        address_line2="address_line2_example",
        building="building_example",
        city="city_example",
        company_name="company_name_example",
        country_code="country_code_example",
        department="department_example",
        email="email_example",
        full_name="full_name_example",
        phone_number="phone_number_example",
        state="state_example",
        zip_code="zip_code_example",
    ) # ShippingAddressModel | model

    # example passing only required values which don't have defaults set
    try:
        # Update shipping address.
        api_instance.update_shipping_address(operator_id, shipping_address_id, shipping_address_model)
    except api.ApiException as e:
        print("Exception when calling ShippingAddressApi->update_shipping_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| Operator ID |
 **shipping_address_id** | **str**| shipping_address_id |
 **shipping_address_model** | [**ShippingAddressModel**](ShippingAddressModel.md)| model |

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

