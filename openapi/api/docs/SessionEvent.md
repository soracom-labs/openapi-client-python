# SessionEvent


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apn** | **str** | The Access Point Name configured. | [optional] 
**dns0** | **str** | First IP address of DNS servers. | [optional] 
**dns1** | **str** | Second IP address of DNS servers. | [optional] 
**event** | **str** | The type of behavior for the event. Possible values are \&quot;Created\&quot; indicates the device created a new session, \&quot;Modified\&quot; indicates that an existing connection was modified, \&quot;Deleted\&quot; indicates a network connection was closed. | [optional] 
**gateway_private_ip_address** | **str** |  | [optional] 
**gateway_public_ip_address** | **str** |  | [optional] 
**imei** | **str, none_type** | The IMEI of the device using the SIM. | [optional] 
**imsi** | **str** | The IMSI of the SIM. | [optional] 
**operator_id** | **str** | The operator ID of the session event. | [optional] 
**time** | **int** | The timestamp of the session event. | [optional] 
**ue_ip_address** | **str, none_type** | The IP address of the device. | [optional] 
**vpg_id** | **str** | The Virtual Private Gateway IP address configured. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


