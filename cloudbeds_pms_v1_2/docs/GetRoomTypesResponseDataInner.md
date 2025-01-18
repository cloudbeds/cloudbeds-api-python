# GetRoomTypesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Room Type ID | [optional] 
**property_id** | **str** | Property ID | [optional] 
**room_type_name** | **str** | Room Type Name | [optional] 
**room_type_name_short** | **str** | Room Type Short Name | [optional] 
**room_type_description** | **str** | Room Type Description | [optional] 
**is_private** | **bool** | Whether room is private or shared | [optional] 
**max_guests** | **int** | Max number of guests allowed in the room type | [optional] 
**adults_included** | **int** | Number of adults included on the basic room rate | [optional] 
**children_included** | **int** | Number of children included on the basic room rate | [optional] 
**room_type_photos** | **List[str]** | List of photos for the room type | [optional] 
**room_type_features** | **List[str]** | List of features for the room type | [optional] 
**rooms_available** | **int** | Number of rooms available, based on the parameters provided. | [optional] 
**room_rate** | **float** | Basic rate for the room, based on the parameters provided. Does not return if roomsAvailable &#x3D; 0. | [optional] 
**room_type_units** | **int** | Number of rooms of a particular type | [optional] 
**room_type_unit_dorm_beds** | **int** | Number of beds per Shared Dorm Room type | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_room_types_response_data_inner import GetRoomTypesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomTypesResponseDataInner from a JSON string
get_room_types_response_data_inner_instance = GetRoomTypesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetRoomTypesResponseDataInner.to_json())

# convert the object into a dict
get_room_types_response_data_inner_dict = get_room_types_response_data_inner_instance.to_dict()
# create an instance of GetRoomTypesResponseDataInner from a dict
get_room_types_response_data_inner_from_dict = GetRoomTypesResponseDataInner.from_dict(get_room_types_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


