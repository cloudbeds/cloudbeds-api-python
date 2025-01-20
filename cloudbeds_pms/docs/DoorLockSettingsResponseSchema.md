# DoorLockSettingsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_types** | [**List[DoorLockSettingsKeyTypeResponseSchema]**](DoorLockSettingsKeyTypeResponseSchema.md) | $keyTypes | 
**encoders** | [**List[DoorLockSettingsEncoderResponseSchema]**](DoorLockSettingsEncoderResponseSchema.md) | $encoders | 
**common_rooms** | [**List[DoorLockSettingsCommonRoomResponseSchema]**](DoorLockSettingsCommonRoomResponseSchema.md) | $commonRooms | 

## Example

```python
from cloudbeds_pms.models.door_lock_settings_response_schema import DoorLockSettingsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockSettingsResponseSchema from a JSON string
door_lock_settings_response_schema_instance = DoorLockSettingsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockSettingsResponseSchema.to_json())

# convert the object into a dict
door_lock_settings_response_schema_dict = door_lock_settings_response_schema_instance.to_dict()
# create an instance of DoorLockSettingsResponseSchema from a dict
door_lock_settings_response_schema_from_dict = DoorLockSettingsResponseSchema.from_dict(door_lock_settings_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


