# RoomAmenitiesUpdateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Room ID | 
**amenities** | [**List[AmenityItemSchema]**](AmenityItemSchema.md) | List of active amenities for this room | 

## Example

```python
from cloudbeds_pms.models.room_amenities_update_schema import RoomAmenitiesUpdateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RoomAmenitiesUpdateSchema from a JSON string
room_amenities_update_schema_instance = RoomAmenitiesUpdateSchema.from_json(json)
# print the JSON string representation of the object
print(RoomAmenitiesUpdateSchema.to_json())

# convert the object into a dict
room_amenities_update_schema_dict = room_amenities_update_schema_instance.to_dict()
# create an instance of RoomAmenitiesUpdateSchema from a dict
room_amenities_update_schema_from_dict = RoomAmenitiesUpdateSchema.from_dict(room_amenities_update_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


