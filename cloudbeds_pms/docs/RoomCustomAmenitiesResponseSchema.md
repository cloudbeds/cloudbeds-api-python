# RoomCustomAmenitiesResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_amenities** | **List[str]** | List of custom room amenities | 

## Example

```python
from cloudbeds_pms.models.room_custom_amenities_response_schema import RoomCustomAmenitiesResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RoomCustomAmenitiesResponseSchema from a JSON string
room_custom_amenities_response_schema_instance = RoomCustomAmenitiesResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RoomCustomAmenitiesResponseSchema.to_json())

# convert the object into a dict
room_custom_amenities_response_schema_dict = room_custom_amenities_response_schema_instance.to_dict()
# create an instance of RoomCustomAmenitiesResponseSchema from a dict
room_custom_amenities_response_schema_from_dict = RoomCustomAmenitiesResponseSchema.from_dict(room_custom_amenities_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


