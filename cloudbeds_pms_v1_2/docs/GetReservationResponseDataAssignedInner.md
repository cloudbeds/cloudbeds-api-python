# GetReservationResponseDataAssignedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_name** | **str** | Name of the assigned room type | [optional] 
**room_type_name_short** | **str** | Short name of the assigned room type | [optional] 
**room_type_is_virtual** | **bool** | If room is virtual (true) or physical (false) | [optional] 
**dorm_room_name** | **str** | Name of the dorm room. Used for the shared dorm beds that are organized into rooms within the same room type | [optional] 
**room_type_id** | **str** | ID of the assigned room type | [optional] 
**sub_reservation_id** | **str** | Sub Reservation ID of the specific assigned room | [optional] 
**room_name** | **str** | Name of the specific assigned room | [optional] 
**room_id** | **str** | ID of the specific assigned room | [optional] 
**start_date** | **date** | Check-In date of the room | [optional] 
**end_date** | **date** | Check-Out date of the room | [optional] 
**adults** | **str** | Number of adult staying in the room | [optional] 
**children** | **str** | Number of children staying in the room | [optional] 
**daily_rates** | [**List[GetReservationResponseDataAssignedInnerDailyRatesInner]**](GetReservationResponseDataAssignedInnerDailyRatesInner.md) | Array with rates detailed by day | [optional] 
**room_total** | **float** | Room total rate | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservation_response_data_assigned_inner import GetReservationResponseDataAssignedInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationResponseDataAssignedInner from a JSON string
get_reservation_response_data_assigned_inner_instance = GetReservationResponseDataAssignedInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationResponseDataAssignedInner.to_json())

# convert the object into a dict
get_reservation_response_data_assigned_inner_dict = get_reservation_response_data_assigned_inner_instance.to_dict()
# create an instance of GetReservationResponseDataAssignedInner from a dict
get_reservation_response_data_assigned_inner_from_dict = GetReservationResponseDataAssignedInner.from_dict(get_reservation_response_data_assigned_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


