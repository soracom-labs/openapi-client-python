# soracom_api.QueryApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_devices**](QueryApi.md#search_devices) | **GET** /query/devices | Search SORACOM Inventory devices by query
[**search_sigfox_devices**](QueryApi.md#search_sigfox_devices) | **GET** /query/sigfox_devices | Search Sigfox devices by query
[**search_sims**](QueryApi.md#search_sims) | **GET** /query/sims | Search SIMs by query terms
[**search_subscriber_traffic_volume_ranking**](QueryApi.md#search_subscriber_traffic_volume_ranking) | **GET** /query/subscribers/traffic_volume/ranking | Search traffic volume ranking of subscribers
[**search_subscribers**](QueryApi.md#search_subscribers) | **GET** /query/subscribers | (DEPRECATED) Search subscribers by query terms


# **search_devices**
> [Device] search_devices()

Search SORACOM Inventory devices by query

Search SORACOM Inventory devices by query terms. It returns partial match results. When this API permission is allowed, it grants the authority to search and retrieve all SORACOM Inventory devices that includes their group information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import query_api
from soracom_api.model.device import Device
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
    api_instance = query_api.QueryApi(api_client)
    name = [
        "name_example",
    ] # [str] | Name to search (optional)
    group = [
        "group_example",
    ] # [str] | Group name to search (optional)
    device_id = [
        "deviceId_example",
    ] # [str] | SORACOM Inventory device ID to search (optional)
    tag = [
        "tag_example",
    ] # [str] | String of tag values to search (optional)
    imsi = [
        "imsi_example",
    ] # [str] | IMSI of the device that was used on bootstrapping (optional)
    imei = [
        "imei_example",
    ] # [str] | IMEI of the device that was used on bootstrapping (optional)
    limit = 10 # int | The maximum number of item to retrieve (optional) if omitted the server will use the default value of 10
    last_evaluated_key = "last_evaluated_key_example" # str | The SORACOM Inventory device ID of the last Inventory device retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next Inventory device onward. (optional)
    search_type = "and" # str | Type of the search ('AND searching' or 'OR searching') (optional) if omitted the server will use the default value of "and"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search SORACOM Inventory devices by query
        api_response = api_instance.search_devices(name=name, group=group, device_id=device_id, tag=tag, imsi=imsi, imei=imei, limit=limit, last_evaluated_key=last_evaluated_key, search_type=search_type)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling QueryApi->search_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **[str]**| Name to search | [optional]
 **group** | **[str]**| Group name to search | [optional]
 **device_id** | **[str]**| SORACOM Inventory device ID to search | [optional]
 **tag** | **[str]**| String of tag values to search | [optional]
 **imsi** | **[str]**| IMSI of the device that was used on bootstrapping | [optional]
 **imei** | **[str]**| IMEI of the device that was used on bootstrapping | [optional]
 **limit** | **int**| The maximum number of item to retrieve | [optional] if omitted the server will use the default value of 10
 **last_evaluated_key** | **str**| The SORACOM Inventory device ID of the last Inventory device retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next Inventory device onward. | [optional]
 **search_type** | **str**| Type of the search (&#39;AND searching&#39; or &#39;OR searching&#39;) | [optional] if omitted the server will use the default value of "and"

### Return type

[**[Device]**](Device.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns result of searching |  -  |
**400** | Invalid search queries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sigfox_devices**
> [SigfoxDevice] search_sigfox_devices()

Search Sigfox devices by query

Search Sigfox devices by query terms. It returns partial match results. When this API permission is allowed, it grants the authority to search and retrieve all Sigfox devices that includes their group information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import query_api
from soracom_api.model.sigfox_device import SigfoxDevice
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
    api_instance = query_api.QueryApi(api_client)
    name = [
        "name_example",
    ] # [str] | Name to search (optional)
    group = [
        "group_example",
    ] # [str] | Group name to search (optional)
    device_id = [
        "deviceId_example",
    ] # [str] | Sigfox device ID to search (optional)
    tag = [
        "tag_example",
    ] # [str] | String of tag values to search (optional)
    status = "and" # str | Status of sigfox devices (optional) if omitted the server will use the default value of "and"
    registration = "and" # str | Registration status of sigfox devices (optional) if omitted the server will use the default value of "and"
    limit = 10 # int | The maximum number of item to retrieve (optional) if omitted the server will use the default value of 10
    last_evaluated_key = "last_evaluated_key_example" # str | The Sigfox device ID of the last Sigfox device retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next Sigfox device onward. (optional)
    search_type = "and" # str | Type of the search ('AND searching' or 'OR searching') (optional) if omitted the server will use the default value of "and"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search Sigfox devices by query
        api_response = api_instance.search_sigfox_devices(name=name, group=group, device_id=device_id, tag=tag, status=status, registration=registration, limit=limit, last_evaluated_key=last_evaluated_key, search_type=search_type)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling QueryApi->search_sigfox_devices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **[str]**| Name to search | [optional]
 **group** | **[str]**| Group name to search | [optional]
 **device_id** | **[str]**| Sigfox device ID to search | [optional]
 **tag** | **[str]**| String of tag values to search | [optional]
 **status** | **str**| Status of sigfox devices | [optional] if omitted the server will use the default value of "and"
 **registration** | **str**| Registration status of sigfox devices | [optional] if omitted the server will use the default value of "and"
 **limit** | **int**| The maximum number of item to retrieve | [optional] if omitted the server will use the default value of 10
 **last_evaluated_key** | **str**| The Sigfox device ID of the last Sigfox device retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next Sigfox device onward. | [optional]
 **search_type** | **str**| Type of the search (&#39;AND searching&#39; or &#39;OR searching&#39;) | [optional] if omitted the server will use the default value of "and"

### Return type

[**[SigfoxDevice]**](SigfoxDevice.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns result of searching |  -  |
**400** | Invalid search queries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_sims**
> [Sim] search_sims()

Search SIMs by query terms

Search SIMs by query terms. It returns partial match results. When this API permission is allowed, it grants the authority to search and retrieve all SIMs that includes their group information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import query_api
from soracom_api.model.sim import Sim
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
    api_instance = query_api.QueryApi(api_client)
    name = [
        "name_example",
    ] # [str] | Name to search (optional)
    group = [
        "group_example",
    ] # [str] | Group name to search (optional)
    sim_id = [
        "sim_id_example",
    ] # [str] | Identifier of the SIM to search (optional)
    imsi = [
        "imsi_example",
    ] # [str] | IMSI to search (optional)
    msisdn = [
        "msisdn_example",
    ] # [str] | MSISDN to search (optional)
    iccid = [
        "iccid_example",
    ] # [str] | ICCID to search (optional)
    serial_number = [
        "serial_number_example",
    ] # [str] | Serial number to search (optional)
    tag = [
        "tag_example",
    ] # [str] | String of tag values to search (optional)
    bundles = [
        "bundles_example",
    ] # [str] | Bundles type to search (optional)
    session_status = "NA" # str | Status of the session to search (ONLINE or OFFLINE) (optional) if omitted the server will use the default value of "NA"
    limit = 10 # int | The maximum number of item to retrieve (optional) if omitted the server will use the default value of 10
    last_evaluated_key = "last_evaluated_key_example" # str | The SIM ID of the last SIM retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next SIM onward. (optional)
    search_type = "and" # str | Type of the search ('AND searching' or 'OR searching') (optional) if omitted the server will use the default value of "and"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search SIMs by query terms
        api_response = api_instance.search_sims(name=name, group=group, sim_id=sim_id, imsi=imsi, msisdn=msisdn, iccid=iccid, serial_number=serial_number, tag=tag, bundles=bundles, session_status=session_status, limit=limit, last_evaluated_key=last_evaluated_key, search_type=search_type)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling QueryApi->search_sims: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **[str]**| Name to search | [optional]
 **group** | **[str]**| Group name to search | [optional]
 **sim_id** | **[str]**| Identifier of the SIM to search | [optional]
 **imsi** | **[str]**| IMSI to search | [optional]
 **msisdn** | **[str]**| MSISDN to search | [optional]
 **iccid** | **[str]**| ICCID to search | [optional]
 **serial_number** | **[str]**| Serial number to search | [optional]
 **tag** | **[str]**| String of tag values to search | [optional]
 **bundles** | **[str]**| Bundles type to search | [optional]
 **session_status** | **str**| Status of the session to search (ONLINE or OFFLINE) | [optional] if omitted the server will use the default value of "NA"
 **limit** | **int**| The maximum number of item to retrieve | [optional] if omitted the server will use the default value of 10
 **last_evaluated_key** | **str**| The SIM ID of the last SIM retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next SIM onward. | [optional]
 **search_type** | **str**| Type of the search (&#39;AND searching&#39; or &#39;OR searching&#39;) | [optional] if omitted the server will use the default value of "and"

### Return type

[**[Sim]**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns result of searching |  -  |
**400** | Invalid search queries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_subscriber_traffic_volume_ranking**
> [TrafficVolumeRanking] search_subscriber_traffic_volume_ranking(_from, to)

Search traffic volume ranking of subscribers

Search traffic volume ranking of subscribers

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import query_api
from soracom_api.model.traffic_volume_ranking import TrafficVolumeRanking
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
    api_instance = query_api.QueryApi(api_client)
    _from = 1 # int | The beginning point of searching range (unixtime: in milliseconds)
    to = 1 # int | The end point of searching range (unixtime: in milliseconds)
    limit = 10 # int | The maximum number of item to retrieve (optional) if omitted the server will use the default value of 10
    order = "desc" # str | The order of ranking (optional) if omitted the server will use the default value of "desc"

    # example passing only required values which don't have defaults set
    try:
        # Search traffic volume ranking of subscribers
        api_response = api_instance.search_subscriber_traffic_volume_ranking(_from, to)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling QueryApi->search_subscriber_traffic_volume_ranking: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Search traffic volume ranking of subscribers
        api_response = api_instance.search_subscriber_traffic_volume_ranking(_from, to, limit=limit, order=order)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling QueryApi->search_subscriber_traffic_volume_ranking: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| The beginning point of searching range (unixtime: in milliseconds) |
 **to** | **int**| The end point of searching range (unixtime: in milliseconds) |
 **limit** | **int**| The maximum number of item to retrieve | [optional] if omitted the server will use the default value of 10
 **order** | **str**| The order of ranking | [optional] if omitted the server will use the default value of "desc"

### Return type

[**[TrafficVolumeRanking]**](TrafficVolumeRanking.md)

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

# **search_subscribers**
> [Subscriber] search_subscribers()

(DEPRECATED) Search subscribers by query terms

(DEPRECATED: please consider to use `/query/sims` API instead) Search subscribers by query terms. It returns partial match results. When this API permission is allowed, it grants the authority to search and retrieve all SIMs that includes their group information.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import query_api
from soracom_api.model.subscriber import Subscriber
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
    api_instance = query_api.QueryApi(api_client)
    name = [
        "name_example",
    ] # [str] | Name to search (optional)
    group = [
        "group_example",
    ] # [str] | Group name to search (optional)
    imsi = [
        "imsi_example",
    ] # [str] | IMSI to search (optional)
    msisdn = [
        "msisdn_example",
    ] # [str] | MSISDN to search (optional)
    iccid = [
        "iccid_example",
    ] # [str] | ICCID to search (optional)
    serial_number = [
        "serial_number_example",
    ] # [str] | Serial number to search (optional)
    tag = [
        "tag_example",
    ] # [str] | String of tag values to search (optional)
    subscription = [
        "subscription_example",
    ] # [str] | Subscription (e.g. `plan01s`) to search (optional)
    module_type = [
        "module_type_example",
    ] # [str] | Module type (e.g. `mini`, `virtual`) to search (optional)
    limit = 10 # int | The maximum number of item to retrieve (optional) if omitted the server will use the default value of 10
    last_evaluated_key = "last_evaluated_key_example" # str | The IMSI of the last subscriber retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next subscriber onward. (optional)
    search_type = "and" # str | Type of the search ('AND searching' or 'OR searching') (optional) if omitted the server will use the default value of "and"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # (DEPRECATED) Search subscribers by query terms
        api_response = api_instance.search_subscribers(name=name, group=group, imsi=imsi, msisdn=msisdn, iccid=iccid, serial_number=serial_number, tag=tag, subscription=subscription, module_type=module_type, limit=limit, last_evaluated_key=last_evaluated_key, search_type=search_type)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling QueryApi->search_subscribers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **[str]**| Name to search | [optional]
 **group** | **[str]**| Group name to search | [optional]
 **imsi** | **[str]**| IMSI to search | [optional]
 **msisdn** | **[str]**| MSISDN to search | [optional]
 **iccid** | **[str]**| ICCID to search | [optional]
 **serial_number** | **[str]**| Serial number to search | [optional]
 **tag** | **[str]**| String of tag values to search | [optional]
 **subscription** | **[str]**| Subscription (e.g. &#x60;plan01s&#x60;) to search | [optional]
 **module_type** | **[str]**| Module type (e.g. &#x60;mini&#x60;, &#x60;virtual&#x60;) to search | [optional]
 **limit** | **int**| The maximum number of item to retrieve | [optional] if omitted the server will use the default value of 10
 **last_evaluated_key** | **str**| The IMSI of the last subscriber retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next subscriber onward. | [optional]
 **search_type** | **str**| Type of the search (&#39;AND searching&#39; or &#39;OR searching&#39;) | [optional] if omitted the server will use the default value of "and"

### Return type

[**[Subscriber]**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns result of searching |  -  |
**400** | Invalid search queries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

