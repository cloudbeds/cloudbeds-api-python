# UpdateRoomAmenitiesRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenities** | **List[str]** | List of amenity codes to set for the room | [optional] 

## Example

```python
from cloudbeds_pms.models.update_room_amenities_request_schema import UpdateRoomAmenitiesRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoomAmenitiesRequestSchema from a JSON string
update_room_amenities_request_schema_instance = UpdateRoomAmenitiesRequestSchema.from_json(json)
# print the JSON string representation of the object
print(UpdateRoomAmenitiesRequestSchema.to_json())

# convert the object into a dict
update_room_amenities_request_schema_dict = update_room_amenities_request_schema_instance.to_dict()
# create an instance of UpdateRoomAmenitiesRequestSchema from a dict
update_room_amenities_request_schema_from_dict = UpdateRoomAmenitiesRequestSchema.from_dict(update_room_amenities_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


