# sandbox.StatsApi

All URIs are relative to *https://api-sandbox.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sandbox_insert_air_stats**](StatsApi.md#sandbox_insert_air_stats) | **POST** /sandbox/stats/air/subscribers/{imsi} | Inserts Air stats for testing
[**sandbox_insert_beam_stats**](StatsApi.md#sandbox_insert_beam_stats) | **POST** /sandbox/stats/beam/subscribers/{imsi} | Inserts Beam stats for testing


# **sandbox_insert_air_stats**
> sandbox_insert_air_stats(imsi, sandbox_insert_air_stats_request)

Inserts Air stats for testing

Populates Air stats for testing purpose. Inserted data are going to be automatically accumulated. It is not possible to put the data multiple times with the same timestamp.

### Example


```python
import time
import sandbox
from sandbox.api import stats_api
from sandbox.model.sandbox_insert_air_stats_request import SandboxInsertAirStatsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-sandbox.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sandbox.Configuration(
    host = "https://api-sandbox.soracom.io/v1"
)


# Enter a context with an instance of the API client
with sandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = stats_api.StatsApi(api_client)
    imsi = "imsi_example" # str | IMSI
    sandbox_insert_air_stats_request = SandboxInsertAirStatsRequest(
        data_traffic_stats_map=SandboxInsertAirStatsRequestDataTrafficStatsMap(
            s1_fast=SandboxDataTrafficStats(
                download_byte_size_total=1,
                download_packet_size_total=1,
                upload_byte_size_total=1,
                upload_packet_size_total=1,
            ),
            s1_minimum=SandboxDataTrafficStats(
                download_byte_size_total=1,
                download_packet_size_total=1,
                upload_byte_size_total=1,
                upload_packet_size_total=1,
            ),
            s1_slow=SandboxDataTrafficStats(
                download_byte_size_total=1,
                download_packet_size_total=1,
                upload_byte_size_total=1,
                upload_packet_size_total=1,
            ),
            s1_standard=SandboxDataTrafficStats(
                download_byte_size_total=1,
                download_packet_size_total=1,
                upload_byte_size_total=1,
                upload_packet_size_total=1,
            ),
        ),
        unixtime=1,
    ) # SandboxInsertAirStatsRequest | The Air stats (up/down bytes of data) with specified timestamp.

    # example passing only required values which don't have defaults set
    try:
        # Inserts Air stats for testing
        api_instance.sandbox_insert_air_stats(imsi, sandbox_insert_air_stats_request)
    except sandbox.ApiException as e:
        print("Exception when calling StatsApi->sandbox_insert_air_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI |
 **sandbox_insert_air_stats_request** | [**SandboxInsertAirStatsRequest**](SandboxInsertAirStatsRequest.md)| The Air stats (up/down bytes of data) with specified timestamp. |

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
**400** | Data with the same timestamp already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sandbox_insert_beam_stats**
> sandbox_insert_beam_stats(imsi, sandbox_insert_beam_stats_request)

Inserts Beam stats for testing

Populates Beam stats for testing purpose. Inserted data are going to be automatically accumulated. It is not possible to put the data multiple times with the same timestamp.

### Example


```python
import time
import sandbox
from sandbox.api import stats_api
from sandbox.model.sandbox_insert_beam_stats_request import SandboxInsertBeamStatsRequest
from pprint import pprint
# Defining the host is optional and defaults to https://api-sandbox.soracom.io/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = sandbox.Configuration(
    host = "https://api-sandbox.soracom.io/v1"
)


# Enter a context with an instance of the API client
with sandbox.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = stats_api.StatsApi(api_client)
    imsi = "imsi_example" # str | IMSI
    sandbox_insert_beam_stats_request = SandboxInsertBeamStatsRequest(
        beam_stats_map=SandboxInsertBeamStatsRequestBeamStatsMap(
            in_http=SandboxBeamCounts(
                count=1,
            ),
            in_mqtt=SandboxBeamCounts(
                count=1,
            ),
            in_tcp=SandboxBeamCounts(
                count=1,
            ),
            in_udp=SandboxBeamCounts(
                count=1,
            ),
            out_http=SandboxBeamCounts(
                count=1,
            ),
            out_https=SandboxBeamCounts(
                count=1,
            ),
            out_mqtt=SandboxBeamCounts(
                count=1,
            ),
            out_mqtts=SandboxBeamCounts(
                count=1,
            ),
            out_tcp=SandboxBeamCounts(
                count=1,
            ),
            out_tcps=SandboxBeamCounts(
                count=1,
            ),
            out_udp=SandboxBeamCounts(
                count=1,
            ),
        ),
        unixtime=1,
    ) # SandboxInsertBeamStatsRequest | The Beam stats (number of requests) with specified timestamp.

    # example passing only required values which don't have defaults set
    try:
        # Inserts Beam stats for testing
        api_instance.sandbox_insert_beam_stats(imsi, sandbox_insert_beam_stats_request)
    except sandbox.ApiException as e:
        print("Exception when calling StatsApi->sandbox_insert_beam_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **imsi** | **str**| IMSI |
 **sandbox_insert_beam_stats_request** | [**SandboxInsertBeamStatsRequest**](SandboxInsertBeamStatsRequest.md)| The Beam stats (number of requests) with specified timestamp. |

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
**400** | Data with the same timestamp already exists. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

