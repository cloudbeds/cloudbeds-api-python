# PutRoomTypeBathroomsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bathrooms** | [**List[BathroomItemSchema]**](BathroomItemSchema.md) | List of bathrooms for this room type. Replaces the entire bathroom configuration. Pass an empty array to clear all bathrooms. | 

## Example

```python
from cloudbeds_pms.models.put_room_type_bathrooms_request_schema import PutRoomTypeBathroomsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PutRoomTypeBathroomsRequestSchema from a JSON string
put_room_type_bathrooms_request_schema_instance = PutRoomTypeBathroomsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PutRoomTypeBathroomsRequestSchema.to_json())

# convert the object into a dict
put_room_type_bathrooms_request_schema_dict = put_room_type_bathrooms_request_schema_instance.to_dict()
# create an instance of PutRoomTypeBathroomsRequestSchema from a dict
put_room_type_bathrooms_request_schema_from_dict = PutRoomTypeBathroomsRequestSchema.from_dict(put_room_type_bathrooms_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


