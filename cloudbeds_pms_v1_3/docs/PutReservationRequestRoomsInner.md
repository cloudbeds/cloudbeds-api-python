# PutReservationRequestRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_reservation_id** | **str** | Sub Reservation ID of the specific assigned room. Optional. | [optional] 
**room_type_id** | **str** | Room Type ID. Mandatory if rooms are sent. | [optional] 
**checkin_date** | **date** | Check-in date for this specific room. Mandatory if rooms are sent. | [optional] 
**checkout_date** | **date** | Check-out date for this specific room. Mandatory if rooms are sent. | [optional] 
**adults** | **int** | Quantity of adults for the room. Mandatory if rooms are sent. | [optional] 
**children** | **int** | Number of children for the room. Mandatory if rooms are sent. | [optional] 
**rate_id** | **str** | Rate ID for the room. Optional. | [optional] 
**adjust_price** | **bool** | Whether to re-price the room after the change (default true). When false, the existing price is preserved for ANY modification of the room (room-type change, guest-count change, or a same-length or shortened stay), not only room-type changes. Because the price is held as-is, increasing the guest count keeps the existing price and is NOT charged the extra-guest amount (per-guest taxes and fees may still recalculate for the new occupancy). A modification that has no existing rate to preserve - extending the stay, or shifting it onto dates the reservation did not previously cover - cannot be honored and is rejected. | [optional] [default to True]

## Example

```python
from cloudbeds_pms_v1_3.models.put_reservation_request_rooms_inner import PutReservationRequestRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PutReservationRequestRoomsInner from a JSON string
put_reservation_request_rooms_inner_instance = PutReservationRequestRoomsInner.from_json(json)
# print the JSON string representation of the object
print(PutReservationRequestRoomsInner.to_json())

# convert the object into a dict
put_reservation_request_rooms_inner_dict = put_reservation_request_rooms_inner_instance.to_dict()
# create an instance of PutReservationRequestRoomsInner from a dict
put_reservation_request_rooms_inner_from_dict = PutReservationRequestRoomsInner.from_dict(put_reservation_request_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


