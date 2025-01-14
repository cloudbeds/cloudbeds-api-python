# DoorLockSettingsCommonRoomResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**doors** | **List[str]** | $doors | 

## Example

```python
from cloudbeds_pms.models.door_lock_settings_common_room_response_schema import DoorLockSettingsCommonRoomResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockSettingsCommonRoomResponseSchema from a JSON string
door_lock_settings_common_room_response_schema_instance = DoorLockSettingsCommonRoomResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockSettingsCommonRoomResponseSchema.to_json())

# convert the object into a dict
door_lock_settings_common_room_response_schema_dict = door_lock_settings_common_room_response_schema_instance.to_dict()
# create an instance of DoorLockSettingsCommonRoomResponseSchema from a dict
door_lock_settings_common_room_response_schema_from_dict = DoorLockSettingsCommonRoomResponseSchema.from_dict(door_lock_settings_common_room_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


