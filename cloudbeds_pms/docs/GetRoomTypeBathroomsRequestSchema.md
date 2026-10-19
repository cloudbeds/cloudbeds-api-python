# GetRoomTypeBathroomsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **int** | Room type ID | 

## Example

```python
from cloudbeds_pms.models.get_room_type_bathrooms_request_schema import GetRoomTypeBathroomsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomTypeBathroomsRequestSchema from a JSON string
get_room_type_bathrooms_request_schema_instance = GetRoomTypeBathroomsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GetRoomTypeBathroomsRequestSchema.to_json())

# convert the object into a dict
get_room_type_bathrooms_request_schema_dict = get_room_type_bathrooms_request_schema_instance.to_dict()
# create an instance of GetRoomTypeBathroomsRequestSchema from a dict
get_room_type_bathrooms_request_schema_from_dict = GetRoomTypeBathroomsRequestSchema.from_dict(get_room_type_bathrooms_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


