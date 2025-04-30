# GetReservationsResponseDataInnerGuestListValueUnassignedRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | ID of the assigned room type | [optional] 
**room_type_name** | **str** | Room Type Name where guest is assigned | [optional] 
**room_type_is_virtual** | **bool** | If room is virtual (true) or physical (false) | [optional] 
**room_type_name_short** | **str** | Room Type Short Name | [optional] 
**rate_id** | **str** | Rate ID | [optional] 
**rate_plan_name** | **str** | Rate plan name | [optional] 
**sub_reservation_id** | **str** | Sub Reservation ID of the specific assigned room | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservations_response_data_inner_guest_list_value_unassigned_rooms_inner import GetReservationsResponseDataInnerGuestListValueUnassignedRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationsResponseDataInnerGuestListValueUnassignedRoomsInner from a JSON string
get_reservations_response_data_inner_guest_list_value_unassigned_rooms_inner_instance = GetReservationsResponseDataInnerGuestListValueUnassignedRoomsInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationsResponseDataInnerGuestListValueUnassignedRoomsInner.to_json())

# convert the object into a dict
get_reservations_response_data_inner_guest_list_value_unassigned_rooms_inner_dict = get_reservations_response_data_inner_guest_list_value_unassigned_rooms_inner_instance.to_dict()
# create an instance of GetReservationsResponseDataInnerGuestListValueUnassignedRoomsInner from a dict
get_reservations_response_data_inner_guest_list_value_unassigned_rooms_inner_from_dict = GetReservationsResponseDataInnerGuestListValueUnassignedRoomsInner.from_dict(get_reservations_response_data_inner_guest_list_value_unassigned_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


