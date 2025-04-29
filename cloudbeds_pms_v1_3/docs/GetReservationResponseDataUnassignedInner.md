# GetReservationResponseDataUnassignedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_name** | **str** | Name of the room type to be assigned | [optional] 
**room_type_is_virtual** | **bool** | If room is virtual (true) or physical (false) | [optional] 
**room_type_id** | **str** | ID of the room type to be assigned | [optional] 
**sub_reservation_id** | **str** | Sub Reservation ID of the specific assigned room | [optional] 
**start_date** | **date** | Check-In date of the room | [optional] 
**end_date** | **date** | Check-Out date of the room | [optional] 
**adults** | **str** | Number of adult staying in the room | [optional] 
**children** | **str** | Number of children staying in the room | [optional] 
**daily_rates** | [**List[GetReservationResponseDataAssignedInnerDailyRatesInner]**](GetReservationResponseDataAssignedInnerDailyRatesInner.md) | Array with rates detailed by day | [optional] 
**room_total** | **float** | Room total rate | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_response_data_unassigned_inner import GetReservationResponseDataUnassignedInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationResponseDataUnassignedInner from a JSON string
get_reservation_response_data_unassigned_inner_instance = GetReservationResponseDataUnassignedInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationResponseDataUnassignedInner.to_json())

# convert the object into a dict
get_reservation_response_data_unassigned_inner_dict = get_reservation_response_data_unassigned_inner_instance.to_dict()
# create an instance of GetReservationResponseDataUnassignedInner from a dict
get_reservation_response_data_unassigned_inner_from_dict = GetReservationResponseDataUnassignedInner.from_dict(get_reservation_response_data_unassigned_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


