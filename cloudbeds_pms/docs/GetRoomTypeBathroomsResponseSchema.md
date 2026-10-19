# GetRoomTypeBathroomsResponseSchema

Response for GET /rooms/v1/{roomTypeId}/bathrooms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bathrooms** | [**List[BathroomItemResponseSchema]**](BathroomItemResponseSchema.md) | Bathrooms in the room type (ordered by position) | 

## Example

```python
from cloudbeds_pms.models.get_room_type_bathrooms_response_schema import GetRoomTypeBathroomsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomTypeBathroomsResponseSchema from a JSON string
get_room_type_bathrooms_response_schema_instance = GetRoomTypeBathroomsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GetRoomTypeBathroomsResponseSchema.to_json())

# convert the object into a dict
get_room_type_bathrooms_response_schema_dict = get_room_type_bathrooms_response_schema_instance.to_dict()
# create an instance of GetRoomTypeBathroomsResponseSchema from a dict
get_room_type_bathrooms_response_schema_from_dict = GetRoomTypeBathroomsResponseSchema.from_dict(get_room_type_bathrooms_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


