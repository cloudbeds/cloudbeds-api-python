# GetReservationResponseDataGuestListValueRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **str** | Room ID where guest is assigned | [optional] 
**room_name** | **str** | Room Name where guest is assigned | [optional] 
**room_type_name** | **str** | Room Type Name where guest is assigned | [optional] 
**room_type_is_virtual** | **bool** | If room is virtual (true) or physical (false) | [optional] 
**sub_reservation_id** | **str** | Sub Reservation ID of the specific assigned room | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_response_data_guest_list_value_rooms_inner import GetReservationResponseDataGuestListValueRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationResponseDataGuestListValueRoomsInner from a JSON string
get_reservation_response_data_guest_list_value_rooms_inner_instance = GetReservationResponseDataGuestListValueRoomsInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationResponseDataGuestListValueRoomsInner.to_json())

# convert the object into a dict
get_reservation_response_data_guest_list_value_rooms_inner_dict = get_reservation_response_data_guest_list_value_rooms_inner_instance.to_dict()
# create an instance of GetReservationResponseDataGuestListValueRoomsInner from a dict
get_reservation_response_data_guest_list_value_rooms_inner_from_dict = GetReservationResponseDataGuestListValueRoomsInner.from_dict(get_reservation_response_data_guest_list_value_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


