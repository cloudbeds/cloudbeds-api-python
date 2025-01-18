# GetReservationRoomDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 
**data** | [**GetReservationRoomDetailsResponseData**](GetReservationRoomDetailsResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservation_room_details_response import GetReservationRoomDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationRoomDetailsResponse from a JSON string
get_reservation_room_details_response_instance = GetReservationRoomDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetReservationRoomDetailsResponse.to_json())

# convert the object into a dict
get_reservation_room_details_response_dict = get_reservation_room_details_response_instance.to_dict()
# create an instance of GetReservationRoomDetailsResponse from a dict
get_reservation_room_details_response_from_dict = GetReservationRoomDetailsResponse.from_dict(get_reservation_room_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


