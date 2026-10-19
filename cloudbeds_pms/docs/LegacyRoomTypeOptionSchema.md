# LegacyRoomTypeOptionSchema

An earlier, narrower assignable-rooms room-type-option shape: id is an integer. See RoomTypeOptionSchema for the current shape.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.legacy_room_type_option_schema import LegacyRoomTypeOptionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyRoomTypeOptionSchema from a JSON string
legacy_room_type_option_schema_instance = LegacyRoomTypeOptionSchema.from_json(json)
# print the JSON string representation of the object
print(LegacyRoomTypeOptionSchema.to_json())

# convert the object into a dict
legacy_room_type_option_schema_dict = legacy_room_type_option_schema_instance.to_dict()
# create an instance of LegacyRoomTypeOptionSchema from a dict
legacy_room_type_option_schema_from_dict = LegacyRoomTypeOptionSchema.from_dict(legacy_room_type_option_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


