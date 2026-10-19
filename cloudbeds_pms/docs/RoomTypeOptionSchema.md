# RoomTypeOptionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.room_type_option_schema import RoomTypeOptionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTypeOptionSchema from a JSON string
room_type_option_schema_instance = RoomTypeOptionSchema.from_json(json)
# print the JSON string representation of the object
print(RoomTypeOptionSchema.to_json())

# convert the object into a dict
room_type_option_schema_dict = room_type_option_schema_instance.to_dict()
# create an instance of RoomTypeOptionSchema from a dict
room_type_option_schema_from_dict = RoomTypeOptionSchema.from_dict(room_type_option_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


