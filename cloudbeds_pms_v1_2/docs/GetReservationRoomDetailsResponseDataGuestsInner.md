# GetReservationRoomDetailsResponseDataGuestsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_id** | **str** | ID of assigned guest | [optional] 
**guest_first_name** | **str** | First name of assigned guest | [optional] 
**guest_last_name** | **str** | Last of assigned guest | [optional] 
**is_main_guest** | **bool** | If guest is reservation&#39;s main guest | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservation_room_details_response_data_guests_inner import GetReservationRoomDetailsResponseDataGuestsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationRoomDetailsResponseDataGuestsInner from a JSON string
get_reservation_room_details_response_data_guests_inner_instance = GetReservationRoomDetailsResponseDataGuestsInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationRoomDetailsResponseDataGuestsInner.to_json())

# convert the object into a dict
get_reservation_room_details_response_data_guests_inner_dict = get_reservation_room_details_response_data_guests_inner_instance.to_dict()
# create an instance of GetReservationRoomDetailsResponseDataGuestsInner from a dict
get_reservation_room_details_response_data_guests_inner_from_dict = GetReservationRoomDetailsResponseDataGuestsInner.from_dict(get_reservation_room_details_response_data_guests_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


