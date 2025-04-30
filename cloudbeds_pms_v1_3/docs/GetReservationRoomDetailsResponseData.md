# GetReservationRoomDetailsResponseData

Details for the rooms assigned on the selected date

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | Reservation Unique Identifier. | [optional] 
**sub_reservation_id** | **str** | Subreservation Unique Identifier | [optional] 
**room_id** | **str** | ID of room assigned | [optional] 
**room_name** | **str** | Name of room assigned | [optional] 
**dorm_room_name** | **str** | Name of the dorm room. Used for the shared dorm beds that are organized into rooms within the same room type. | [optional] 
**guest_id** | **str** | Guest Identifier | [optional] 
**guest_name** | **str** | Guest Name | [optional] 
**room_status** | **str** | Room status&lt;br /&gt; &#39;cancelled&#39; - Reservation with this room was canceled&lt;br /&gt; &#39;checked_out&#39; - Guest already left the room&lt;br /&gt; &#39;in_house&#39; - Guest is in the room&lt;br /&gt; &#39;not_checked_in&#39; - Guest isn&#39;t checked-in yet | [optional] 
**room_type_id** | **str** | ID of room type assigned | [optional] 
**room_type_name** | **str** | Name of room type assigned | [optional] 
**room_type_is_virtual** | **bool** | If room is virtual (true) or physical (false) | [optional] 
**max_guests** | **int** | Maximum number of guests that room type permits | [optional] 
**adults** | **int** | Number of adults registered to room (this does not mean there will be this number of guests in guests array) | [optional] 
**children** | **int** | Number of children registered to room (this does not mean there will be this number of guests in guests array) | [optional] 
**guests** | [**List[GetReservationRoomDetailsResponseDataGuestsInner]**](GetReservationRoomDetailsResponseDataGuestsInner.md) | Array with all guests assigned to room | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_room_details_response_data import GetReservationRoomDetailsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationRoomDetailsResponseData from a JSON string
get_reservation_room_details_response_data_instance = GetReservationRoomDetailsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetReservationRoomDetailsResponseData.to_json())

# convert the object into a dict
get_reservation_room_details_response_data_dict = get_reservation_room_details_response_data_instance.to_dict()
# create an instance of GetReservationRoomDetailsResponseData from a dict
get_reservation_room_details_response_data_from_dict = GetReservationRoomDetailsResponseData.from_dict(get_reservation_room_details_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


