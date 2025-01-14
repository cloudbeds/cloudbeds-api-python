# DoorLockSettingsCommonRoomRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Common room ID. | 
**name** | **str** | Common room name. | 
**doors** | **List[str]** | Common room doors. | 

## Example

```python
from cloudbeds_pms.models.door_lock_settings_common_room_request_schema import DoorLockSettingsCommonRoomRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockSettingsCommonRoomRequestSchema from a JSON string
door_lock_settings_common_room_request_schema_instance = DoorLockSettingsCommonRoomRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockSettingsCommonRoomRequestSchema.to_json())

# convert the object into a dict
door_lock_settings_common_room_request_schema_dict = door_lock_settings_common_room_request_schema_instance.to_dict()
# create an instance of DoorLockSettingsCommonRoomRequestSchema from a dict
door_lock_settings_common_room_request_schema_from_dict = DoorLockSettingsCommonRoomRequestSchema.from_dict(door_lock_settings_common_room_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


