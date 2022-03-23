# Subscriber


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apn** | **str** | The Access Point Name configured. | [optional] 
**bundles** | **[str]** |  | [optional] 
**created_at** | **int** | The timestamp that the SIM was created. | [optional] 
**expired_at** | **int, none_type** | The timestamp of a date and time where the SIM was expired. | [optional] 
**expired_time** | **int** | The timestamp of a date and time where the SIM was expired. | [optional] 
**expiry_action** | **str, none_type** |  | [optional] 
**group_id** | **str, none_type** | The SIM group ID where the SIM belongs to. | [optional] 
**iccid** | **str** | The ICCID of the SIM. | [optional] 
**imei_lock** | [**ImeiLock**](ImeiLock.md) |  | [optional] 
**imsi** | **str** | The IMSI of the SIM. | [optional] 
**ip_address** | **str** |  | [optional] 
**last_modified_at** | **int** | The timestamp when the SIM information was modified. | [optional] 
**last_port_mapping_created_time** | **int, none_type** | The timestamp (in Unix milliseconds) of the last instance where the Napter On-Demand Remote Access service was used with the subscriber. If Napter has never been used with the subscriber, null is returned. | [optional] 
**module_type** | **str** | The form factor of the physical SIM. Possible values are \&quot;mini\&quot; for 2FF SIM card, \&quot;micro\&quot; for 3FF SIM card, \&quot;nano\&quot; for 4FF SIM card, \&quot;trio\&quot; for a Universal 3-in-1 (2FF/3FF/4FF) SIM card, or \&quot;embedded\&quot; for MFF2 or Embedded SIM (eSIM). | [optional] 
**msisdn** | **str** | The MSISDN of the SIM. | [optional] 
**operator_id** | **str** | The Operator ID of the SIM. | [optional] 
**plan** | **int** | Whether or not the subscription supports SMS functionality. 0 &#x3D; SMS not supported; 1 &#x3D; SMS supported. | [optional] 
**previous_session** | [**PreviousSessionStatus**](PreviousSessionStatus.md) |  | [optional] 
**registered_time** | **int** | The timestamp (in Unix milliseconds) that the subscriber was manually registered to your account. When purchasing SIMs directly through the User Console, SIMs will automatically be registered to your account, and null is returned. | [optional] 
**serial_number** | **str, none_type** | The serial number of the SIM. | [optional] 
**session_status** | [**SessionStatus**](SessionStatus.md) |  | [optional] 
**sim_id** | **str** | The SIM ID of the SIM. | [optional] 
**speed_class** | **str** | The speed class of the SIM. | [optional] 
**status** | **str** | The subscription status of the subscriber. Possible values are \&quot;ready\&quot;, \&quot;active\&quot;, \&quot;inactive\&quot;, \&quot;standby\&quot;, \&quot;suspended\&quot;, or \&quot;terminated\&quot;. | [optional] 
**subscription** | **str, none_type** | The name of the subscription for the SIM. | [optional] 
**tags** | [**TagSet**](TagSet.md) |  | [optional] 
**termination_enabled** | **bool** |  | [optional] 
**type** | **str** | The speed class of the SIM. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


