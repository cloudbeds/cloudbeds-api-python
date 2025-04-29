# GetRatePlansResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_id** | **str** | Rate ID | [optional] 
**is_derived** | **bool** | True if this rate is derived from another rate | [optional] 
**room_rate** | **float** | Rate for the room, based on the parameters provided | [optional] 
**total_rate** | **float** | Total rate for the room, based on the parameters provided. Calculated using base rates and additional costs from extra guests. | [optional] 
**rooms_available** | **int** | Number of rooms available for the selected date | [optional] 
**room_type_id** | **str** | ] room type ID (if not specified in request) | [optional] 
**room_type_name** | **int** | ] room type name (if not specified in request) | [optional] 
**property_id** | **str** | Property ID, used if multiple properties are included in request | [optional] 
**rate_plan_id** | **str** | ratePlanID (If rate depends on plan) | [optional] 
**rate_plan_name_public** | **str** | ratePlanNamePublic | [optional] 
**rate_plan_name_private** | **str** | ratePlanNamePrivate | [optional] 
**promo_code** | **str** | Promotional code when rate plan has has it | [optional] 
**derived_type** | **str** | type of deriving (only if current rate was derived from other one). | [optional] 
**derived_value** | **float** | Can be positive or negative (only if current rate was derived from other one). | [optional] 
**base_rate** | **float** | Base rate on given period | [optional] 
**days_of_week** | **List[str]** | Returns when there is a difference between range given with startDate/endDate and days of week which rate plan applies. | [optional] 
**add_ons** | [**List[GetRatePlansResponseDataInnerAddOnsInner]**](GetRatePlansResponseDataInnerAddOnsInner.md) | addOns information on the rates | [optional] 
**room_rate_detailed** | [**List[GetRatePlansResponseDataInnerRoomRateDetailedInner]**](GetRatePlansResponseDataInnerRoomRateDetailedInner.md) | Detailed information on the rates, if requested | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_rate_plans_response_data_inner import GetRatePlansResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRatePlansResponseDataInner from a JSON string
get_rate_plans_response_data_inner_instance = GetRatePlansResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetRatePlansResponseDataInner.to_json())

# convert the object into a dict
get_rate_plans_response_data_inner_dict = get_rate_plans_response_data_inner_instance.to_dict()
# create an instance of GetRatePlansResponseDataInner from a dict
get_rate_plans_response_data_inner_from_dict = GetRatePlansResponseDataInner.from_dict(get_rate_plans_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


