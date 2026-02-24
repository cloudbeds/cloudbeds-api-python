# GetRoomAmenitiesResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenities** | [**List[AmenityItemSchema]**](AmenityItemSchema.md) | List of active room amenities | 
**custom_amenities** | **List[str]** | List of custom room amenities | 

## Example

```python
from cloudbeds_pms.models.get_room_amenities_response_schema import GetRoomAmenitiesResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomAmenitiesResponseSchema from a JSON string
get_room_amenities_response_schema_instance = GetRoomAmenitiesResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GetRoomAmenitiesResponseSchema.to_json())

# convert the object into a dict
get_room_amenities_response_schema_dict = get_room_amenities_response_schema_instance.to_dict()
# create an instance of GetRoomAmenitiesResponseSchema from a dict
get_room_amenities_response_schema_from_dict = GetRoomAmenitiesResponseSchema.from_dict(get_room_amenities_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


