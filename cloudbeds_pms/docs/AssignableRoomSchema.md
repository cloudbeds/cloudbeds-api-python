# AssignableRoomSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_id** | **str** | Composite room id \&quot;{roomTypeId}-{roomNumber}\&quot; used by the reassign action. | 
**name** | **str** |  | 
**housekeeping_status** | **str** | Housekeeping status key. | 

## Example

```python
from cloudbeds_pms.models.assignable_room_schema import AssignableRoomSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AssignableRoomSchema from a JSON string
assignable_room_schema_instance = AssignableRoomSchema.from_json(json)
# print the JSON string representation of the object
print(AssignableRoomSchema.to_json())

# convert the object into a dict
assignable_room_schema_dict = assignable_room_schema_instance.to_dict()
# create an instance of AssignableRoomSchema from a dict
assignable_room_schema_from_dict = AssignableRoomSchema.from_dict(assignable_room_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


