# DeleteRoomCustomAmenitiesRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_amenities** | **List[str]** | List of custom room amenities to remove from the room | [optional] 

## Example

```python
from cloudbeds_pms.models.delete_room_custom_amenities_request_schema import DeleteRoomCustomAmenitiesRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteRoomCustomAmenitiesRequestSchema from a JSON string
delete_room_custom_amenities_request_schema_instance = DeleteRoomCustomAmenitiesRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DeleteRoomCustomAmenitiesRequestSchema.to_json())

# convert the object into a dict
delete_room_custom_amenities_request_schema_dict = delete_room_custom_amenities_request_schema_instance.to_dict()
# create an instance of DeleteRoomCustomAmenitiesRequestSchema from a dict
delete_room_custom_amenities_request_schema_from_dict = DeleteRoomCustomAmenitiesRequestSchema.from_dict(delete_room_custom_amenities_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


