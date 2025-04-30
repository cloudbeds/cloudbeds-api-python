# GetAvailableRoomTypesResponseDataInnerPropertyRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Room type ID | [optional] 
**room_type_name** | **str** | Room type name | [optional] 
**room_type_name_short** | **str** | Room type short name | [optional] 
**room_type_description** | **str** | Room Type Description | [optional] 
**max_guests** | **int** | Max number of guests allowed in the room type | [optional] 
**adults_included** | **int** | Number of adults included on the basic room rate | [optional] 
**children_included** | **int** | Number of children included on the basic room rate | [optional] 
**room_type_photos** | [**List[GetHotelDetailsResponseDataPropertyImageInner]**](GetHotelDetailsResponseDataPropertyImageInner.md) | List of photos for the room type | [optional] 
**room_type_features** | **List[str]** | List of features for the room type | [optional] 
**room_rate** | **float** | Basic rate for the room, based on the parameters provided | [optional] 
**room_rate_id** | **str** | Specific Rate ID used for the room type ID | [optional] 
**rate_plan_name_public** | **str** | Rate plan public name | [optional] 
**rate_plan_name_private** | **str** | Rate plan private name | [optional] 
**rooms_available** | **int** | Number of rooms available, based on the parameters provided | [optional] 
**adults_extra_charge** | **List[object]** | Total extra charge for number of adults, depending on room settings (see \&quot;adultsIncluded\&quot; field). It is an associative array, where the key is the number of adults, and the value is the total extra charge when the number of adults is selected. | [optional] 
**children_extra_charge** | **List[object]** | Total extra charge for number of children, depending on room settings (see \&quot;childrenIncluded\&quot; field). It is an associative array, where the key is the number of children, and the value is the total extra charge when the number of children is selected. | [optional] 
**room_rate_detailed** | [**List[GetAvailableRoomTypesResponseDataInnerPropertyRoomsInnerRoomRateDetailedInner]**](GetAvailableRoomTypesResponseDataInnerPropertyRoomsInnerRoomRateDetailedInner.md) | Detailed information on the rates, if requested | [optional] 
**derived_type** | **str** | type of deriving (only if current rate was derived from other one). | [optional] 
**derived_value** | **float** | Can be positive or negative (only if current rate was derived from other one). | [optional] 
**individual_rooms** | [**List[GetAvailableRoomTypesResponseDataInnerPropertyRoomsInnerIndividualRoomsInner]**](GetAvailableRoomTypesResponseDataInnerPropertyRoomsInnerIndividualRoomsInner.md) | Individual rooms available to be booked (if set on backend) | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_available_room_types_response_data_inner_property_rooms_inner import GetAvailableRoomTypesResponseDataInnerPropertyRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableRoomTypesResponseDataInnerPropertyRoomsInner from a JSON string
get_available_room_types_response_data_inner_property_rooms_inner_instance = GetAvailableRoomTypesResponseDataInnerPropertyRoomsInner.from_json(json)
# print the JSON string representation of the object
print(GetAvailableRoomTypesResponseDataInnerPropertyRoomsInner.to_json())

# convert the object into a dict
get_available_room_types_response_data_inner_property_rooms_inner_dict = get_available_room_types_response_data_inner_property_rooms_inner_instance.to_dict()
# create an instance of GetAvailableRoomTypesResponseDataInnerPropertyRoomsInner from a dict
get_available_room_types_response_data_inner_property_rooms_inner_from_dict = GetAvailableRoomTypesResponseDataInnerPropertyRoomsInner.from_dict(get_available_room_types_response_data_inner_property_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


