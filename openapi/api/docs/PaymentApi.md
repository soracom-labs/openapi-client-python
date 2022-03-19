# soracom_api.PaymentApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_payment_method**](PaymentApi.md#activate_payment_method) | **POST** /payment_methods/current/activate | Activate payment method.
[**export_payment_statement**](PaymentApi.md#export_payment_statement) | **POST** /payment_statements/{payment_statement_id}/export | Export payment statement.
[**get_payer_information**](PaymentApi.md#get_payer_information) | **GET** /payment_statements/payer_information | Export payer information.
[**get_payment_method**](PaymentApi.md#get_payment_method) | **GET** /payment_methods/current | Get payment method information.
[**get_payment_transaction**](PaymentApi.md#get_payment_transaction) | **GET** /payment_history/transactions/{payment_transaction_id} | Get payment transaction result.
[**get_volume_discount**](PaymentApi.md#get_volume_discount) | **GET** /volume_discounts/{contract_id} | Get long term discount.
[**list_coupons**](PaymentApi.md#list_coupons) | **GET** /coupons | List coupons.
[**list_payment_statements**](PaymentApi.md#list_payment_statements) | **GET** /payment_statements | List payment statements.
[**list_volume_discounts**](PaymentApi.md#list_volume_discounts) | **GET** /volume_discounts | List long term discounts.
[**register_coupon**](PaymentApi.md#register_coupon) | **POST** /coupons/{coupon_code}/register | Register Coupon.
[**register_payer_information**](PaymentApi.md#register_payer_information) | **POST** /payment_statements/payer_information | Register payer information.


# **activate_payment_method**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} activate_payment_method()

Activate payment method.

Activates a current payment method that has an error.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import payment_api
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
    api_instance = payment_api.PaymentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Activate payment method.
        api_response = api_instance.activate_payment_method()
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->activate_payment_method: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**404** | Payment method not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_payment_statement**
> FileExportResponse export_payment_statement(payment_statement_id)

Export payment statement.

Export payment statement.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import payment_api
from soracom_api.model.file_export_response import FileExportResponse
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
    api_instance = payment_api.PaymentApi(api_client)
    payment_statement_id = "payment_statement_id_example" # str | Payment statement ID
    export_mode = "async" # str | Export mode (async, sync) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export payment statement.
        api_response = api_instance.export_payment_statement(payment_statement_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->export_payment_statement: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export payment statement.
        api_response = api_instance.export_payment_statement(payment_statement_id, export_mode=export_mode)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->export_payment_statement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_statement_id** | **str**| Payment statement ID |
 **export_mode** | **str**| Export mode (async, sync) | [optional]

### Return type

[**FileExportResponse**](FileExportResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Invalid payment statement ID. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payer_information**
> RegisterPayerInformationModel get_payer_information()

Export payer information.

Export payer information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import payment_api
from soracom_api.model.register_payer_information_model import RegisterPayerInformationModel
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
    api_instance = payment_api.PaymentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Export payer information.
        api_response = api_instance.get_payer_information()
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->get_payer_information: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RegisterPayerInformationModel**](RegisterPayerInformationModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Payer information not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_method**
> GetPaymentMethodResult get_payment_method()

Get payment method information.

Returns current payment methods. Detailed information is included in the properties.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import payment_api
from soracom_api.model.get_payment_method_result import GetPaymentMethodResult
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
    api_instance = payment_api.PaymentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get payment method information.
        api_response = api_instance.get_payment_method()
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->get_payment_method: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPaymentMethodResult**](GetPaymentMethodResult.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**404** | Payment method not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_transaction**
> GetPaymentTransactionResult get_payment_transaction(payment_transaction_id)

Get payment transaction result.

Returns result of a payment transaction.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import payment_api
from soracom_api.model.get_payment_transaction_result import GetPaymentTransactionResult
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
    api_instance = payment_api.PaymentApi(api_client)
    payment_transaction_id = "payment_transaction_id_example" # str | Payment transaction ID

    # example passing only required values which don't have defaults set
    try:
        # Get payment transaction result.
        api_response = api_instance.get_payment_transaction(payment_transaction_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->get_payment_transaction: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_transaction_id** | **str**| Payment transaction ID |

### Return type

[**GetPaymentTransactionResult**](GetPaymentTransactionResult.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Invalid payment transaction ID. |  -  |
**404** | Payment transaction result not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_volume_discount**
> GetVolumeDiscountResponse get_volume_discount(contract_id)

Get long term discount.

Returns contracted long term discount.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import payment_api
from soracom_api.model.get_volume_discount_response import GetVolumeDiscountResponse
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
    api_instance = payment_api.PaymentApi(api_client)
    contract_id = "contract_id_example" # str | contract_id

    # example passing only required values which don't have defaults set
    try:
        # Get long term discount.
        api_response = api_instance.get_volume_discount(contract_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->get_volume_discount: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contract_id** | **str**| contract_id |

### Return type

[**GetVolumeDiscountResponse**](GetVolumeDiscountResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | Long term discount not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_coupons**
> ListCouponResponse list_coupons()

List coupons.

Returns a list of currently registered coupons.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import payment_api
from soracom_api.model.list_coupon_response import ListCouponResponse
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
    api_instance = payment_api.PaymentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List coupons.
        api_response = api_instance.list_coupons()
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->list_coupons: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCouponResponse**](ListCouponResponse.md)

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

# **list_payment_statements**
> ListPaymentStatementResponse list_payment_statements()

List payment statements.

List payment statements.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import payment_api
from soracom_api.model.list_payment_statement_response import ListPaymentStatementResponse
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
    api_instance = payment_api.PaymentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List payment statements.
        api_response = api_instance.list_payment_statements()
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->list_payment_statements: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListPaymentStatementResponse**](ListPaymentStatementResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_volume_discounts**
> ListVolumeDiscountResponse list_volume_discounts()

List long term discounts.

Returns a list of contracted long term discounts.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import payment_api
from soracom_api.model.list_volume_discount_response import ListVolumeDiscountResponse
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
    api_instance = payment_api.PaymentApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List long term discounts.
        api_response = api_instance.list_volume_discounts()
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->list_volume_discounts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListVolumeDiscountResponse**](ListVolumeDiscountResponse.md)

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

# **register_coupon**
> CouponResponse register_coupon(coupon_code)

Register Coupon.

Registers a coupon.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import payment_api
from soracom_api.model.coupon_response import CouponResponse
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
    api_instance = payment_api.PaymentApi(api_client)
    coupon_code = "coupon_code_example" # str | Coupon code

    # example passing only required values which don't have defaults set
    try:
        # Register Coupon.
        api_response = api_instance.register_coupon(coupon_code)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->register_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **coupon_code** | **str**| Coupon code |

### Return type

[**CouponResponse**](CouponResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK. |  -  |
**400** | The coupon code is invalid or the coupon code registration limit has been reached. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_payer_information**
> register_payer_information(register_payer_information_model)

Register payer information.

Register payer information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import payment_api
from soracom_api.model.register_payer_information_model import RegisterPayerInformationModel
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
    api_instance = payment_api.PaymentApi(api_client)
    register_payer_information_model = RegisterPayerInformationModel(
        company_name="company_name_example",
        department="department_example",
        full_name="full_name_example",
    ) # RegisterPayerInformationModel | Payer information to be registered in the accounting specification

    # example passing only required values which don't have defaults set
    try:
        # Register payer information.
        api_instance.register_payer_information(register_payer_information_model)
    except soracom_api.ApiException as e:
        print("Exception when calling PaymentApi->register_payer_information: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_payer_information_model** | [**RegisterPayerInformationModel**](RegisterPayerInformationModel.md)| Payer information to be registered in the accounting specification |

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
**400** | Invalid payer information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

