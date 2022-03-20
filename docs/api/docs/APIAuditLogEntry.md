# APIAuditLogEntry


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_kind** | **str** | The kind of the API (e.g. &#x60;/v1/auth&#x60;). | [optional] 
**operator_id** | **str** | The operator ID that called the API. | [optional] 
**remote_ip_address** | **str** | The IP address of the caller. | [optional] 
**request_path** | **str** | The request path that has been called. | [optional] 
**requested_time_epoch_ms** | **int** | The timestamp of the API call. This can be used as the &#x60;last_evaluated_key&#x60; request parameter, for pagination. | [optional] 
**user_name** | **str** | The SAM username that called the API, if this parameter is empty, it means the caller user is the root user. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


