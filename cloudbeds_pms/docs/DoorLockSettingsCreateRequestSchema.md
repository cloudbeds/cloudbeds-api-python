# DoorLockSettingsCreateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encoders** | [**List[DoorLockSettingsEncoderRequestSchema]**](DoorLockSettingsEncoderRequestSchema.md) | List of supported encoders. | [default to []]
**key_types** | [**List[DoorLockSettingsKeyTypeRequestSchema]**](DoorLockSettingsKeyTypeRequestSchema.md) | List of supported key types. | [default to []]
**common_rooms** | [**List[DoorLockSettingsCommonRoomRequestSchema]**](DoorLockSettingsCommonRoomRequestSchema.md) | List of common rooms. | [default to []]

## Example

```python
from cloudbeds_pms.models.door_lock_settings_create_request_schema import DoorLockSettingsCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockSettingsCreateRequestSchema from a JSON string
door_lock_settings_create_request_schema_instance = DoorLockSettingsCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockSettingsCreateRequestSchema.to_json())

# convert the object into a dict
door_lock_settings_create_request_schema_dict = door_lock_settings_create_request_schema_instance.to_dict()
# create an instance of DoorLockSettingsCreateRequestSchema from a dict
door_lock_settings_create_request_schema_from_dict = DoorLockSettingsCreateRequestSchema.from_dict(door_lock_settings_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


