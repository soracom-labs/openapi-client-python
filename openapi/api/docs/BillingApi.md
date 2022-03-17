# api.BillingApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_billing**](BillingApi.md#export_billing) | **POST** /bills/{yyyyMM}/export | Output billing CSV file to S3.
[**export_latest_billing**](BillingApi.md#export_latest_billing) | **POST** /bills/latest/export | Export latest billing CSV file to S3.
[**get_billing**](BillingApi.md#get_billing) | **GET** /bills/{yyyyMM} | Get bill.
[**get_billing_history**](BillingApi.md#get_billing_history) | **GET** /bills | Get billing history.
[**get_billing_per_day**](BillingApi.md#get_billing_per_day) | **GET** /bills/{yyyyMM}/daily | Get bill per day.
[**get_latest_billing**](BillingApi.md#get_latest_billing) | **GET** /bills/latest | Get latest bill.


# **export_billing**
> FileExportResponse export_billing(yyyy_mm)

Output billing CSV file to S3.

Returns detailed information for the billing amounts for the specified month. This detailed information includes billing amounts per day, subscriber, and billing item.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import billing_api
from api.model.file_export_response import FileExportResponse
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
    api_instance = billing_api.BillingApi(api_client)
    yyyy_mm = "yyyyMM_example" # str | yyyyMM
    export_mode = "async" # str | export_mode (async, sync) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Output billing CSV file to S3.
        api_response = api_instance.export_billing(yyyy_mm)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling BillingApi->export_billing: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Output billing CSV file to S3.
        api_response = api_instance.export_billing(yyyy_mm, export_mode=export_mode)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling BillingApi->export_billing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **yyyy_mm** | **str**| yyyyMM |
 **export_mode** | **str**| export_mode (async, sync) | [optional]

### Return type

[**FileExportResponse**](FileExportResponse.md)

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

# **export_latest_billing**
> FileExportResponse export_latest_billing()

Export latest billing CSV file to S3.

Returns detailed information of the billing amounts for the latest month. This detailed information includes billing amounts per day, subscriber, and billing item. The amounts retrieved using this API correspond to the values before the invoice was finalized.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import billing_api
from api.model.file_export_response import FileExportResponse
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
    api_instance = billing_api.BillingApi(api_client)
    export_mode = "async" # str | export_mode (async, sync) (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export latest billing CSV file to S3.
        api_response = api_instance.export_latest_billing(export_mode=export_mode)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling BillingApi->export_latest_billing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_mode** | **str**| export_mode (async, sync) | [optional]

### Return type

[**FileExportResponse**](FileExportResponse.md)

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

# **get_billing**
> MonthlyBill get_billing(yyyy_mm)

Get bill.

Returns the billing history for the specified month (after applied discounts such as free tiers, etc., inclusive of tax). The amounts retrieved using this API correspond to the values before the invoice was finalized.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import billing_api
from api.model.monthly_bill import MonthlyBill
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
    api_instance = billing_api.BillingApi(api_client)
    yyyy_mm = "yyyyMM_example" # str | year and month

    # example passing only required values which don't have defaults set
    try:
        # Get bill.
        api_response = api_instance.get_billing(yyyy_mm)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling BillingApi->get_billing: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **yyyy_mm** | **str**| year and month |

### Return type

[**MonthlyBill**](MonthlyBill.md)

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

# **get_billing_history**
> GetBillingHistoryResponse get_billing_history()

Get billing history.

Returns past billing history (after applied discounts such as free tiers, etc., inclusive of tax). This API only returns the billing amounts that have been finalized at the end of the month.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import billing_api
from api.model.get_billing_history_response import GetBillingHistoryResponse
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
    api_instance = billing_api.BillingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get billing history.
        api_response = api_instance.get_billing_history()
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling BillingApi->get_billing_history: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetBillingHistoryResponse**](GetBillingHistoryResponse.md)

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

# **get_billing_per_day**
> DailyBillResponse get_billing_per_day(yyyy_mm)

Get bill per day.

Returns detailed information of billing amounts per day for the specified month. This API only returns the billing amounts that have been finalized.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import billing_api
from api.model.daily_bill_response import DailyBillResponse
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
    api_instance = billing_api.BillingApi(api_client)
    yyyy_mm = "yyyyMM_example" # str | year and month

    # example passing only required values which don't have defaults set
    try:
        # Get bill per day.
        api_response = api_instance.get_billing_per_day(yyyy_mm)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling BillingApi->get_billing_per_day: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **yyyy_mm** | **str**| year and month |

### Return type

[**DailyBillResponse**](DailyBillResponse.md)

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

# **get_latest_billing**
> GetLatestBill get_latest_billing()

Get latest bill.

Returns the latest billing amounts after applied discounts such as free tiers, etc. The amounts retrieved using this API correspond to the values before the invoice was finalized.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import billing_api
from api.model.get_latest_bill import GetLatestBill
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
    api_instance = billing_api.BillingApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get latest bill.
        api_response = api_instance.get_latest_billing()
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling BillingApi->get_latest_billing: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetLatestBill**](GetLatestBill.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

