# UpdateRoomAmenitiesResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenities** | [**List[AmenityItemSchema]**](AmenityItemSchema.md) | Updated list of room amenities | 

## Example

```python
from cloudbeds_pms.models.update_room_amenities_response_schema import UpdateRoomAmenitiesResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRoomAmenitiesResponseSchema from a JSON string
update_room_amenities_response_schema_instance = UpdateRoomAmenitiesResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UpdateRoomAmenitiesResponseSchema.to_json())

# convert the object into a dict
update_room_amenities_response_schema_dict = update_room_amenities_response_schema_instance.to_dict()
# create an instance of UpdateRoomAmenitiesResponseSchema from a dict
update_room_amenities_response_schema_from_dict = UpdateRoomAmenitiesResponseSchema.from_dict(update_room_amenities_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


