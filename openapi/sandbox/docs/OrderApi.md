# sandbox.OrderApi

All URIs are relative to *https://api-sandbox.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sandbox_ship_order**](OrderApi.md#sandbox_ship_order) | **POST** /sandbox/orders/ship | Ships the specified order.


# **sandbox_ship_order**
> sandbox_ship_order(sandbox_ship_order_request)

Ships the specified order.

Changes the shipping status to 'shipped' and gets ready the subscribers included in the order.

### Example


```python
import time
import sandbox
from sandbox.api import order_api
from sandbox.model.sandbox_ship_order_request import SandboxShipOrderRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-sandbox.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sandbox.Configuration(
    host = "https://api-sandbox.soracom.io/v1"
)


# Enter a context with an instance of the API client
with sandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = order_api.OrderApi(api_client)
    sandbox_ship_order_request = SandboxShipOrderRequest(
        operator_id="operator_id_example",
        order_id="order_id_example",
    ) # SandboxShipOrderRequest | Shipping request

    # example passing only required values which don't have defaults set
    try:
        # Ships the specified order.
        api_instance.sandbox_ship_order(sandbox_ship_order_request)
    except sandbox.ApiException as e:
        print("Exception when calling OrderApi->sandbox_ship_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_ship_order_request** | [**SandboxShipOrderRequest**](SandboxShipOrderRequest.md)| Shipping request |

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
**400** | Order does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

