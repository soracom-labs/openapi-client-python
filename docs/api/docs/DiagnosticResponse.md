# DiagnosticResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**diagnostic_id** | **str** |  | [optional] 
**_from** | **int** | Start time for diagnostic (unixtime milliseconds) | [optional] 
**insights** | [**[{str: (Insight,)}]**](Insight.md) |  | [optional] 
**resource_id** | **str** | resourceId according to resourceType | [optional] 
**resource_type** | **str** |  | [optional]  if omitted the server will use the default value of "sim"
**service** | **str** |  | [optional]  if omitted the server will use the default value of "Air"
**status** | **str** |  | [optional] 
**to** | **int** | End time for diagnostic (unixtime milliseconds) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


