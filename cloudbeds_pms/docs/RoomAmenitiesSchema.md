# RoomAmenitiesSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Room ID | 
**amenities** | [**List[AmenityItemSchema]**](AmenityItemSchema.md) | List of active amenities for this room | 

## Example

```python
from cloudbeds_pms.models.room_amenities_schema import RoomAmenitiesSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RoomAmenitiesSchema from a JSON string
room_amenities_schema_instance = RoomAmenitiesSchema.from_json(json)
# print the JSON string representation of the object
print(RoomAmenitiesSchema.to_json())

# convert the object into a dict
room_amenities_schema_dict = room_amenities_schema_instance.to_dict()
# create an instance of RoomAmenitiesSchema from a dict
room_amenities_schema_from_dict = RoomAmenitiesSchema.from_dict(room_amenities_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


