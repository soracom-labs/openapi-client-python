# api.VirtualPrivateGatewayApi

All URIs are relative to *https://api.soracom.io/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_gate**](VirtualPrivateGatewayApi.md#close_gate) | **POST** /virtual_private_gateways/{vpg_id}/gate/close | Close SORACOM Gate.
[**create_mirroring_peer**](VirtualPrivateGatewayApi.md#create_mirroring_peer) | **POST** /virtual_private_gateways/{vpg_id}/junction/mirroring/peers | Add node in the list of Junction mirroring peers
[**create_packet_capture_session**](VirtualPrivateGatewayApi.md#create_packet_capture_session) | **POST** /virtual_private_gateways/{vpg_id}/packet_capture_sessions | Create Packet Capture Session
[**create_virtual_private_gateway**](VirtualPrivateGatewayApi.md#create_virtual_private_gateway) | **POST** /virtual_private_gateways | Create Virtual Private Gateway.
[**create_vpc_peering_connection**](VirtualPrivateGatewayApi.md#create_vpc_peering_connection) | **POST** /virtual_private_gateways/{vpg_id}/vpc_peering_connections | Create VPC Peering Connection
[**delete_mirroring_peer**](VirtualPrivateGatewayApi.md#delete_mirroring_peer) | **DELETE** /virtual_private_gateways/{vpg_id}/junction/mirroring/peers/{ipaddr} | Remove peer from the list of Junction mirroring peers
[**delete_packet_capture_session**](VirtualPrivateGatewayApi.md#delete_packet_capture_session) | **DELETE** /virtual_private_gateways/{vpg_id}/packet_capture_sessions/{session_id} | Delete Packet Capture Session
[**delete_virtual_private_gateway_ip_address_map_entry**](VirtualPrivateGatewayApi.md#delete_virtual_private_gateway_ip_address_map_entry) | **DELETE** /virtual_private_gateways/{vpg_id}/ip_address_map/{key} | Delete VPG IP address map entry
[**delete_vpc_peering_connection**](VirtualPrivateGatewayApi.md#delete_vpc_peering_connection) | **DELETE** /virtual_private_gateways/{vpg_id}/vpc_peering_connections/{pcx_id} | Delete VPC Peering Connection.
[**get_packet_capture_session**](VirtualPrivateGatewayApi.md#get_packet_capture_session) | **GET** /virtual_private_gateways/{vpg_id}/packet_capture_sessions/{session_id} | Get Packet Capture Session
[**get_virtual_private_gateway**](VirtualPrivateGatewayApi.md#get_virtual_private_gateway) | **GET** /virtual_private_gateways/{vpg_id} | Get Virtual Private Gateway.
[**list_gate_peers**](VirtualPrivateGatewayApi.md#list_gate_peers) | **GET** /virtual_private_gateways/{vpg_id}/gate/peers | List VPG Gate peers
[**list_packet_capture_sessions**](VirtualPrivateGatewayApi.md#list_packet_capture_sessions) | **GET** /virtual_private_gateways/{vpg_id}/packet_capture_sessions | List Packet Capture Sessions
[**list_virtual_private_gateway_ip_address_map_entries**](VirtualPrivateGatewayApi.md#list_virtual_private_gateway_ip_address_map_entries) | **GET** /virtual_private_gateways/{vpg_id}/ip_address_map | List VPG IP address map entries
[**list_virtual_private_gateways**](VirtualPrivateGatewayApi.md#list_virtual_private_gateways) | **GET** /virtual_private_gateways | List Virtual Private Gateways.
[**open_gate**](VirtualPrivateGatewayApi.md#open_gate) | **POST** /virtual_private_gateways/{vpg_id}/gate/open | Open SORACOM Gate.
[**put_virtual_private_gateway_ip_address_map_entry**](VirtualPrivateGatewayApi.md#put_virtual_private_gateway_ip_address_map_entry) | **POST** /virtual_private_gateways/{vpg_id}/ip_address_map | Put an entry in VPG IP address map
[**register_gate_peer**](VirtualPrivateGatewayApi.md#register_gate_peer) | **POST** /virtual_private_gateways/{vpg_id}/gate/peers | Register VPG Gate peer
[**set_inspection_configuration**](VirtualPrivateGatewayApi.md#set_inspection_configuration) | **POST** /virtual_private_gateways/{vpg_id}/junction/set_inspection | Set configuration for Junction inspection feature
[**set_redirection_configuration**](VirtualPrivateGatewayApi.md#set_redirection_configuration) | **POST** /virtual_private_gateways/{vpg_id}/junction/set_redirection | Set configuration for Junction redirection feature
[**set_routing_filter**](VirtualPrivateGatewayApi.md#set_routing_filter) | **POST** /virtual_private_gateways/{vpg_id}/set_routing_filter | Sets Virtual Private Gateway outbound routing filter.
[**stop_packet_capture_session**](VirtualPrivateGatewayApi.md#stop_packet_capture_session) | **POST** /virtual_private_gateways/{vpg_id}/packet_capture_sessions/{session_id}/stop | Stop Packet Capture Session
[**terminate_virtual_private_gateway**](VirtualPrivateGatewayApi.md#terminate_virtual_private_gateway) | **POST** /virtual_private_gateways/{vpg_id}/terminate | Terminate Virtual Private Gateway.
[**unregister_gate_peer**](VirtualPrivateGatewayApi.md#unregister_gate_peer) | **DELETE** /virtual_private_gateways/{vpg_id}/gate/peers/{outer_ip_address} | Unregister VPG gate peer
[**unset_inspection_configuration**](VirtualPrivateGatewayApi.md#unset_inspection_configuration) | **POST** /virtual_private_gateways/{vpg_id}/junction/unset_inspection | Unset configuration for Junction inspection feature
[**unset_redirection_configuration**](VirtualPrivateGatewayApi.md#unset_redirection_configuration) | **POST** /virtual_private_gateways/{vpg_id}/junction/unset_redirection | Unset configuration for Junction redirection feature
[**update_mirroring_peer**](VirtualPrivateGatewayApi.md#update_mirroring_peer) | **PUT** /virtual_private_gateways/{vpg_id}/junction/mirroring/peers/{ipaddr} | Update a Junction mirroring peer


# **close_gate**
> close_gate(vpg_id)

Close SORACOM Gate.

Close SORACOM Gate on the specified VPG.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.

    # example passing only required values which don't have defaults set
    try:
        # Close SORACOM Gate.
        api_instance.close_gate(vpg_id)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->close_gate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |

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
**200** | SORACOM Gate is successfully closed on the VPG. |  -  |
**400** | Client side error. |  -  |
**404** | The specified VPG does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mirroring_peer**
> create_mirroring_peer(vpg_id, junction_mirroring_peer)

Add node in the list of Junction mirroring peers

Add node in the list of Junction mirroring peers

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.junction_mirroring_peer import JunctionMirroringPeer
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID
    junction_mirroring_peer = JunctionMirroringPeer(
        description="description_example",
        enabled=False,
        ip_address="ip_address_example",
        protocol="gre",
    ) # JunctionMirroringPeer | Mirroring peer

    # example passing only required values which don't have defaults set
    try:
        # Add node in the list of Junction mirroring peers
        api_instance.create_mirroring_peer(vpg_id, junction_mirroring_peer)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->create_mirroring_peer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |
 **junction_mirroring_peer** | [**JunctionMirroringPeer**](JunctionMirroringPeer.md)| Mirroring peer |

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
**201** | Mirroring peer added/updated |  -  |
**404** | No such VPG found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_packet_capture_session**
> PacketCaptureSession create_packet_capture_session(vpg_id, packet_capture_session_request)

Create Packet Capture Session

Create a packet capture sessions associated the VPG

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.packet_capture_session_request import PacketCaptureSessionRequest
from api.model.packet_capture_session import PacketCaptureSession
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID
    packet_capture_session_request = PacketCaptureSessionRequest(
        duration=30,
        prefix="zBAMDTMv2D2ylmgd10Z3UB",
    ) # PacketCaptureSessionRequest | A packet capture session request

    # example passing only required values which don't have defaults set
    try:
        # Create Packet Capture Session
        api_response = api_instance.create_packet_capture_session(vpg_id, packet_capture_session_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->create_packet_capture_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |
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
**200** | Created a new packet capture sessions associated with the VPG |  -  |
**400** | Failed to create a packet capture sessions associated with the VPG |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_private_gateway**
> VirtualPrivateGateway create_virtual_private_gateway(create_virtual_private_gateway_request)

Create Virtual Private Gateway.

Create new VPG.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.create_virtual_private_gateway_request import CreateVirtualPrivateGatewayRequest
from api.model.virtual_private_gateway import VirtualPrivateGateway
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    create_virtual_private_gateway_request = CreateVirtualPrivateGatewayRequest(
        device_subnet_cidr_range="10.128.0.0/9",
        type=14,
        use_internet_gateway=True,
    ) # CreateVirtualPrivateGatewayRequest | Request containing information for the new VPG to be created.

    # example passing only required values which don't have defaults set
    try:
        # Create Virtual Private Gateway.
        api_response = api_instance.create_virtual_private_gateway(create_virtual_private_gateway_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->create_virtual_private_gateway: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_virtual_private_gateway_request** | [**CreateVirtualPrivateGatewayRequest**](CreateVirtualPrivateGatewayRequest.md)| Request containing information for the new VPG to be created. |

### Return type

[**VirtualPrivateGateway**](VirtualPrivateGateway.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_vpc_peering_connection**
> CreateVpcPeeringConnectionRequest create_vpc_peering_connection(vpg_id, create_vpc_peering_connection_request)

Create VPC Peering Connection

Creates a VPC peering connection for the specified VPG.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.create_vpc_peering_connection_request import CreateVpcPeeringConnectionRequest
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.
    create_vpc_peering_connection_request = CreateVpcPeeringConnectionRequest(
        destination_cidr_block="destination_cidr_block_example",
        peer_owner_id="peer_owner_id_example",
        peer_region="peer_region_example",
        peer_vpc_id="peer_vpc_id_example",
    ) # CreateVpcPeeringConnectionRequest | VPC peering connection to be created.

    # example passing only required values which don't have defaults set
    try:
        # Create VPC Peering Connection
        api_response = api_instance.create_vpc_peering_connection(vpg_id, create_vpc_peering_connection_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->create_vpc_peering_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |
 **create_vpc_peering_connection_request** | [**CreateVpcPeeringConnectionRequest**](CreateVpcPeeringConnectionRequest.md)| VPC peering connection to be created. |

### Return type

[**CreateVpcPeeringConnectionRequest**](CreateVpcPeeringConnectionRequest.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created VPC peering connection. |  -  |
**404** | The specified VPC peering connection does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mirroring_peer**
> delete_mirroring_peer(vpg_id, ipaddr)

Remove peer from the list of Junction mirroring peers

Remove peer from the list of Junction mirroring peers

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID
    ipaddr = "ipaddr_example" # str | IP address of mirroring peer

    # example passing only required values which don't have defaults set
    try:
        # Remove peer from the list of Junction mirroring peers
        api_instance.delete_mirroring_peer(vpg_id, ipaddr)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->delete_mirroring_peer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |
 **ipaddr** | **str**| IP address of mirroring peer |

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
**204** | Mirroring peer removed |  -  |
**404** | No such VPG found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_packet_capture_session**
> PacketCaptureSession delete_packet_capture_session(vpg_id, session_id)

Delete Packet Capture Session

Delete a packet capture sessions associated the VPG

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.packet_capture_session import PacketCaptureSession
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID
    session_id = "session_id_example" # str | Packet capture session ID

    # example passing only required values which don't have defaults set
    try:
        # Delete Packet Capture Session
        api_response = api_instance.delete_packet_capture_session(vpg_id, session_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->delete_packet_capture_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |
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
**200** | Deleted the packet capture sessions associated with the VPG |  -  |
**400** | Failed to delete the packet capture sessions associated with the VPG was not found |  -  |
**404** | The packet capture sessions associated with the VPG was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_private_gateway_ip_address_map_entry**
> IpAddressMapEntry delete_virtual_private_gateway_ip_address_map_entry(vpg_id, key)

Delete VPG IP address map entry

Deletes an entry in VPG IP address map.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.ip_address_map_entry import IpAddressMapEntry
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.
    key = "key_example" # str | Target key to remove.

    # example passing only required values which don't have defaults set
    try:
        # Delete VPG IP address map entry
        api_response = api_instance.delete_virtual_private_gateway_ip_address_map_entry(vpg_id, key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->delete_virtual_private_gateway_ip_address_map_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |
 **key** | **str**| Target key to remove. |

### Return type

[**IpAddressMapEntry**](IpAddressMapEntry.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted the entry from the VPG IP address map. |  -  |
**400** | Error in the request. |  -  |
**404** | The specified VPG or node does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_vpc_peering_connection**
> delete_vpc_peering_connection(vpg_id, pcx_id)

Delete VPC Peering Connection.

Deletes the specified VPC peering connection.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.
    pcx_id = "pcx_id_example" # str | VPC peering connection ID to be deleted.

    # example passing only required values which don't have defaults set
    try:
        # Delete VPC Peering Connection.
        api_instance.delete_vpc_peering_connection(vpg_id, pcx_id)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->delete_vpc_peering_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |
 **pcx_id** | **str**| VPC peering connection ID to be deleted. |

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
**204** | Deletion of specified VPC peering connection complete. |  -  |
**404** | The specified VPC peering connection does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_packet_capture_session**
> PacketCaptureSession get_packet_capture_session(vpg_id, session_id)

Get Packet Capture Session

Get a packet capture sessions associated the VPG

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.packet_capture_session import PacketCaptureSession
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID
    session_id = "session_id_example" # str | Packet capture session ID

    # example passing only required values which don't have defaults set
    try:
        # Get Packet Capture Session
        api_response = api_instance.get_packet_capture_session(vpg_id, session_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->get_packet_capture_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |
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
**200** | The packet capture sessions associated with the VPG |  -  |
**404** | The packet capture sessions associated with the VPG was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_private_gateway**
> get_virtual_private_gateway(vpg_id)

Get Virtual Private Gateway.

Retrieves information about the specified VPG.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.

    # example passing only required values which don't have defaults set
    try:
        # Get Virtual Private Gateway.
        api_instance.get_virtual_private_gateway(vpg_id)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->get_virtual_private_gateway: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |

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
**200** | The specified VPG. |  -  |
**404** | The specified VPG does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_gate_peers**
> [GatePeer] list_gate_peers(vpg_id)

List VPG Gate peers

List Gate peers registered in the Virtual Private Gateway

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.gate_peer import GatePeer
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.

    # example passing only required values which don't have defaults set
    try:
        # List VPG Gate peers
        api_response = api_instance.list_gate_peers(vpg_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->list_gate_peers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |

### Return type

[**[GatePeer]**](GatePeer.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of peers registered in the VPG. |  -  |
**400** | Client side error in the request. |  -  |
**404** | The specified VPG does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_packet_capture_sessions**
> [PacketCaptureSession] list_packet_capture_sessions(vpg_id)

List Packet Capture Sessions

List packet capture sessions associated with the VPG

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.packet_capture_session import PacketCaptureSession
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID
    last_evaluated_key = "null" # str | ID of the last group in the previous page (optional) if omitted the server will use the default value of "null"
    limit = 10 # int | Max number of results in a response (optional) if omitted the server will use the default value of 10

    # example passing only required values which don't have defaults set
    try:
        # List Packet Capture Sessions
        api_response = api_instance.list_packet_capture_sessions(vpg_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->list_packet_capture_sessions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Packet Capture Sessions
        api_response = api_instance.list_packet_capture_sessions(vpg_id, last_evaluated_key=last_evaluated_key, limit=limit)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->list_packet_capture_sessions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |
 **last_evaluated_key** | **str**| ID of the last group in the previous page | [optional] if omitted the server will use the default value of "null"
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
**200** | List of packet capture sessions associated with the VPG |  -  |
**400** | Failed to list packet capture sessions associated with the VPG |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_private_gateway_ip_address_map_entries**
> [IpAddressMapEntry] list_virtual_private_gateway_ip_address_map_entries(vpg_id)

List VPG IP address map entries

Describes the list of IP address map entries in the Virtual Private Gateway

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.ip_address_map_entry import IpAddressMapEntry
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.

    # example passing only required values which don't have defaults set
    try:
        # List VPG IP address map entries
        api_response = api_instance.list_virtual_private_gateway_ip_address_map_entries(vpg_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->list_virtual_private_gateway_ip_address_map_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |

### Return type

[**[IpAddressMapEntry]**](IpAddressMapEntry.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully fetched the list of IP address map entries. |  -  |
**400** | Error in the request. |  -  |
**404** | The specified VPG or node does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_virtual_private_gateways**
> [VirtualPrivateGateway] list_virtual_private_gateways()

List Virtual Private Gateways.

Returns a list of VPGs.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.virtual_private_gateway import VirtualPrivateGateway
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    tag_name = "tag_name_example" # str | Tag name of the VPG. Filters through all VPGs that exactly match the tag name. When tag_name is specified, tag_value is required. (optional)
    tag_value = "tag_value_example" # str | Tag value of the VPGs. (optional)
    tag_value_match_mode = "exact" # str | Tag match mode. (optional) if omitted the server will use the default value of "exact"
    limit = 1 # int | Maximum number of results per response page. (optional)
    last_evaluated_key = "last_evaluated_key_example" # str | The last group ID retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next VPG onward. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Virtual Private Gateways.
        api_response = api_instance.list_virtual_private_gateways(tag_name=tag_name, tag_value=tag_value, tag_value_match_mode=tag_value_match_mode, limit=limit, last_evaluated_key=last_evaluated_key)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->list_virtual_private_gateways: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_name** | **str**| Tag name of the VPG. Filters through all VPGs that exactly match the tag name. When tag_name is specified, tag_value is required. | [optional]
 **tag_value** | **str**| Tag value of the VPGs. | [optional]
 **tag_value_match_mode** | **str**| Tag match mode. | [optional] if omitted the server will use the default value of "exact"
 **limit** | **int**| Maximum number of results per response page. | [optional]
 **last_evaluated_key** | **str**| The last group ID retrieved on the current page. By specifying this parameter, you can continue to retrieve the list from the next VPG onward. | [optional]

### Return type

[**[VirtualPrivateGateway]**](VirtualPrivateGateway.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of VPGs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_gate**
> open_gate(vpg_id)

Open SORACOM Gate.

Open SORACOM Gate on the specified VPG.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.open_gate_request import OpenGateRequest
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.
    open_gate_request = OpenGateRequest(
        privacy_separator_enabled=False,
        vxlan_id=10,
    ) # OpenGateRequest | Optional configuration parameters for Gate. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Open SORACOM Gate.
        api_instance.open_gate(vpg_id)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->open_gate: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Open SORACOM Gate.
        api_instance.open_gate(vpg_id, open_gate_request=open_gate_request)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->open_gate: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |
 **open_gate_request** | [**OpenGateRequest**](OpenGateRequest.md)| Optional configuration parameters for Gate. | [optional]

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
**200** | SORACOM Gate is successfully opened on the VPG. |  -  |
**400** | Client side error. |  -  |
**404** | The specified VPG does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_virtual_private_gateway_ip_address_map_entry**
> IpAddressMapEntry put_virtual_private_gateway_ip_address_map_entry(vpg_id, put_ip_address_map_entry_request)

Put an entry in VPG IP address map

Puts an entry in VPG IP address map.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.put_ip_address_map_entry_request import PutIpAddressMapEntryRequest
from api.model.ip_address_map_entry import IpAddressMapEntry
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.
    put_ip_address_map_entry_request = PutIpAddressMapEntryRequest(
        ip_address="ip_address_example",
        key="key_example",
    ) # PutIpAddressMapEntryRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Put an entry in VPG IP address map
        api_response = api_instance.put_virtual_private_gateway_ip_address_map_entry(vpg_id, put_ip_address_map_entry_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->put_virtual_private_gateway_ip_address_map_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |
 **put_ip_address_map_entry_request** | [**PutIpAddressMapEntryRequest**](PutIpAddressMapEntryRequest.md)|  |

### Return type

[**IpAddressMapEntry**](IpAddressMapEntry.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully put an entry for the specified key and IP address. |  -  |
**400** | Error in the request. |  -  |
**404** | The specified VPG or node does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_gate_peer**
> GatePeer register_gate_peer(vpg_id, register_gate_peer_request)

Register VPG Gate peer

Register a host as a gate peer in the Virtual Private Gateway

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.gate_peer import GatePeer
from api.model.register_gate_peer_request import RegisterGatePeerRequest
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.
    register_gate_peer_request = RegisterGatePeerRequest(
        inner_ip_address="inner_ip_address_example",
        outer_ip_address="outer_ip_address_example",
    ) # RegisterGatePeerRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Register VPG Gate peer
        api_response = api_instance.register_gate_peer(vpg_id, register_gate_peer_request)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->register_gate_peer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |
 **register_gate_peer_request** | [**RegisterGatePeerRequest**](RegisterGatePeerRequest.md)|  |

### Return type

[**GatePeer**](GatePeer.md)

### Authorization

[api_key](../README.md#api_key), [api_token](../README.md#api_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Gate peer is successfully registered. |  -  |
**400** | Client side error in the request. |  -  |
**404** | The specified VPG does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_inspection_configuration**
> set_inspection_configuration(vpg_id, junction_inspection_configuration)

Set configuration for Junction inspection feature

Set configuration for Junction inspection feature

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.junction_inspection_configuration import JunctionInspectionConfiguration
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID
    junction_inspection_configuration = JunctionInspectionConfiguration(
        enabled=False,
        report=FunnelConfiguration(
            add_sim_id=False,
            content_type=FunnelContentType("json"),
            credentials_id="credentials_id_example",
            destination=FunnelDestination(
                provider="provider_example",
                resource_url="resource_url_example",
                service="service_example",
            ),
            enabled=False,
        ),
    ) # JunctionInspectionConfiguration | Inspection configuration

    # example passing only required values which don't have defaults set
    try:
        # Set configuration for Junction inspection feature
        api_instance.set_inspection_configuration(vpg_id, junction_inspection_configuration)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->set_inspection_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |
 **junction_inspection_configuration** | [**JunctionInspectionConfiguration**](JunctionInspectionConfiguration.md)| Inspection configuration |

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
**200** | Configuration added/updated |  -  |
**404** | No such VPG found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_redirection_configuration**
> set_redirection_configuration(vpg_id, junction_redirection_configuration)

Set configuration for Junction redirection feature

Set configuration for Junction redirection feature

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.junction_redirection_configuration import JunctionRedirectionConfiguration
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID
    junction_redirection_configuration = JunctionRedirectionConfiguration(
        description="description_example",
        enabled=False,
        gateway="gateway_example",
    ) # JunctionRedirectionConfiguration | Redirection configuration

    # example passing only required values which don't have defaults set
    try:
        # Set configuration for Junction redirection feature
        api_instance.set_redirection_configuration(vpg_id, junction_redirection_configuration)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->set_redirection_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |
 **junction_redirection_configuration** | [**JunctionRedirectionConfiguration**](JunctionRedirectionConfiguration.md)| Redirection configuration |

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
**200** | Configuration added/updated |  -  |
**404** | No such VPG found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_routing_filter**
> set_routing_filter(vpg_id, routing_filter_entry)

Sets Virtual Private Gateway outbound routing filter.

Sets Virtual Private Gateway outbound routing filter.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.routing_filter_entry import RoutingFilterEntry
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.
    routing_filter_entry = [
        RoutingFilterEntry(
            action="allow",
            ip_range="ip_range_example",
        ),
    ] # [RoutingFilterEntry] | List of routing filter entries

    # example passing only required values which don't have defaults set
    try:
        # Sets Virtual Private Gateway outbound routing filter.
        api_instance.set_routing_filter(vpg_id, routing_filter_entry)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->set_routing_filter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |
 **routing_filter_entry** | [**[RoutingFilterEntry]**](RoutingFilterEntry.md)| List of routing filter entries |

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
**200** | The routing filter is successfully configured. |  -  |
**400** | Invalid argument is given |  -  |
**404** | The specified VPG does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_packet_capture_session**
> PacketCaptureSession stop_packet_capture_session(vpg_id, session_id)

Stop Packet Capture Session

Stop a packet capture session associated with the VPG

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.packet_capture_session import PacketCaptureSession
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID
    session_id = "session_id_example" # str | Packet capture session ID

    # example passing only required values which don't have defaults set
    try:
        # Stop Packet Capture Session
        api_response = api_instance.stop_packet_capture_session(vpg_id, session_id)
        pprint(api_response)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->stop_packet_capture_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |
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
**200** | The stopped packet capture session associated with the VPG |  -  |
**400** | The packet capture session can be stopped only when its status is CAPTURING |  -  |
**404** | The packet capture session associated with the VPG was not found |  -  |
**500** | The packet capture session could not be stopped |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_virtual_private_gateway**
> terminate_virtual_private_gateway(vpg_id)

Terminate Virtual Private Gateway.

Terminates the specified VPG.

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.

    # example passing only required values which don't have defaults set
    try:
        # Terminate Virtual Private Gateway.
        api_instance.terminate_virtual_private_gateway(vpg_id)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->terminate_virtual_private_gateway: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |

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
**200** | Termination of specified VPG started. |  -  |
**400** | There is a reason why the specified VPG cannot be terminated. |  -  |
**404** | The specified VPG does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unregister_gate_peer**
> unregister_gate_peer(vpg_id, outer_ip_address)

Unregister VPG gate peer

Unregister a gate peer from the Virtual Private Gateway

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | Target VPG ID.
    outer_ip_address = "outer_ip_address_example" # str | ID of the target node.

    # example passing only required values which don't have defaults set
    try:
        # Unregister VPG gate peer
        api_instance.unregister_gate_peer(vpg_id, outer_ip_address)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->unregister_gate_peer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| Target VPG ID. |
 **outer_ip_address** | **str**| ID of the target node. |

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
**204** | Successfully deregistered the Gate peer. |  -  |
**400** | Error in the request. |  -  |
**404** | The specified VPG or node does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_inspection_configuration**
> unset_inspection_configuration(vpg_id)

Unset configuration for Junction inspection feature

Unset configuration for Junction inspection feature

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID

    # example passing only required values which don't have defaults set
    try:
        # Unset configuration for Junction inspection feature
        api_instance.unset_inspection_configuration(vpg_id)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->unset_inspection_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |

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
**200** | Configuration unset |  -  |
**404** | No such VPG found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unset_redirection_configuration**
> unset_redirection_configuration(vpg_id)

Unset configuration for Junction redirection feature

Unset configuration for Junction redirection feature

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID

    # example passing only required values which don't have defaults set
    try:
        # Unset configuration for Junction redirection feature
        api_instance.unset_redirection_configuration(vpg_id)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->unset_redirection_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |

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
**200** | Configuration unset |  -  |
**404** | No such VPG found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mirroring_peer**
> update_mirroring_peer(vpg_id, ipaddr, attribute_update)

Update a Junction mirroring peer

Update a Junction mirroring peer

### Example

* Api Key Authentication (api_key):
* Api Key Authentication (api_token):

```python
import time
import api
from api.api import virtual_private_gateway_api
from api.model.attribute_update import AttributeUpdate
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
    api_instance = virtual_private_gateway_api.VirtualPrivateGatewayApi(api_client)
    vpg_id = "vpg_id_example" # str | VPG ID
    ipaddr = "ipaddr_example" # str | Mirroring peer IP address
    attribute_update = [
        AttributeUpdate(
            key="key_example",
            value="value_example",
        ),
    ] # [AttributeUpdate] | List of attributes to update

    # example passing only required values which don't have defaults set
    try:
        # Update a Junction mirroring peer
        api_instance.update_mirroring_peer(vpg_id, ipaddr, attribute_update)
    except api.ApiException as e:
        print("Exception when calling VirtualPrivateGatewayApi->update_mirroring_peer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vpg_id** | **str**| VPG ID |
 **ipaddr** | **str**| Mirroring peer IP address |
 **attribute_update** | [**[AttributeUpdate]**](AttributeUpdate.md)| List of attributes to update |

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
**200** | Mirroring peer updated |  -  |
**404** | No such VPG found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

