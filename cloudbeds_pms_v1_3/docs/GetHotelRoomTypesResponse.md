# GetHotelRoomTypesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**count** | **int** | Number of results returned | [optional] 
**data** | **List[str]** | Room Types details | [optional] 
**total** | **int** | Total number of results | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_hotel_room_types_response import GetHotelRoomTypesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHotelRoomTypesResponse from a JSON string
get_hotel_room_types_response_instance = GetHotelRoomTypesResponse.from_json(json)
# print the JSON string representation of the object
print(GetHotelRoomTypesResponse.to_json())

# convert the object into a dict
get_hotel_room_types_response_dict = get_hotel_room_types_response_instance.to_dict()
# create an instance of GetHotelRoomTypesResponse from a dict
get_hotel_room_types_response_from_dict = GetHotelRoomTypesResponse.from_dict(get_hotel_room_types_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


