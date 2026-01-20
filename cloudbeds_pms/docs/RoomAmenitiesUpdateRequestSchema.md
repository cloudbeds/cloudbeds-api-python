# RoomAmenitiesUpdateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Room ID to update | 
**amenities** | **List[str]** | List of amenity codes to set for the room (full replace) | 

## Example

```python
from cloudbeds_pms.models.room_amenities_update_request_schema import RoomAmenitiesUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RoomAmenitiesUpdateRequestSchema from a JSON string
room_amenities_update_request_schema_instance = RoomAmenitiesUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(RoomAmenitiesUpdateRequestSchema.to_json())

# convert the object into a dict
room_amenities_update_request_schema_dict = room_amenities_update_request_schema_instance.to_dict()
# create an instance of RoomAmenitiesUpdateRequestSchema from a dict
room_amenities_update_request_schema_from_dict = RoomAmenitiesUpdateRequestSchema.from_dict(room_amenities_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


