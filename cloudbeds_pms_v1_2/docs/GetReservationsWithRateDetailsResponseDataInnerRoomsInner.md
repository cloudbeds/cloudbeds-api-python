# GetReservationsWithRateDetailsResponseDataInnerRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Room Type ID | [optional] 
**room_type_is_virtual** | **bool** | If room is virtual (true) or physical (false) | [optional] 
**room_type_name** | **str** | Room Type Name | [optional] 
**sub_reservation_id** | **str** | sub Reservation ID (specific to each room) | [optional] 
**guest_id** | **str** | ID of the main guest assigned to the room | [optional] 
**guest_name** | **str** | Name of the main guest assigned to the room | [optional] 
**rate_id** | **str** | ID of the rate used for the booking room | [optional] 
**rate_name** | **str** | Name of the rate used for the booking room | [optional] 
**adults** | **str** | Number of adults in the room | [optional] 
**children** | **str** | Number of children in the room | [optional] 
**room_id** | **str** | Room ID (null if the reservation has not been assigned a specific room yet). | [optional] 
**room_name** | **str** | Name of the room, if roomID&#x3D;null it does not exist. | [optional] 
**room_check_in** | **str** | Check-in date for the room | [optional] 
**room_check_out** | **str** | Check-out date for the room | [optional] 
**room_status** | **str** |  | [optional] 
**detailed_room_rates** | **List[object]** | Associative object, with dates as indexes, and rates as values | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservations_with_rate_details_response_data_inner_rooms_inner import GetReservationsWithRateDetailsResponseDataInnerRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationsWithRateDetailsResponseDataInnerRoomsInner from a JSON string
get_reservations_with_rate_details_response_data_inner_rooms_inner_instance = GetReservationsWithRateDetailsResponseDataInnerRoomsInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationsWithRateDetailsResponseDataInnerRoomsInner.to_json())

# convert the object into a dict
get_reservations_with_rate_details_response_data_inner_rooms_inner_dict = get_reservations_with_rate_details_response_data_inner_rooms_inner_instance.to_dict()
# create an instance of GetReservationsWithRateDetailsResponseDataInnerRoomsInner from a dict
get_reservations_with_rate_details_response_data_inner_rooms_inner_from_dict = GetReservationsWithRateDetailsResponseDataInnerRoomsInner.from_dict(get_reservations_with_rate_details_response_data_inner_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


