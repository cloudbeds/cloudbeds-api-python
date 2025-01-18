# GetAdjustmentResponseData

Adjustment

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment_id** | **str** | Adjustment unique identifier | [optional] 
**property_id** | **str** | unique hotel identifier | [optional] 
**created** | **datetime** | Adjustment created time | [optional] 
**room_id** | **str** | Adjustment room id | [optional] 
**room_name** | **str** | Room name of Adjustment | [optional] 
**reservation_identifier** | **str** | Reservation Unique Identifier | [optional] 
**description** | **str** | Adjustment description | [optional] 
**notes** | **str** | Adjustment notes | [optional] 
**amount** | **float** | Adjustment amount | [optional] 
**currency** | **float** | Adjustment currency | [optional] 
**posted** | **float** | Adjustment posted transaction | [optional] 
**type** | **str** | Adjustment type | [optional] 
**void_id** | **str** | Voided adjustment transaction unique identifier.  Null if adjustment not voided | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_adjustment_response_data import GetAdjustmentResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdjustmentResponseData from a JSON string
get_adjustment_response_data_instance = GetAdjustmentResponseData.from_json(json)
# print the JSON string representation of the object
print(GetAdjustmentResponseData.to_json())

# convert the object into a dict
get_adjustment_response_data_dict = get_adjustment_response_data_instance.to_dict()
# create an instance of GetAdjustmentResponseData from a dict
get_adjustment_response_data_from_dict = GetAdjustmentResponseData.from_dict(get_adjustment_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


