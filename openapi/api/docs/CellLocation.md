# CellLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg_strength** | **int** | Average signal strength from all observations for the cell network. This is an integer value, in dBm. | [optional] 
**created** | **datetime** | Timestamp of the time when this record was first created. | [optional] 
**exact** | **int** | Whether or not this cell is a position estimate based on observations subject to change in the future (&#x60;0&#x60;) or an exact location entered from a knowledgeable source (&#x60;1&#x60;). | [optional] 
**lat** | **float** | Latitude | [optional] 
**lon** | **float** | Longitude | [optional] 
**range** | **int** | Estimate of radio range, in meters. This is an estimate on how large each cell area is, as a radius around the estimated position and is based on the observations or a knowledgeable source. | [optional] 
**samples** | **int** | Total number of observations used to calculate the estimated position, range and avg_strength. | [optional] 
**updated** | **datetime** | Timestamp of the time when this record was most recently modified. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


