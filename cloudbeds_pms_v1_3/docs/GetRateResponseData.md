# GetRateResponseData

Rates details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_id** | **str** | Rate ID | [optional] 
**is_derived** | **bool** | This rate has been derived from another rate | [optional] 
**parent_rate_id** | **str** | Rate ID of the parent rate row (null when rate is not derived). | [optional] 
**parent_rate_plan_id** | **str** | Package ID of the parent rate plan (null when not derived or derived from the room-type base rate). | [optional] 
**parent_rate_plan_name_public** | **str** | Public name of the parent rate plan (null when parentRatePlanID is null). | [optional] 
**parent_rate_plan_name_private** | **str** | Private/internal name of the parent rate plan (null when parentRatePlanID is null). | [optional] 
**room_rate** | **float** | Base rate for the room, calculated based on the Room Type ID, selected dates, and promo code. This does not include additional guest charges | [optional] 
**total_rate** | **float** | Total rate for the room, which includes the base rate (roomRate) plus additional costs for extra guests (adults and children) | [optional] 
**rooms_available** | **int** | Number of rooms available, based on the parameters provided | [optional] 
**days_of_week** | **List[str]** |  | [optional] 
**room_rate_detailed** | [**List[GetRateResponseDataRoomRateDetailedInner]**](GetRateResponseDataRoomRateDetailedInner.md) | Detailed information on the rates, if requested | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_rate_response_data import GetRateResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateResponseData from a JSON string
get_rate_response_data_instance = GetRateResponseData.from_json(json)
# print the JSON string representation of the object
print(GetRateResponseData.to_json())

# convert the object into a dict
get_rate_response_data_dict = get_rate_response_data_instance.to_dict()
# create an instance of GetRateResponseData from a dict
get_rate_response_data_from_dict = GetRateResponseData.from_dict(get_rate_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


