# UpdatePropertyRoomsAmenitiesResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rooms** | [**List[RoomAmenitiesSchema]**](RoomAmenitiesSchema.md) | Updated rooms with their amenities | 

## Example

```python
from cloudbeds_pms.models.update_property_rooms_amenities_response_schema import UpdatePropertyRoomsAmenitiesResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePropertyRoomsAmenitiesResponseSchema from a JSON string
update_property_rooms_amenities_response_schema_instance = UpdatePropertyRoomsAmenitiesResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UpdatePropertyRoomsAmenitiesResponseSchema.to_json())

# convert the object into a dict
update_property_rooms_amenities_response_schema_dict = update_property_rooms_amenities_response_schema_instance.to_dict()
# create an instance of UpdatePropertyRoomsAmenitiesResponseSchema from a dict
update_property_rooms_amenities_response_schema_from_dict = UpdatePropertyRoomsAmenitiesResponseSchema.from_dict(update_property_rooms_amenities_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


