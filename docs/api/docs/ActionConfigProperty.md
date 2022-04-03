# ActionConfigProperty


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**execution_date_time_const** | **str** |  | 
**access_key** | **str** | Only for InvokeAWSLambdaAction | [optional] 
**body** | **str** | Only for ExecuteWebRequestAction (Optional) | [optional] 
**content_type** | **str** | Only for ExecuteWebRequestAction | [optional] 
**endpoint** | **str** | Only for InvokeAWSLambdaAction | [optional] 
**execution_offset_minutes** | **str** | Run in the minutes after the timing of executionDateTimeConst | [optional] 
**function_name** | **str** | Only for InvokeAWSLambdaAction | [optional] 
**headers** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | Only for ExecuteWebRequestAction (Optional) | [optional] 
**http_method** | **str** | Only for ExecuteWebRequestAction | [optional] 
**message** | **str** | Only for SendMailAction, SendMailToOperatorAction | [optional] 
**parameter1** | **str** | Only for InvokeAWSLambdaAction | [optional] 
**parameter2** | **str** | Only for InvokeAWSLambdaAction | [optional] 
**parameter3** | **str** | Only for InvokeAWSLambdaAction | [optional] 
**parameter4** | **str** | Only for InvokeAWSLambdaAction | [optional] 
**parameter5** | **str** | Only for InvokeAWSLambdaAction | [optional] 
**secret_access_key** | **str** | Only for InvokeAWSLambdaAction | [optional] 
**speed_class** | **str** | Only for ChangeSpeedClassAction | [optional] 
**title** | **str** | Only for SendMailAction, SendMailToOperatorAction | [optional] 
**to** | **str** | Only for SendMailAction | [optional] 
**url** | **str** | Access URL and parameters. Only for ExecuteWebRequestAction | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


