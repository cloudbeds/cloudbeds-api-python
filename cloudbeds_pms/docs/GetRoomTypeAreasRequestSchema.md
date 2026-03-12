# GetRoomTypeAreasRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **int** | Room type ID | 

## Example

```python
from cloudbeds_pms.models.get_room_type_areas_request_schema import GetRoomTypeAreasRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoomTypeAreasRequestSchema from a JSON string
get_room_type_areas_request_schema_instance = GetRoomTypeAreasRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GetRoomTypeAreasRequestSchema.to_json())

# convert the object into a dict
get_room_type_areas_request_schema_dict = get_room_type_areas_request_schema_instance.to_dict()
# create an instance of GetRoomTypeAreasRequestSchema from a dict
get_room_type_areas_request_schema_from_dict = GetRoomTypeAreasRequestSchema.from_dict(get_room_type_areas_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


