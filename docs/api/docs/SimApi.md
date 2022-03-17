# soracom_api.SimApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_sim**](SimApi.md#activate_sim) | **POST** /sims/{sim_id}/activate | Activate SIM.
[**add_subscription**](SimApi.md#add_subscription) | **POST** /sims/{sim_id}/profiles/{iccid}/add_subscription | Adds a new subscription container to a SIM profile
[**attach_arc_sim_credentials**](SimApi.md#attach_arc_sim_credentials) | **POST** /sims/{sim_id}/credentials/arc | (DEPRECATED) Attach the credentials for Arc to a SIM.
[**cancel_subscription_container_download**](SimApi.md#cancel_subscription_container_download) | **POST** /sims/{sim_id}/profiles/{iccid}/subscribers/{imsi}/cancel_download | Cancel subscription download to subscription container
[**create_arc_session**](SimApi.md#create_arc_session) | **POST** /sims/{sim_id}/sessions/arc | Re-create an Arc session.
[**create_sim**](SimApi.md#create_sim) | **POST** /sims | Create a SIM.
[**create_sim_packet_capture_session**](SimApi.md#create_sim_packet_capture_session) | **POST** /sims/{sim_id}/packet_capture_sessions | Create Packet Capture Session
[**deactivate_sim**](SimApi.md#deactivate_sim) | **POST** /sims/{sim_id}/deactivate | Deactivate SIM.
[**delete_sim_packet_capture_session**](SimApi.md#delete_sim_packet_capture_session) | **DELETE** /sims/{sim_id}/packet_capture_sessions/{session_id} | Delete Packet Capture Session
[**delete_sim_session**](SimApi.md#delete_sim_session) | **POST** /sims/{sim_id}/delete_session | Delete Session
[**delete_sim_tag**](SimApi.md#delete_sim_tag) | **DELETE** /sims/{sim_id}/tags/{tag_name} | Delete SIM tag.
[**delete_subscription_container_country_mapping_entry**](SimApi.md#delete_subscription_container_country_mapping_entry) | **DELETE** /sims/{sim_id}/profiles/{iccid}/subscription_containers/country_mapping/{mcc} | Delete subscription container mapping entries
[**disable_sim_termination**](SimApi.md#disable_sim_termination) | **POST** /sims/{sim_id}/disable_termination | Disable termination of the SIM.
[**downlink_ping_to_user_equipment**](SimApi.md#downlink_ping_to_user_equipment) | **POST** /sims/{sim_id}/downlink/ping | Send ping requests to a SIM.
[**enable_sim_termination**](SimApi.md#enable_sim_termination) | **POST** /sims/{sim_id}/enable_termination | Enable termination of the SIM.
[**enable_subscription_container**](SimApi.md#enable_subscription_container) | **POST** /sims/{sim_id}/profiles/{iccid}/subscription_containers/{containerId}/enable | Enables a subscription container.
[**get_data_from_sim**](SimApi.md#get_data_from_sim) | **GET** /sims/{sim_id}/data | Get data sent from a SIM.
[**get_sim**](SimApi.md#get_sim) | **GET** /sims/{sim_id} | Get a SIM identified by sim_id
[**get_sim_packet_capture_session**](SimApi.md#get_sim_packet_capture_session) | **GET** /sims/{sim_id}/packet_capture_sessions/{session_id} | Get Packet Capture Session
[**list_sim_packet_capture_sessions**](SimApi.md#list_sim_packet_capture_sessions) | **GET** /sims/{sim_id}/packet_capture_sessions | List Packet Capture Sessions
[**list_sim_session_events**](SimApi.md#list_sim_session_events) | **GET** /sims/{sim_id}/events/sessions | List Session Events.
[**list_sims**](SimApi.md#list_sims) | **GET** /sims | List SIMs.
[**list_subscription_containers**](SimApi.md#list_subscription_containers) | **GET** /sims/{sim_id}/profiles/{iccid}/subscription_containers | Get subscription container status.
[**put_sim_tags**](SimApi.md#put_sim_tags) | **PUT** /sims/{sim_id}/tags | Bulk insert or update SIM tags.
[**put_subscription_container_country_mapping_entries**](SimApi.md#put_subscription_container_country_mapping_entries) | **PUT** /sims/{sim_id}/profiles/{iccid}/subscription_containers/country_mapping | Updates subscription container country mapping entries.
[**register_sim**](SimApi.md#register_sim) | **POST** /sims/{sim_id}/register | Register SIM.
[**remove_arc_sim_credentials**](SimApi.md#remove_arc_sim_credentials) | **DELETE** /sims/{sim_id}/credentials/arc | (DEPRECATED) Remove the credentials for Arc from a SIM.
[**renew_arc_sim_credentials**](SimApi.md#renew_arc_sim_credentials) | **PUT** /sims/{sim_id}/credentials/arc | Renew the credentials for Arc to a SIM.
[**report_sim_local_info**](SimApi.md#report_sim_local_info) | **POST** /sims/{sim_id}/report_local_info | Triggers SIM to report SIM local info.
[**send_sms_to_sim**](SimApi.md#send_sms_to_sim) | **POST** /sims/{sim_id}/send_sms | Send SMS to SIM
[**set_sim_expiry_time**](SimApi.md#set_sim_expiry_time) | **POST** /sims/{sim_id}/set_expiry_time | Update expiry time of SIM.
[**set_sim_group**](SimApi.md#set_sim_group) | **POST** /sims/{sim_id}/set_group | Set Group id of a SIM.
[**set_sim_imei_lock**](SimApi.md#set_sim_imei_lock) | **POST** /sims/{sim_id}/set_imei_lock | Set IMEI lock configuration for the SIM.
[**set_sim_to_standby**](SimApi.md#set_sim_to_standby) | **POST** /sims/{sim_id}/set_to_standby | Set SIM to standby mode.
[**stop_sim_packet_capture_session**](SimApi.md#stop_sim_packet_capture_session) | **POST** /sims/{sim_id}/packet_capture_sessions/{session_id}/stop | Stop SIM Packet Capture Session
[**suspend_sim**](SimApi.md#suspend_sim) | **POST** /sims/{sim_id}/suspend | Suspend SIM.
[**terminate_sim**](SimApi.md#terminate_sim) | **POST** /sims/{sim_id}/terminate | Terminate SIM.
[**terminate_subscription_container**](SimApi.md#terminate_subscription_container) | **POST** /sims/{sim_id}/profiles/{iccid}/subscribers/{imsi}/terminate | Terminate subscription container
[**unset_sim_expiry_time**](SimApi.md#unset_sim_expiry_time) | **POST** /sims/{sim_id}/unset_expiry_time | Delete expiry time of the SIM.
[**unset_sim_group**](SimApi.md#unset_sim_group) | **POST** /sims/{sim_id}/unset_group | Unset Group to SIM.
[**unset_sim_imei_lock**](SimApi.md#unset_sim_imei_lock) | **POST** /sims/{sim_id}/unset_imei_lock | Unset IMEI lock configuration for SIM.
[**update_sim_speed_class**](SimApi.md#update_sim_speed_class) | **POST** /sims/{sim_id}/update_speed_class | Update SIM speed class.


# **activate_sim**
> Sim activate_sim(sim_id)

Activate SIM.

Change status of specified SIM to active.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Activate SIM.
        api_response = api_instance.activate_sim(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->activate_sim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_subscription**
> SimProfile add_subscription(sim_id, iccid)

Adds a new subscription container to a SIM profile

This API is used to trigger the OTA update of a new subscription container to a SIM profile.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.sim_profile import SimProfile
from soracom_api.model.inline_object3 import InlineObject3
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | Id of the target SIM
    iccid = "iccid_example" # str | Iccid of the target profile
    inline_object3 = InlineObject3(
        enable=True,
        subscription="subscription_example",
        type="virtual",
    ) # InlineObject3 |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Adds a new subscription container to a SIM profile
        api_response = api_instance.add_subscription(sim_id, iccid)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->add_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Adds a new subscription container to a SIM profile
        api_response = api_instance.add_subscription(sim_id, iccid, inline_object3=inline_object3)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->add_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| Id of the target SIM |
 **iccid** | **str**| Iccid of the target profile |
 **inline_object3** | [**InlineObject3**](InlineObject3.md)|  | [optional]

### Return type

[**SimProfile**](SimProfile.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The updated SIM profile |  -  |
**404** | No such profile or sim found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attach_arc_sim_credentials**
> ArcCredentialAttachResponse attach_arc_sim_credentials(sim_id, arc_credential_attach_request)

(DEPRECATED) Attach the credentials for Arc to a SIM.

(DEPRECATED) Use this API to attach a set of credentials to a SIM. Please use `renewArcSimCredentials` API instead.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.arc_credential_attach_request import ArcCredentialAttachRequest
from soracom_api.model.arc_credential_attach_response import ArcCredentialAttachResponse
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    arc_credential_attach_request = ArcCredentialAttachRequest(
        arc_client_peer_public_key="arc_client_peer_public_key_example",
    ) # ArcCredentialAttachRequest | Arc credential attach request

    # example passing only required values which don't have defaults set
    try:
        # (DEPRECATED) Attach the credentials for Arc to a SIM.
        api_response = api_instance.attach_arc_sim_credentials(sim_id, arc_credential_attach_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->attach_arc_sim_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **arc_credential_attach_request** | [**ArcCredentialAttachRequest**](ArcCredentialAttachRequest.md)| Arc credential attach request |

### Return type

[**ArcCredentialAttachResponse**](ArcCredentialAttachResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Arc credential attach response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_subscription_container_download**
> SubscriptionContainerStatus cancel_subscription_container_download(sim_id, iccid, imsi)

Cancel subscription download to subscription container

Cancel the download of subscription before it gets downloaded to the SIM. The condition is that the status of the subscription is still `shipped`

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.subscription_container_status import SubscriptionContainerStatus
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target subscription container.
    iccid = "iccid_example" # str | ICCID of the target subscription container.
    imsi = "imsi_example" # str | IMSI of the target subscription container.

    # example passing only required values which don't have defaults set
    try:
        # Cancel subscription download to subscription container
        api_response = api_instance.cancel_subscription_container_download(sim_id, iccid, imsi)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->cancel_subscription_container_download: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target subscription container. |
 **iccid** | **str**| ICCID of the target subscription container. |
 **imsi** | **str**| IMSI of the target subscription container. |

### Return type

[**SubscriptionContainerStatus**](SubscriptionContainerStatus.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A schema listing subscription containers and containing a map of PLMN codes to subscription containers. |  -  |
**404** | No such SIM found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_arc_session**
> ArcSessionCreateResponse create_arc_session(sim_id)

Re-create an Arc session.

Use this API to re-activate a session for a virtual SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.arc_session_create_response import ArcSessionCreateResponse
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Re-create an Arc session.
        api_response = api_instance.create_arc_session(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->create_arc_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

### Return type

[**ArcSessionCreateResponse**](ArcSessionCreateResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Arc session created |  -  |
**400** | Arc credentials missing |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sim**
> Sim create_sim(create_sim_request)

Create a SIM.

Creates a SIM for example for use with Arc service.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.create_sim_request import CreateSimRequest
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
    api_instance = sim_api.SimApi(api_client)
    create_sim_request = CreateSimRequest(
        subscription="subscription_example",
        type="virtual",
    ) # CreateSimRequest | A SIM creation request

    # example passing only required values which don't have defaults set
    try:
        # Create a SIM.
        api_response = api_instance.create_sim(create_sim_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->create_sim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_sim_request** | [**CreateSimRequest**](CreateSimRequest.md)| A SIM creation request |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | SIM created. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_sim_packet_capture_session**
> PacketCaptureSession create_sim_packet_capture_session(sim_id, packet_capture_session_request)

Create Packet Capture Session

Create a packet capture session associated with the SIM

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.packet_capture_session_request import PacketCaptureSessionRequest
from soracom_api.model.packet_capture_session import PacketCaptureSession
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | The SIM ID for which a packet capture session is created
    packet_capture_session_request = PacketCaptureSessionRequest(
        duration=30,
        prefix="zBAMDTMv2D2ylmgd10Z3UB",
    ) # PacketCaptureSessionRequest | A packet capture session request

    # example passing only required values which don't have defaults set
    try:
        # Create Packet Capture Session
        api_response = api_instance.create_sim_packet_capture_session(sim_id, packet_capture_session_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->create_sim_packet_capture_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| The SIM ID for which a packet capture session is created |
 **packet_capture_session_request** | [**PacketCaptureSessionRequest**](PacketCaptureSessionRequest.md)| A packet capture session request |

### Return type

[**PacketCaptureSession**](PacketCaptureSession.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Created a new packet capture sessions associated with the SIM |  -  |
**404** | No such sim found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_sim**
> Sim deactivate_sim(sim_id)

Deactivate SIM.

Change status of specified SIM to inactive.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Deactivate SIM.
        api_response = api_instance.deactivate_sim(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->deactivate_sim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sim_packet_capture_session**
> PacketCaptureSession delete_sim_packet_capture_session(sim_id, session_id)

Delete Packet Capture Session

Delete a packet capture session associated with the SIM

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.packet_capture_session import PacketCaptureSession
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID
    session_id = "session_id_example" # str | Packet capture session ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Packet Capture Session
        api_response = api_instance.delete_sim_packet_capture_session(sim_id, session_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->delete_sim_packet_capture_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID |
 **session_id** | **str**| Packet capture session ID |

### Return type

[**PacketCaptureSession**](PacketCaptureSession.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted the packet capture session associated with the SIM |  -  |
**400** | Failed to delete the packet capture session associated with the SIM |  -  |
**404** | The packet capture session associated with the SIM was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sim_session**
> Sim delete_sim_session(sim_id)

Delete Session

Deletes session for the specified SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Delete Session
        api_response = api_instance.delete_sim_session(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->delete_sim_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sim_tag**
> delete_sim_tag(sim_id, tag_name)

Delete SIM tag.

Deletes a tag from the specified SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | Sim Id of the target SIM.
    tag_name = "tag_name_example" # str | Tag name to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().)

    # example passing only required values which don't have defaults set
    try:
        # Delete SIM tag.
        api_instance.delete_sim_tag(sim_id, tag_name)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->delete_sim_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| Sim Id of the target SIM. |
 **tag_name** | **str**| Tag name to be deleted. (This will be part of a URL path, so it needs to be percent-encoded. In JavaScript, specify the name after it has been encoded using encodeURIComponent().) |

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
**204** | Deletion of specified tag complete. |  -  |
**404** | The specified subscriber or the tag does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription_container_country_mapping_entry**
> SubscriptionContainerStatus delete_subscription_container_country_mapping_entry(sim_id, iccid, mcc)

Delete subscription container mapping entries

Delete subscription container country mapping entries

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.subscription_container_status import SubscriptionContainerStatus
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    iccid = "iccid_example" # str | Iccid of the target profile
    mcc = "mcc_example" # str | mobile country code

    # example passing only required values which don't have defaults set
    try:
        # Delete subscription container mapping entries
        api_response = api_instance.delete_subscription_container_country_mapping_entry(sim_id, iccid, mcc)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->delete_subscription_container_country_mapping_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **iccid** | **str**| Iccid of the target profile |
 **mcc** | **str**| mobile country code |

### Return type

[**SubscriptionContainerStatus**](SubscriptionContainerStatus.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A schema listing subscription containers and containing a map of PLMN codes to subscription containers. |  -  |
**400** | Missing parameter |  -  |
**404** | No such profile or sim found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_sim_termination**
> Sim disable_sim_termination(sim_id)

Disable termination of the SIM.

Disables termination of the specified SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Disable termination of the SIM.
        api_response = api_instance.disable_sim_termination(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->disable_sim_termination: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **downlink_ping_to_user_equipment**
> DownlinkPingResponse downlink_ping_to_user_equipment(sim_id, downlink_ping_request)

Send ping requests to a SIM.

Send ICMP ping requests to a SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.downlink_ping_response import DownlinkPingResponse
from soracom_api.model.downlink_ping_request import DownlinkPingRequest
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    downlink_ping_request = DownlinkPingRequest(
        number_of_ping_requests=1,
        timeout_seconds=1,
    ) # DownlinkPingRequest | ping options

    # example passing only required values which don't have defaults set
    try:
        # Send ping requests to a SIM.
        api_response = api_instance.downlink_ping_to_user_equipment(sim_id, downlink_ping_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->downlink_ping_to_user_equipment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **downlink_ping_request** | [**DownlinkPingRequest**](DownlinkPingRequest.md)| ping options |

### Return type

[**DownlinkPingResponse**](DownlinkPingResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of the ping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_sim_termination**
> Sim enable_sim_termination(sim_id)

Enable termination of the SIM.

Enables termination of specified SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Enable termination of the SIM.
        api_response = api_instance.enable_sim_termination(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->enable_sim_termination: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_subscription_container**
> SubscriptionContainerStatus enable_subscription_container(sim_id, iccid, container_id)

Enables a subscription container.

Causes the identified container to become the active one on the Sim.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.subscription_container_status import SubscriptionContainerStatus
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    iccid = "iccid_example" # str | Iccid of the target profile
    container_id = "containerId_example" # str | Identifier of the target container

    # example passing only required values which don't have defaults set
    try:
        # Enables a subscription container.
        api_response = api_instance.enable_subscription_container(sim_id, iccid, container_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->enable_subscription_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **iccid** | **str**| Iccid of the target profile |
 **container_id** | **str**| Identifier of the target container |

### Return type

[**SubscriptionContainerStatus**](SubscriptionContainerStatus.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A schema listing subscription containers and containing a map of PLMN codes to subscription containers. |  -  |
**404** | No such profile or sim found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_from_sim**
> [DataEntry] get_data_from_sim(sim_id)

Get data sent from a SIM.

Returns a list of data entries sent from a SIM that match certain criteria. If the total number of entries does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.data_entry import DataEntry
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | Sim Id of the target SIM.
    _from = 1 # int | Start time for the data entries search range (unixtime in milliseconds). (optional)
    to = 1 # int | End time for the data entries search range (unixtime in milliseconds). (optional)
    sort = "desc" # str | Sort order of the data entries. Either descending (latest data entry first) or ascending (oldest data entry first). (optional) if omitted the server will use the default value of "desc"
    limit = 1 # int | Maximum number of data entries to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The value of `time` in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get data sent from a SIM.
        api_response = api_instance.get_data_from_sim(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->get_data_from_sim: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get data sent from a SIM.
        api_response = api_instance.get_data_from_sim(sim_id, _from=_from, to=to, sort=sort, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->get_data_from_sim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| Sim Id of the target SIM. |
 **_from** | **int**| Start time for the data entries search range (unixtime in milliseconds). | [optional]
 **to** | **int**| End time for the data entries search range (unixtime in milliseconds). | [optional]
 **sort** | **str**| Sort order of the data entries. Either descending (latest data entry first) or ascending (oldest data entry first). | [optional] if omitted the server will use the default value of "desc"
 **limit** | **int**| Maximum number of data entries to retrieve. | [optional]
 **last_evaluated_key** | **str**| The value of &#x60;time&#x60; in the last log entry retrieved in the previous page. By specifying this parameter, you can continue to retrieve the list from the next page onward. | [optional]

### Return type

[**[DataEntry]**](DataEntry.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of data entries. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sim**
> Sim get_sim(sim_id)

Get a SIM identified by sim_id

Obtain a SIM record identified by the sim_id

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | Id of the target SIM

    # example passing only required values which don't have defaults set
    try:
        # Get a SIM identified by sim_id
        api_response = api_instance.get_sim(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->get_sim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| Id of the target SIM |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A SIM identified by sim_id |  -  |
**404** | No such SIM found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sim_packet_capture_session**
> PacketCaptureSession get_sim_packet_capture_session(sim_id, session_id)

Get Packet Capture Session

Get a packet capture sessions associated the SIM

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.packet_capture_session import PacketCaptureSession
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID
    session_id = "session_id_example" # str | Packet capture session ID

    # example passing only required values which don't have defaults set
    try:
        # Get Packet Capture Session
        api_response = api_instance.get_sim_packet_capture_session(sim_id, session_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->get_sim_packet_capture_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID |
 **session_id** | **str**| Packet capture session ID |

### Return type

[**PacketCaptureSession**](PacketCaptureSession.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The packet capture session associated with the SIM |  -  |
**404** | The packet capture session associated with the SIM was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sim_packet_capture_sessions**
> [PacketCaptureSession] list_sim_packet_capture_sessions(sim_id)

List Packet Capture Sessions

List packet capture sessions associated with the SIM

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.packet_capture_session import PacketCaptureSession
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID
    last_evaluated_key = "last_evaluated_key_example" # str | ID of the last packet capture session in the previous page (optional)
    limit = 10 # int | Max number of results in a response (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # List Packet Capture Sessions
        api_response = api_instance.list_sim_packet_capture_sessions(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->list_sim_packet_capture_sessions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Packet Capture Sessions
        api_response = api_instance.list_sim_packet_capture_sessions(sim_id, last_evaluated_key=last_evaluated_key, limit=limit)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->list_sim_packet_capture_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID |
 **last_evaluated_key** | **str**| ID of the last packet capture session in the previous page | [optional]
 **limit** | **int**| Max number of results in a response | [optional] if omitted the server will use the default value of 10

### Return type

[**[PacketCaptureSession]**](PacketCaptureSession.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of packet capture sessions associated with the SIM |  -  |
**404** | No such sim found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sim_session_events**
> [SessionEvent] list_sim_session_events(sim_id)

List Session Events.

Returns the history of session creation, change, and deletion events occurred on the target SIM in the last 14 days. If the total number of events does not fit in one page, a URL for accessing the next page is returned in the `Link` header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.session_event import SessionEvent
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    _from = 1 # int | Start time for the events search range (unixtime). (optional)
    to = 1 # int | End time for the events search range (unixtime). (optional)
    limit = 1 # int | Maximum number of events to retrieve. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The time stamp of the last event retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next event onward. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Session Events.
        api_response = api_instance.list_sim_session_events(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->list_sim_session_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Session Events.
        api_response = api_instance.list_sim_session_events(sim_id, _from=_from, to=to, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->list_sim_session_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **_from** | **int**| Start time for the events search range (unixtime). | [optional]
 **to** | **int**| End time for the events search range (unixtime). | [optional]
 **limit** | **int**| Maximum number of events to retrieve. | [optional]
 **last_evaluated_key** | **str**| The time stamp of the last event retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next event onward. | [optional]

### Return type

[**[SessionEvent]**](SessionEvent.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of session events |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sims**
> [Sim] list_sims()

List SIMs.

Returns a list of SIMs that match certain criteria. If the total number of SIMs does not fit in one page, a URL for accessing the next page is returned in the 'Link' header of the response.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    limit = 1 # int | Maximum number of SIMs to retrieve. Setting a limit does not guarantee the number of sims returned in the response (i.e. the response may contain fewer sims than the specified limit). (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The ID of the last SIM retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next SIM onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List SIMs.
        api_response = api_instance.list_sims(limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->list_sims: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of SIMs to retrieve. Setting a limit does not guarantee the number of sims returned in the response (i.e. the response may contain fewer sims than the specified limit). | [optional]
 **last_evaluated_key** | **str**| The ID of the last SIM retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next SIM onward. | [optional]

### Return type

[**[Sim]**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of SIMs. |  -  |
**404** | No such SIM found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_subscription_containers**
> SubscriptionContainerStatus list_subscription_containers(sim_id, iccid)

Get subscription container status.

Returns a schema listing subscription containers and containing a map of PLMN codes to subscription containers

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.subscription_container_status import SubscriptionContainerStatus
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | Sim Id of the target SIM.
    iccid = "iccid_example" # str | Iccid of the target profile

    # example passing only required values which don't have defaults set
    try:
        # Get subscription container status.
        api_response = api_instance.list_subscription_containers(sim_id, iccid)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->list_subscription_containers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| Sim Id of the target SIM. |
 **iccid** | **str**| Iccid of the target profile |

### Return type

[**SubscriptionContainerStatus**](SubscriptionContainerStatus.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A schema listing subscription containers and containing a map of PLMN codes to subscription containers. |  -  |
**400** | Missing parameter |  -  |
**404** | No such profile or sim found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_sim_tags**
> Sim put_sim_tags(sim_id, tag_update_request)

Bulk insert or update SIM tags.

Inserts/updates tags for the specified SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.tag_update_request import TagUpdateRequest
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    tag_update_request = [
        TagUpdateRequest(
            tag_name="tag_name_example",
            tag_value="tag_value_example",
        ),
    ] # [TagUpdateRequest] | Array of tags to be inserted/updated.

    # example passing only required values which don't have defaults set
    try:
        # Bulk insert or update SIM tags.
        api_response = api_instance.put_sim_tags(sim_id, tag_update_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->put_sim_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **tag_update_request** | [**[TagUpdateRequest]**](TagUpdateRequest.md)| Array of tags to be inserted/updated. |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_subscription_container_country_mapping_entries**
> SubscriptionContainerStatus put_subscription_container_country_mapping_entries(sim_id, iccid, mapping_entries)

Updates subscription container country mapping entries.

Inserts/updates Country (and optionally network) to subscription container mapping entries in the mapping table.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.mapping_entries import MappingEntries
from soracom_api.model.subscription_container_status import SubscriptionContainerStatus
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    iccid = "iccid_example" # str | Iccid of the target profile
    mapping_entries = MappingEntries(
        mapping_entries=[
            GlobalSimAppletPLMNRecord(
                container_id=1,
                mcc="mcc_example",
                mnc="mnc_example",
            ),
        ],
    ) # MappingEntries | collection of country (and optionally network) to subscription container mapping entries

    # example passing only required values which don't have defaults set
    try:
        # Updates subscription container country mapping entries.
        api_response = api_instance.put_subscription_container_country_mapping_entries(sim_id, iccid, mapping_entries)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->put_subscription_container_country_mapping_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **iccid** | **str**| Iccid of the target profile |
 **mapping_entries** | [**MappingEntries**](MappingEntries.md)| collection of country (and optionally network) to subscription container mapping entries |

### Return type

[**SubscriptionContainerStatus**](SubscriptionContainerStatus.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A schema listing subscription containers and containing a map of PLMN codes to subscription containers. |  -  |
**400** | Missing parameter |  -  |
**404** | No such profile or sim found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_sim**
> Sim register_sim(sim_id, register_sim_request)

Register SIM.

Registers a SIM to an operator.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.register_sim_request import RegisterSimRequest
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    register_sim_request = RegisterSimRequest(
        group_id="group_id_example",
        registration_secret="registration_secret_example",
        tags=[
            TagUpdateRequest(
                tag_name="tag_name_example",
                tag_value="tag_value_example",
            ),
        ],
    ) # RegisterSimRequest | A SIM registration request

    # example passing only required values which don't have defaults set
    try:
        # Register SIM.
        api_response = api_instance.register_sim(sim_id, register_sim_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->register_sim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **register_sim_request** | [**RegisterSimRequest**](RegisterSimRequest.md)| A SIM registration request |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sim registration complete. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_arc_sim_credentials**
> remove_arc_sim_credentials(sim_id)

(DEPRECATED) Remove the credentials for Arc from a SIM.

(DEPRECATED) Use this API to remove the set of credentials for Arc from the specified SIM. Please do not use this API.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # (DEPRECATED) Remove the credentials for Arc from a SIM.
        api_instance.remove_arc_sim_credentials(sim_id)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->remove_arc_sim_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

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
**204** | The credentials for Arc have been removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **renew_arc_sim_credentials**
> ArcCredentialRenewResponse renew_arc_sim_credentials(sim_id, arc_credential_renew_request)

Renew the credentials for Arc to a SIM.

Use this API to attach a set of credentials to a SIM and re-initialize a session at once.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.arc_credential_renew_request import ArcCredentialRenewRequest
from soracom_api.model.arc_credential_renew_response import ArcCredentialRenewResponse
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    arc_credential_renew_request = ArcCredentialRenewRequest(
        arc_client_peer_public_key="arc_client_peer_public_key_example",
    ) # ArcCredentialRenewRequest | Arc credential attach request

    # example passing only required values which don't have defaults set
    try:
        # Renew the credentials for Arc to a SIM.
        api_response = api_instance.renew_arc_sim_credentials(sim_id, arc_credential_renew_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->renew_arc_sim_credentials: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **arc_credential_renew_request** | [**ArcCredentialRenewRequest**](ArcCredentialRenewRequest.md)| Arc credential attach request |

### Return type

[**ArcCredentialRenewResponse**](ArcCredentialRenewResponse.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Arc credential attach response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_sim_local_info**
> Subscriber report_sim_local_info(sim_id)

Triggers SIM to report SIM local info.

Triggers SIM to report SIM local info.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Triggers SIM to report SIM local info.
        api_response = api_instance.report_sim_local_info(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->report_sim_local_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

### Return type

[**Subscriber**](Subscriber.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The local info reporting has successfully been triggered. The subscriber information is asynchronously updated when the SIM reports the information back. |  -  |
**400** | The specified SIM active subscriber does not support local info reporting feature. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms_to_sim**
> SmsForwardingReport send_sms_to_sim(sim_id, sms_forwarding_request)

Send SMS to SIM

Send SMS to the specified SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.sms_forwarding_request import SmsForwardingRequest
from soracom_api.model.sms_forwarding_report import SmsForwardingReport
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    sms_forwarding_request = SmsForwardingRequest(
        encoding_type=2,
        payload="payload_example",
    ) # SmsForwardingRequest | SMS forwarding request that contains message body and its encoding type.

    # example passing only required values which don't have defaults set
    try:
        # Send SMS to SIM
        api_response = api_instance.send_sms_to_sim(sim_id, sms_forwarding_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->send_sms_to_sim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **sms_forwarding_request** | [**SmsForwardingRequest**](SmsForwardingRequest.md)| SMS forwarding request that contains message body and its encoding type. |

### Return type

[**SmsForwardingReport**](SmsForwardingReport.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | SMS forwarding report containing message ID. |  -  |
**400** | The specified SIM does not support SMS API. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_sim_expiry_time**
> Sim set_sim_expiry_time(sim_id, expiry_time)

Update expiry time of SIM.

Updates expiry time of the specified SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.expiry_time import ExpiryTime
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    expiry_time = ExpiryTime(
        expiry_action="doNothing",
        expiry_time=1,
    ) # ExpiryTime | Expiry time after the update (unixtime: in milliseconds).

    # example passing only required values which don't have defaults set
    try:
        # Update expiry time of SIM.
        api_response = api_instance.set_sim_expiry_time(sim_id, expiry_time)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->set_sim_expiry_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **expiry_time** | [**ExpiryTime**](ExpiryTime.md)| Expiry time after the update (unixtime: in milliseconds). |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_sim_group**
> Sim set_sim_group(sim_id, set_group_request)

Set Group id of a SIM.

Sets or overwrites a group for the specified SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.set_group_request import SetGroupRequest
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    set_group_request = SetGroupRequest(
        group_id="group_id_example",
        tags=TagSet(
            key="key_example",
        ),
    ) # SetGroupRequest | Group (may include ID only).

    # example passing only required values which don't have defaults set
    try:
        # Set Group id of a SIM.
        api_response = api_instance.set_sim_group(sim_id, set_group_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->set_sim_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **set_group_request** | [**SetGroupRequest**](SetGroupRequest.md)| Group (may include ID only). |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_sim_imei_lock**
> Sim set_sim_imei_lock(sim_id)

Set IMEI lock configuration for the SIM.

Set IMEI that the SIM should be locked to.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.set_imei_lock_request import SetImeiLockRequest
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    set_imei_lock_request = SetImeiLockRequest(
        imei="imei_example",
    ) # SetImeiLockRequest | IMEI lock configuration for the SIM. (IMEI can be left blank for locking to the current IMEI of an online SIM.) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Set IMEI lock configuration for the SIM.
        api_response = api_instance.set_sim_imei_lock(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->set_sim_imei_lock: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Set IMEI lock configuration for the SIM.
        api_response = api_instance.set_sim_imei_lock(sim_id, set_imei_lock_request=set_imei_lock_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->set_sim_imei_lock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **set_imei_lock_request** | [**SetImeiLockRequest**](SetImeiLockRequest.md)| IMEI lock configuration for the SIM. (IMEI can be left blank for locking to the current IMEI of an online SIM.) | [optional]

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**400** | Invalid IMEI string or SIM is offline and IMEI not specified. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_sim_to_standby**
> Sim set_sim_to_standby(sim_id)

Set SIM to standby mode.

Set the specified SIM to standby mode.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Set SIM to standby mode.
        api_response = api_instance.set_sim_to_standby(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->set_sim_to_standby: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**400** | The specified SIM does not support standby mode. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_sim_packet_capture_session**
> PacketCaptureSession stop_sim_packet_capture_session(sim_id, session_id)

Stop SIM Packet Capture Session

Stop a packet capture session associated with the SIM

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.packet_capture_session import PacketCaptureSession
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID
    session_id = "session_id_example" # str | Packet capture session ID

    # example passing only required values which don't have defaults set
    try:
        # Stop SIM Packet Capture Session
        api_response = api_instance.stop_sim_packet_capture_session(sim_id, session_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->stop_sim_packet_capture_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID |
 **session_id** | **str**| Packet capture session ID |

### Return type

[**PacketCaptureSession**](PacketCaptureSession.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stopped packet capture session associated with the SIM |  -  |
**400** | The packet capture session can be stopped only when its status is CAPTURING |  -  |
**404** | The packet capture session associated with the SIM was not found |  -  |
**500** | The packet capture session could not be stopped |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suspend_sim**
> Sim suspend_sim(sim_id)

Suspend SIM.

Suspends the specified SIM

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Suspend SIM.
        api_response = api_instance.suspend_sim(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->suspend_sim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_sim**
> Sim terminate_sim(sim_id)

Terminate SIM.

Terminates the specified SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Terminate SIM.
        api_response = api_instance.terminate_sim(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->terminate_sim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_subscription_container**
> terminate_subscription_container(sim_id, iccid, imsi)

Terminate subscription container

Terminate subscription container. Currently this API supports only for virtual subscribers for SORACOM Arc service.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target subscription container.
    iccid = "iccid_example" # str | ICCID of the target subscription container.
    imsi = "imsi_example" # str | IMSI of the target subscription container.

    # example passing only required values which don't have defaults set
    try:
        # Terminate subscription container
        api_instance.terminate_subscription_container(sim_id, iccid, imsi)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->terminate_subscription_container: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target subscription container. |
 **iccid** | **str**| ICCID of the target subscription container. |
 **imsi** | **str**| IMSI of the target subscription container. |

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
**204** | The subscription container has been terminated. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_sim_expiry_time**
> unset_sim_expiry_time(sim_id)

Delete expiry time of the SIM.

Deletes expiry time of specified SIM and changes it to indefinite.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Delete expiry time of the SIM.
        api_instance.unset_sim_expiry_time(sim_id)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->unset_sim_expiry_time: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

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
**204** | Change of specified SIM&#39;s expiry time to indefinite complete. |  -  |
**404** | The specified SIM does not exist or the SIM does not have an expiry time. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_sim_group**
> Sim unset_sim_group(sim_id)

Unset Group to SIM.

Removes the group configuration from the specified SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Unset Group to SIM.
        api_response = api_instance.unset_sim_group(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->unset_sim_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist or the SIM does not belong to a group. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_sim_imei_lock**
> Sim unset_sim_imei_lock(sim_id)

Unset IMEI lock configuration for SIM.

Remove any existing IMEI lock configuration for the SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | Sim Id of the target SIM.

    # example passing only required values which don't have defaults set
    try:
        # Unset IMEI lock configuration for SIM.
        api_response = api_instance.unset_sim_imei_lock(sim_id)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->unset_sim_imei_lock: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| Sim Id of the target SIM. |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sim_speed_class**
> Sim update_sim_speed_class(sim_id, update_speed_class_request)

Update SIM speed class.

Changes the speed class of the specified SIM.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import soracom_api
from soracom_api.api import sim_api
from soracom_api.model.update_speed_class_request import UpdateSpeedClassRequest
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
    api_instance = sim_api.SimApi(api_client)
    sim_id = "sim_id_example" # str | SIM ID of the target SIM.
    update_speed_class_request = UpdateSpeedClassRequest(
        speed_class="s1.minimum",
    ) # UpdateSpeedClassRequest | speed_class

    # example passing only required values which don't have defaults set
    try:
        # Update SIM speed class.
        api_response = api_instance.update_sim_speed_class(sim_id, update_speed_class_request)
        pprint(api_response)
    except soracom_api.ApiException as e:
        print("Exception when calling SimApi->update_sim_speed_class: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sim_id** | **str**| SIM ID of the target SIM. |
 **update_speed_class_request** | [**UpdateSpeedClassRequest**](UpdateSpeedClassRequest.md)| speed_class |

### Return type

[**Sim**](Sim.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The SIM&#39;s detailed information after the update. |  -  |
**404** | The specified SIM does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

