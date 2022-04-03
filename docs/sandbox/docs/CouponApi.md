# soracom_sandbox.CouponApi

All URIs are relative to *https://api-sandbox.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sandbox_create_coupon**](CouponApi.md#sandbox_create_coupon) | **POST** /sandbox/coupons/create | Creates a coupon


# **sandbox_create_coupon**
> SandboxCreateCouponResponse sandbox_create_coupon(sandbox_create_coupon_request)

Creates a coupon

Creates a coupon.

### Example


```python
import time
import soracom_sandbox
from soracom_sandbox.api import coupon_api
from soracom_sandbox.model.sandbox_create_coupon_request import SandboxCreateCouponRequest
from soracom_sandbox.model.sandbox_create_coupon_response import SandboxCreateCouponResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api-sandbox.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = soracom_sandbox.Configuration(
    host = "https://api-sandbox.soracom.io/v1"
)


# Enter a context with an instance of the API client
with soracom_sandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = coupon_api.CouponApi(api_client)
    sandbox_create_coupon_request = SandboxCreateCouponRequest(
        amount=1000,
        applicable_bill_item_name="dailyDataTrafficChargeTotal",
        expiry_year_month="yyyyMM",
    ) # SandboxCreateCouponRequest | request

    # example passing only required values which don't have defaults set
    try:
        # Creates a coupon
        api_response = api_instance.sandbox_create_coupon(sandbox_create_coupon_request)
        pprint(api_response)
    except soracom_sandbox.ApiException as e:
        print("Exception when calling CouponApi->sandbox_create_coupon: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_create_coupon_request** | [**SandboxCreateCouponRequest**](SandboxCreateCouponRequest.md)| request |

### Return type

[**SandboxCreateCouponResponse**](SandboxCreateCouponResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Request is not correct. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

