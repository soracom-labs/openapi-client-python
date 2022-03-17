# Cell


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ci** | **int** | The Cell Identity (for 2G and 3G networks), a 16 bit value represented in decimal form as an integer. (See 3GPP TS 23.003 4.3) | [optional] 
**eci** | **int** | The E-UTRAN Cell Identifier (for LTE networks), a 28 bit value represented in decimal form as a long. (See 3GPP TS 23.003 19.6) | [optional] 
**lac** | **int** | The Location Area Code (for 2G and 3G networks), a 16 bit value represented in decimal form as an integer. (See 3GPP TS 23.003 4.1) | [optional] 
**mcc** | **int** | The Mobile Country Code, a 3 digit number. | [optional] 
**mnc** | **int** | The Mobile Network Code, a 2 or 3 digit number. If the value returned is only 1 digit in length, then you should prepend the value with a leading zero. | [optional] 
**rac** | **int** | The Routing Area Code (for 2G and 3G networks), an 8 bit value represented in decimal form as an integer. (See 3GPP TS 23.003 4.2) | [optional] 
**radio_type** | **str** | The Radio Access Technology or type of network that the device is connected to. Possible values are \&quot;gsm\&quot; for 2G or 3G networks, or \&quot;lte\&quot; for LTE networks. Unfortunately, it is not possible to differentiate 2G from 3G, or LTE from LTE Cat-M1. | [optional] 
**sac** | **int** | The Service Area Code (for 2G and 3G networks), a 16 bit value represented in decimal form as an integer. (See 3GPP TS 23.003 12.5) | [optional] 
**tac** | **int** | The Tracking Area Code (for LTE networks), a 16 bit value represented in decimal form as an integer. (See 3GPP TS 23.003 19.4.2.3) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


