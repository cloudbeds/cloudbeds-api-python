# PutRoomTypeAreasResponseSchema

Response for PUT /rooms/v1/{roomTypeId}/areas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**layout_type_code** | **str** | Layout type code (null when areas are cleared) | 
**areas** | [**List[AreaItemResponseSchema]**](AreaItemResponseSchema.md) | Areas in the room type | 

## Example

```python
from cloudbeds_pms.models.put_room_type_areas_response_schema import PutRoomTypeAreasResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PutRoomTypeAreasResponseSchema from a JSON string
put_room_type_areas_response_schema_instance = PutRoomTypeAreasResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PutRoomTypeAreasResponseSchema.to_json())

# convert the object into a dict
put_room_type_areas_response_schema_dict = put_room_type_areas_response_schema_instance.to_dict()
# create an instance of PutRoomTypeAreasResponseSchema from a dict
put_room_type_areas_response_schema_from_dict = PutRoomTypeAreasResponseSchema.from_dict(put_room_type_areas_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


