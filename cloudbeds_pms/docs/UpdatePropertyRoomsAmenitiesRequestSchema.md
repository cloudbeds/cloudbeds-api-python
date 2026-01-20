# UpdatePropertyRoomsAmenitiesRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rooms** | [**List[RoomAmenitiesUpdateRequestSchema]**](RoomAmenitiesUpdateRequestSchema.md) | List of rooms with amenities to update | 

## Example

```python
from cloudbeds_pms.models.update_property_rooms_amenities_request_schema import UpdatePropertyRoomsAmenitiesRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePropertyRoomsAmenitiesRequestSchema from a JSON string
update_property_rooms_amenities_request_schema_instance = UpdatePropertyRoomsAmenitiesRequestSchema.from_json(json)
# print the JSON string representation of the object
print(UpdatePropertyRoomsAmenitiesRequestSchema.to_json())

# convert the object into a dict
update_property_rooms_amenities_request_schema_dict = update_property_rooms_amenities_request_schema_instance.to_dict()
# create an instance of UpdatePropertyRoomsAmenitiesRequestSchema from a dict
update_property_rooms_amenities_request_schema_from_dict = UpdatePropertyRoomsAmenitiesRequestSchema.from_dict(update_property_rooms_amenities_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


