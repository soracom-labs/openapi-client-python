# SmsForwardingRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoding_type** | **int** | Encoding type of the message body. &#x60;1&#x60; indicates the body is &#x60;DCS_7BIT&#x60; that only supports single byte characters. &#x60;2&#x60; is &#x60;DCS_UCS2&#x60; that supports multi-byte text. When omitted, it is treated as &#x60;2&#x60; (&#x60;DCS_UCS2&#x60;). | [optional]  if omitted the server will use the default value of 2
**payload** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


