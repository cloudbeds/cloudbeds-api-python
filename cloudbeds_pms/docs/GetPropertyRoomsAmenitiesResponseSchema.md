# GetPropertyRoomsAmenitiesResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rooms** | [**List[RoomAmenitiesSchema]**](RoomAmenitiesSchema.md) | List of rooms with their amenities | 

## Example

```python
from cloudbeds_pms.models.get_property_rooms_amenities_response_schema import GetPropertyRoomsAmenitiesResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetPropertyRoomsAmenitiesResponseSchema from a JSON string
get_property_rooms_amenities_response_schema_instance = GetPropertyRoomsAmenitiesResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GetPropertyRoomsAmenitiesResponseSchema.to_json())

# convert the object into a dict
get_property_rooms_amenities_response_schema_dict = get_property_rooms_amenities_response_schema_instance.to_dict()
# create an instance of GetPropertyRoomsAmenitiesResponseSchema from a dict
get_property_rooms_amenities_response_schema_from_dict = GetPropertyRoomsAmenitiesResponseSchema.from_dict(get_property_rooms_amenities_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


