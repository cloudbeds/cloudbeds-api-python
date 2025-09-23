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
**adjust_price** | **bool** | Whether to adjust pricing when changing room types. If false, preserves existing rates. Default is true. | [optional] [default to True]

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


