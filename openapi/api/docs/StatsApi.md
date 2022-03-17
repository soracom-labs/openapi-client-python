# api.StatsApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_air_stats**](StatsApi.md#export_air_stats) | **POST** /stats/air/operators/{operator_id}/export | Export Air Usage Report of All Subscribers.
[**export_beam_stats**](StatsApi.md#export_beam_stats) | **POST** /stats/beam/operators/{operator_id}/export | Export Beam Usage Report of All Subscribers.
[**get_air_stats**](StatsApi.md#get_air_stats) | **GET** /stats/air/subscribers/{imsi} | Get Air Usage Report of Subscriber.
[**get_air_stats_of_sim**](StatsApi.md#get_air_stats_of_sim) | **GET** /stats/air/sims/{simId} | Get Air Usage Report of SIM.
[**get_beam_stats**](StatsApi.md#get_beam_stats) | **GET** /stats/beam/subscribers/{imsi} | Get Beam Usage Report of Subscriber.
[**get_harvest_exported_data_stats**](StatsApi.md#get_harvest_exported_data_stats) | **GET** /stats/harvest/operators/{operator_id} | Get &#39;Harvest usage report&#39; for the specified operator.
[**get_napter_audit_logs_exported_data_stats**](StatsApi.md#get_napter_audit_logs_exported_data_stats) | **GET** /stats/napter/audit_logs | Get Napter audit logs&#39; monthly exported data stats


# **export_air_stats**
> FileExportResponse export_air_stats(operator_id, export_request)

Export Air Usage Report of All Subscribers.

Retrieves a file containing the usage report of all subscribers for the specified operator. The report data range is specified with from, to in unixtime. The report contains monthly data. The file output destination is AWS S3. The file output format is CSV.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import stats_api
from api.model.file_export_response import FileExportResponse
from api.model.export_request import ExportRequest
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
    api_instance = stats_api.StatsApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    export_request = ExportRequest(
        _from=1,
        period="month",
        to=1,
    ) # ExportRequest | export time period
    export_mode = "async" # str | export_mode (async, sync) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export Air Usage Report of All Subscribers.
        api_response = api_instance.export_air_stats(operator_id, export_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling StatsApi->export_air_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export Air Usage Report of All Subscribers.
        api_response = api_instance.export_air_stats(operator_id, export_request, export_mode=export_mode)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling StatsApi->export_air_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **export_request** | [**ExportRequest**](ExportRequest.md)| export time period |
 **export_mode** | **str**| export_mode (async, sync) | [optional]

### Return type

[**FileExportResponse**](FileExportResponse.md)

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

# **export_beam_stats**
> FileExportResponse export_beam_stats(operator_id, export_request)

Export Beam Usage Report of All Subscribers.

Retrieves a file containing the usage report of all subscribers for the specified operator. The report data range is specified with from, to in unixtime. The report contains monthly data. The file output destination is AWS S3. The file output format is CSV.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import stats_api
from api.model.file_export_response import FileExportResponse
from api.model.export_request import ExportRequest
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
    api_instance = stats_api.StatsApi(api_client)
    operator_id = "operator_id_example" # str | operator ID
    export_request = ExportRequest(
        _from=1,
        period="month",
        to=1,
    ) # ExportRequest | export time period
    export_mode = "async" # str | export_mode (async, sync) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Export Beam Usage Report of All Subscribers.
        api_response = api_instance.export_beam_stats(operator_id, export_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling StatsApi->export_beam_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export Beam Usage Report of All Subscribers.
        api_response = api_instance.export_beam_stats(operator_id, export_request, export_mode=export_mode)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling StatsApi->export_beam_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator ID |
 **export_request** | [**ExportRequest**](ExportRequest.md)| export time period |
 **export_mode** | **str**| export_mode (async, sync) | [optional]

### Return type

[**FileExportResponse**](FileExportResponse.md)

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

# **get_air_stats**
> [AirStatsResponse] get_air_stats(imsi, _from, to, period)

Get Air Usage Report of Subscriber.

Retrieves the usage report for the subscriber specified by the IMSI.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import stats_api
from api.model.air_stats_response import AirStatsResponse
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
    api_instance = stats_api.StatsApi(api_client)
    imsi = "imsi_example" # str | imsi
    _from = 1 # int | Start time in unixtime for the aggregate data.
    to = 1 # int | End time in unixtime for the aggregate data.
    period = "month" # str | Units of aggregate data. For minutes, the interval is around 5 minutes.

    # example passing only required values which don't have defaults set
    try:
        # Get Air Usage Report of Subscriber.
        api_response = api_instance.get_air_stats(imsi, _from, to, period)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling StatsApi->get_air_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| imsi |
 **_from** | **int**| Start time in unixtime for the aggregate data. |
 **to** | **int**| End time in unixtime for the aggregate data. |
 **period** | **str**| Units of aggregate data. For minutes, the interval is around 5 minutes. |

### Return type

[**[AirStatsResponse]**](AirStatsResponse.md)

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

# **get_air_stats_of_sim**
> [AirStatsResponse] get_air_stats_of_sim(sim_id, _from, to, period)

Get Air Usage Report of SIM.

Retrieves the usage report for the SIM specified by the simId.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import stats_api
from api.model.air_stats_response import AirStatsResponse
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
    api_instance = stats_api.StatsApi(api_client)
    sim_id = "simId_example" # str | SIM ID
    _from = 1 # int | Start time in unixtime for the aggregate data.
    to = 1 # int | End time in unixtime for the aggregate data.
    period = "month" # str | Units of aggregate data. For minutes, the interval is around 5 minutes.

    # example passing only required values which don't have defaults set
    try:
        # Get Air Usage Report of SIM.
        api_response = api_instance.get_air_stats_of_sim(sim_id, _from, to, period)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling StatsApi->get_air_stats_of_sim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID |
 **_from** | **int**| Start time in unixtime for the aggregate data. |
 **to** | **int**| End time in unixtime for the aggregate data. |
 **period** | **str**| Units of aggregate data. For minutes, the interval is around 5 minutes. |

### Return type

[**[AirStatsResponse]**](AirStatsResponse.md)

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

# **get_beam_stats**
> [BeamStatsResponse] get_beam_stats(imsi, _from, to, period)

Get Beam Usage Report of Subscriber.

Retrieves the Soracom Beam usage report for the subscriber specified by the IMSI.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import stats_api
from api.model.beam_stats_response import BeamStatsResponse
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
    api_instance = stats_api.StatsApi(api_client)
    imsi = "imsi_example" # str | imsi
    _from = 1 # int | Start time in unixtime for the aggregate data.
    to = 1 # int | End time in unixtime for the aggregate data.
    period = "month" # str | Units of aggregate data. For minutes, the interval is around 5 minutes.

    # example passing only required values which don't have defaults set
    try:
        # Get Beam Usage Report of Subscriber.
        api_response = api_instance.get_beam_stats(imsi, _from, to, period)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling StatsApi->get_beam_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| imsi |
 **_from** | **int**| Start time in unixtime for the aggregate data. |
 **to** | **int**| End time in unixtime for the aggregate data. |
 **period** | **str**| Units of aggregate data. For minutes, the interval is around 5 minutes. |

### Return type

[**[BeamStatsResponse]**](BeamStatsResponse.md)

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

# **get_harvest_exported_data_stats**
> HarvestExportedDataStatsResponse get_harvest_exported_data_stats(operator_id)

Get 'Harvest usage report' for the specified operator.

Retrieves the SORACOM Harvest usage report for the operator.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import stats_api
from api.model.harvest_exported_data_stats_response import HarvestExportedDataStatsResponse
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
    api_instance = stats_api.StatsApi(api_client)
    operator_id = "operator_id_example" # str | operator_id
    year_month = "year_month_example" # str | Year/Month in 'YYYYMM' format. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get 'Harvest usage report' for the specified operator.
        api_response = api_instance.get_harvest_exported_data_stats(operator_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling StatsApi->get_harvest_exported_data_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get 'Harvest usage report' for the specified operator.
        api_response = api_instance.get_harvest_exported_data_stats(operator_id, year_month=year_month)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling StatsApi->get_harvest_exported_data_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **operator_id** | **str**| operator_id |
 **year_month** | **str**| Year/Month in &#39;YYYYMM&#39; format. | [optional]

### Return type

[**HarvestExportedDataStatsResponse**](HarvestExportedDataStatsResponse.md)

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

# **get_napter_audit_logs_exported_data_stats**
> NapterAuditLogsExportedDataStatsResponse get_napter_audit_logs_exported_data_stats()

Get Napter audit logs' monthly exported data stats

Get Napter audit logs' monthly exported data stats

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import stats_api
from api.model.napter_audit_logs_exported_data_stats_response import NapterAuditLogsExportedDataStatsResponse
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
    api_instance = stats_api.StatsApi(api_client)
    year_month = "year_month_example" # str | Year/Month in 'YYYYMM' format. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Napter audit logs' monthly exported data stats
        api_response = api_instance.get_napter_audit_logs_exported_data_stats(year_month=year_month)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling StatsApi->get_napter_audit_logs_exported_data_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year_month** | **str**| Year/Month in &#39;YYYYMM&#39; format. | [optional]

### Return type

[**NapterAuditLogsExportedDataStatsResponse**](NapterAuditLogsExportedDataStatsResponse.md)

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

