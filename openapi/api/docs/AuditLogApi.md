# api.AuditLogApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_audit_logs**](AuditLogApi.md#get_api_audit_logs) | **GET** /audit_logs/api | Retrieve audit logs for API calls
[**get_napter_audit_logs**](AuditLogApi.md#get_napter_audit_logs) | **GET** /audit_logs/napter | Retrieve audit logs for Napter


# **get_api_audit_logs**
> [APIAuditLogEntry] get_api_audit_logs()

Retrieve audit logs for API calls

Retrieve audit logs for API calls.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import audit_log_api
from api.model.api_audit_log_entry import APIAuditLogEntry
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
    api_instance = audit_log_api.AuditLogApi(api_client)
    api_kind = "api_kind_example" # str | Filter item for audit log retrieval by API kind (e.g. `/v1/auth`). (optional)
    from_epoch_ms = 1 # int | Start time for the log search range (unixtime milliseconds). (optional)
    to_epoch_ms = 1 # int | End time for the log search range (unixtime milliseconds). (optional)
    limit = 1 # int | Maximum number of log entries to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The value of `requestedTimeEpochMs` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve audit logs for API calls
        api_response = api_instance.get_api_audit_logs(api_kind=api_kind, from_epoch_ms=from_epoch_ms, to_epoch_ms=to_epoch_ms, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling AuditLogApi->get_api_audit_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_kind** | **str**| Filter item for audit log retrieval by API kind (e.g. &#x60;/v1/auth&#x60;). | [optional]
 **from_epoch_ms** | **int**| Start time for the log search range (unixtime milliseconds). | [optional]
 **to_epoch_ms** | **int**| End time for the log search range (unixtime milliseconds). | [optional]
 **limit** | **int**| Maximum number of log entries to retrieve. | [optional]
 **last_evaluated_key** | **str**| The value of &#x60;requestedTimeEpochMs&#x60; in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. | [optional]

### Return type

[**[APIAuditLogEntry]**](APIAuditLogEntry.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of API audit log entries. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_napter_audit_logs**
> [NapterAuditLogEntry] get_napter_audit_logs()

Retrieve audit logs for Napter

Retrieve audit logs for Napter.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import audit_log_api
from api.model.napter_audit_log_entry import NapterAuditLogEntry
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
    api_instance = audit_log_api.AuditLogApi(api_client)
    resource_type = "Subscriber" # str | Type of the target resource to query Napter audit log entries. (optional) if omitted the server will use the default value of "Subscriber"
    resource_id = "resource_id_example" # str | Identity of the target resource to query log entries. (optional)
    _from = 1 # int | Start time for the log search range (unixtime milliseconds). (optional)
    to = 1 # int | End time for the log search range (unixtime milliseconds). (optional)
    limit = 1 # int | Maximum number of log entries to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The value of `time` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve audit logs for Napter
        api_response = api_instance.get_napter_audit_logs(resource_type=resource_type, resource_id=resource_id, _from=_from, to=to, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling AuditLogApi->get_napter_audit_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **resource_type** | **str**| Type of the target resource to query Napter audit log entries. | [optional] if omitted the server will use the default value of "Subscriber"
 **resource_id** | **str**| Identity of the target resource to query log entries. | [optional]
 **_from** | **int**| Start time for the log search range (unixtime milliseconds). | [optional]
 **to** | **int**| End time for the log search range (unixtime milliseconds). | [optional]
 **limit** | **int**| Maximum number of log entries to retrieve. | [optional]
 **last_evaluated_key** | **str**| The value of &#x60;time&#x60; in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. | [optional]

### Return type

[**[NapterAuditLogEntry]**](NapterAuditLogEntry.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of Napter audit log entries. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

