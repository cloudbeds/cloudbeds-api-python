# GetAvailableRoomTypesResponseDataInnerPropertyRoomsInnerIndividualRoomsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **str** |  | [optional] 
**room_name** | **float** |  | [optional] 
**dorm_room_name** | **str** | Name of the dorm room. Used for the shared dorm beds that are organized into rooms within the same room type. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_available_room_types_response_data_inner_property_rooms_inner_individual_rooms_inner import GetAvailableRoomTypesResponseDataInnerPropertyRoomsInnerIndividualRoomsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAvailableRoomTypesResponseDataInnerPropertyRoomsInnerIndividualRoomsInner from a JSON string
get_available_room_types_response_data_inner_property_rooms_inner_individual_rooms_inner_instance = GetAvailableRoomTypesResponseDataInnerPropertyRoomsInnerIndividualRoomsInner.from_json(json)
# print the JSON string representation of the object
print(GetAvailableRoomTypesResponseDataInnerPropertyRoomsInnerIndividualRoomsInner.to_json())

# convert the object into a dict
get_available_room_types_response_data_inner_property_rooms_inner_individual_rooms_inner_dict = get_available_room_types_response_data_inner_property_rooms_inner_individual_rooms_inner_instance.to_dict()
# create an instance of GetAvailableRoomTypesResponseDataInnerPropertyRoomsInnerIndividualRoomsInner from a dict
get_available_room_types_response_data_inner_property_rooms_inner_individual_rooms_inner_from_dict = GetAvailableRoomTypesResponseDataInnerPropertyRoomsInnerIndividualRoomsInner.from_dict(get_available_room_types_response_data_inner_property_rooms_inner_individual_rooms_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


