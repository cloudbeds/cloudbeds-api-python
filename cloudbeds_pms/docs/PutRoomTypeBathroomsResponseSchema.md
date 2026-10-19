# PutRoomTypeBathroomsResponseSchema

Response for PUT /rooms/v1/{roomTypeId}/bathrooms

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bathrooms** | [**List[BathroomItemResponseSchema]**](BathroomItemResponseSchema.md) | Bathrooms in the room type after update | 

## Example

```python
from cloudbeds_pms.models.put_room_type_bathrooms_response_schema import PutRoomTypeBathroomsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PutRoomTypeBathroomsResponseSchema from a JSON string
put_room_type_bathrooms_response_schema_instance = PutRoomTypeBathroomsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PutRoomTypeBathroomsResponseSchema.to_json())

# convert the object into a dict
put_room_type_bathrooms_response_schema_dict = put_room_type_bathrooms_response_schema_instance.to_dict()
# create an instance of PutRoomTypeBathroomsResponseSchema from a dict
put_room_type_bathrooms_response_schema_from_dict = PutRoomTypeBathroomsResponseSchema.from_dict(put_room_type_bathrooms_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


