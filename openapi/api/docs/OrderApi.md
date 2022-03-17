# api.OrderApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order**](OrderApi.md#cancel_order) | **PUT** /orders/{order_id}/cancel | Cancel order.
[**confirm_coupon_order**](OrderApi.md#confirm_coupon_order) | **PUT** /coupons/{order_id}/confirm | Confirm coupon order.
[**confirm_order**](OrderApi.md#confirm_order) | **PUT** /orders/{order_id}/confirm | Confirm order.
[**confirm_volume_discount_order**](OrderApi.md#confirm_volume_discount_order) | **PUT** /volume_discounts/{order_id}/confirm | Confirm long term discount order.
[**create_coupon_quotation**](OrderApi.md#create_coupon_quotation) | **POST** /coupons | Create coupon quotation.
[**create_quotation**](OrderApi.md#create_quotation) | **POST** /orders | Create Quotation.
[**create_volume_discount_quotation**](OrderApi.md#create_volume_discount_quotation) | **POST** /volume_discounts | Create long term discount quotation.
[**get_order**](OrderApi.md#get_order) | **GET** /orders/{order_id} | Get confirmed order.
[**list_available_discounts**](OrderApi.md#list_available_discounts) | **GET** /volume_discounts/available_discounts | List available long term discounts.
[**list_ordered_subscribers**](OrderApi.md#list_ordered_subscribers) | **GET** /orders/{order_id}/subscribers | List ordered subscribers.
[**list_orders**](OrderApi.md#list_orders) | **GET** /orders | List confirmed orders.
[**list_products**](OrderApi.md#list_products) | **GET** /products | List products.
[**register_ordered_sim**](OrderApi.md#register_ordered_sim) | **POST** /orders/{order_id}/subscribers/register | Register subscribers for operator.


# **cancel_order**
> str cancel_order(order_id)

Cancel order.

Cancels an order. If the order has already been dispatched, an error is returned.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "order_id_example" # str | order_id

    # example passing only required values which don't have defaults set
    try:
        # Cancel order.
        api_response = api_instance.cancel_order(order_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->cancel_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| order_id |

### Return type

**str**

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The order was cancelled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_coupon_order**
> CouponResponse confirm_coupon_order(order_id)

Confirm coupon order.

Performs a credit limit and confirms the order if no problems are encountered.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
from api.model.coupon_response import CouponResponse
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "order_id_example" # str | order_id

    # example passing only required values which don't have defaults set
    try:
        # Confirm coupon order.
        api_response = api_instance.confirm_coupon_order(order_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->confirm_coupon_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| order_id |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_order**
> confirm_order(order_id)

Confirm order.

Performs a credit limit and confirms the order if no problems are encountered.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "order_id_example" # str | order_id

    # example passing only required values which don't have defaults set
    try:
        # Confirm order.
        api_instance.confirm_order(order_id)
    except api.ApiException as e:
        print("Exception when calling OrderApi->confirm_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| order_id |

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
**200** | OK. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_volume_discount_order**
> GetVolumeDiscountResponse confirm_volume_discount_order(order_id)

Confirm long term discount order.

Performs a credit limit and confirms the order if no problems are encountered.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
from api.model.get_volume_discount_response import GetVolumeDiscountResponse
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "order_id_example" # str | order_id

    # example passing only required values which don't have defaults set
    try:
        # Confirm long term discount order.
        api_response = api_instance.confirm_volume_discount_order(order_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->confirm_volume_discount_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| order_id |

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_coupon_quotation**
> EstimatedCouponModel create_coupon_quotation(create_estimated_coupon_request)

Create coupon quotation.

Creates a new coupon quotation. If the orderId is put in /confirm, the order is complete.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
from api.model.create_estimated_coupon_request import CreateEstimatedCouponRequest
from api.model.estimated_coupon_model import EstimatedCouponModel
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
    api_instance = order_api.OrderApi(api_client)
    create_estimated_coupon_request = CreateEstimatedCouponRequest(
        amount=3.14,
    ) # CreateEstimatedCouponRequest | Coupon details

    # example passing only required values which don't have defaults set
    try:
        # Create coupon quotation.
        api_response = api_instance.create_coupon_quotation(create_estimated_coupon_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->create_coupon_quotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_estimated_coupon_request** | [**CreateEstimatedCouponRequest**](CreateEstimatedCouponRequest.md)| Coupon details |

### Return type

[**EstimatedCouponModel**](EstimatedCouponModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_quotation**
> EstimatedOrderModel create_quotation(create_estimated_order_request)

Create Quotation.

Creates a new order quotation. If the orderId is put in /confirm, the order is complete.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
from api.model.create_estimated_order_request import CreateEstimatedOrderRequest
from api.model.estimated_order_model import EstimatedOrderModel
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
    api_instance = order_api.OrderApi(api_client)
    create_estimated_order_request = CreateEstimatedOrderRequest(
        order_item_list=[
            OrderItemModel(
                product_code="product_code_example",
                quantity=1,
            ),
        ],
        shipping_address_id="shipping_address_id_example",
    ) # CreateEstimatedOrderRequest | Order item list and shipping address ID

    # example passing only required values which don't have defaults set
    try:
        # Create Quotation.
        api_response = api_instance.create_quotation(create_estimated_order_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->create_quotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_estimated_order_request** | [**CreateEstimatedOrderRequest**](CreateEstimatedOrderRequest.md)| Order item list and shipping address ID |

### Return type

[**EstimatedOrderModel**](EstimatedOrderModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A new order quotation was created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_volume_discount_quotation**
> EstimatedVolumeDiscountModel create_volume_discount_quotation(create_estimated_volume_discount_request)

Create long term discount quotation.

Creates a new long term discount quotation. If the orderId is put in /confirm, the order is complete. (Currently, long term discount is only applied to plan-D, plan-K)

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
from api.model.create_estimated_volume_discount_request import CreateEstimatedVolumeDiscountRequest
from api.model.estimated_volume_discount_model import EstimatedVolumeDiscountModel
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
    api_instance = order_api.OrderApi(api_client)
    create_estimated_volume_discount_request = CreateEstimatedVolumeDiscountRequest(
        contract_term_month=12,
        quantity=1,
        start_date="yyyyMMdd",
        volume_discount_payment_type="MONTHLY",
        volume_discount_type="SORACOM_AIR_BASIC_CHARGE_V2",
    ) # CreateEstimatedVolumeDiscountRequest | Long term discount contract details

    # example passing only required values which don't have defaults set
    try:
        # Create long term discount quotation.
        api_response = api_instance.create_volume_discount_quotation(create_estimated_volume_discount_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->create_volume_discount_quotation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_estimated_volume_discount_request** | [**CreateEstimatedVolumeDiscountRequest**](CreateEstimatedVolumeDiscountRequest.md)| Long term discount contract details |

### Return type

[**EstimatedVolumeDiscountModel**](EstimatedVolumeDiscountModel.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order**
> GetOrderResponse get_order(order_id)

Get confirmed order.

Returns a confirmed order.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
from api.model.get_order_response import GetOrderResponse
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "order_id_example" # str | order_id

    # example passing only required values which don't have defaults set
    try:
        # Get confirmed order.
        api_response = api_instance.get_order(order_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->get_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| order_id |

### Return type

[**GetOrderResponse**](GetOrderResponse.md)

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

# **list_available_discounts**
> AvailableLongTermDiscountResponse list_available_discounts()

List available long term discounts.

Returns a list of available long term discounts.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
from api.model.available_long_term_discount_response import AvailableLongTermDiscountResponse
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
    api_instance = order_api.OrderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List available long term discounts.
        api_response = api_instance.list_available_discounts()
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->list_available_discounts: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AvailableLongTermDiscountResponse**](AvailableLongTermDiscountResponse.md)

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

# **list_ordered_subscribers**
> ListOrderedSubscriberResponse list_ordered_subscribers(order_id)

List ordered subscribers.

List ordered subscribers

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
from api.model.list_ordered_subscriber_response import ListOrderedSubscriberResponse
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "order_id_example" # str | order_id
    last_evaluated_key = "last_evaluated_key_example" # str | Serial number of the last subscriber in the previous page that is set to response header with X-Soracom-Next-Key. (optional)
    limit = 1 # int | Max number of subscribers in a response. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List ordered subscribers.
        api_response = api_instance.list_ordered_subscribers(order_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->list_ordered_subscribers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List ordered subscribers.
        api_response = api_instance.list_ordered_subscribers(order_id, last_evaluated_key=last_evaluated_key, limit=limit)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->list_ordered_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| order_id |
 **last_evaluated_key** | **str**| Serial number of the last subscriber in the previous page that is set to response header with X-Soracom-Next-Key. | [optional]
 **limit** | **int**| Max number of subscribers in a response. | [optional]

### Return type

[**ListOrderedSubscriberResponse**](ListOrderedSubscriberResponse.md)

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

# **list_orders**
> ListOrderResponse list_orders()

List confirmed orders.

Returns a list of confirmed orders.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
from api.model.list_order_response import ListOrderResponse
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
    api_instance = order_api.OrderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List confirmed orders.
        api_response = api_instance.list_orders()
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->list_orders: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListOrderResponse**](ListOrderResponse.md)

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

# **list_products**
> ListProductResponse list_products()

List products.

Returns a list of products.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
from api.model.list_product_response import ListProductResponse
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
    api_instance = order_api.OrderApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List products.
        api_response = api_instance.list_products()
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->list_products: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListProductResponse**](ListProductResponse.md)

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

# **register_ordered_sim**
> str register_ordered_sim(order_id)

Register subscribers for operator.

Registers the ordered SIM with the operator.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import order_api
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
    api_instance = order_api.OrderApi(api_client)
    order_id = "order_id_example" # str | order_id

    # example passing only required values which don't have defaults set
    try:
        # Register subscribers for operator.
        api_response = api_instance.register_ordered_sim(order_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling OrderApi->register_ordered_sim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| order_id |

### Return type

**str**

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Subscribers were registered for the operator. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

