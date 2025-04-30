# GetAdjustmentsResponseData

Adjustments

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adjustment_id** | **str** | Adjustment unique identifier | [optional] 
**created** | **datetime** | Adjustment created time | [optional] 
**room_id** | **str** | Adjustment room id | [optional] 
**room_name** | **str** | Room name of Adjustment | [optional] 
**description** | **str** | Adjustment description | [optional] 
**notes** | **str** | Adjustment notes | [optional] 
**amount** | **float** | Adjustment amount | [optional] 
**type** | **str** | Adjustment type | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_adjustments_response_data import GetAdjustmentsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetAdjustmentsResponseData from a JSON string
get_adjustments_response_data_instance = GetAdjustmentsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetAdjustmentsResponseData.to_json())

# convert the object into a dict
get_adjustments_response_data_dict = get_adjustments_response_data_instance.to_dict()
# create an instance of GetAdjustmentsResponseData from a dict
get_adjustments_response_data_from_dict = GetAdjustmentsResponseData.from_dict(get_adjustments_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


