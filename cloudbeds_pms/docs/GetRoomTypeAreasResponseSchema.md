# GetRoomTypeAreasResponseSchema

Response for GET /rooms/v1/{roomTypeId}/areas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout_type_code** | **str** | Layout type code (empty string if not set) | 
**areas** | [**List[AreaItemResponseSchema]**](AreaItemResponseSchema.md) | Areas in the room type (ordered by position) | 

## Example

```python
from cloudbeds_pms.models.get_room_type_areas_response_schema import GetRoomTypeAreasResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomTypeAreasResponseSchema from a JSON string
get_room_type_areas_response_schema_instance = GetRoomTypeAreasResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GetRoomTypeAreasResponseSchema.to_json())

# convert the object into a dict
get_room_type_areas_response_schema_dict = get_room_type_areas_response_schema_instance.to_dict()
# create an instance of GetRoomTypeAreasResponseSchema from a dict
get_room_type_areas_response_schema_from_dict = GetRoomTypeAreasResponseSchema.from_dict(get_room_type_areas_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


