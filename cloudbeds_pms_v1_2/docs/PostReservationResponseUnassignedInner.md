# PostReservationResponseUnassignedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_reservation_id** | **str** |  | [optional] 
**room_type_name** | **str** |  | [optional] 
**room_type_id** | **str** |  | [optional] 
**adults** | **int** | Adults included in rate | [optional] 
**children** | **int** | Children included in rate | [optional] 
**daily_rates** | [**List[GetReservationResponseDataAssignedInnerDailyRatesInner]**](GetReservationResponseDataAssignedInnerDailyRatesInner.md) | rates for room | [optional] 
**room_total** | **float** |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_reservation_response_unassigned_inner import PostReservationResponseUnassignedInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostReservationResponseUnassignedInner from a JSON string
post_reservation_response_unassigned_inner_instance = PostReservationResponseUnassignedInner.from_json(json)
# print the JSON string representation of the object
print(PostReservationResponseUnassignedInner.to_json())

# convert the object into a dict
post_reservation_response_unassigned_inner_dict = post_reservation_response_unassigned_inner_instance.to_dict()
# create an instance of PostReservationResponseUnassignedInner from a dict
post_reservation_response_unassigned_inner_from_dict = PostReservationResponseUnassignedInner.from_dict(post_reservation_response_unassigned_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


