# DoorLockSettingsEncoderRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.door_lock_settings_encoder_request_schema import DoorLockSettingsEncoderRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockSettingsEncoderRequestSchema from a JSON string
door_lock_settings_encoder_request_schema_instance = DoorLockSettingsEncoderRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockSettingsEncoderRequestSchema.to_json())

# convert the object into a dict
door_lock_settings_encoder_request_schema_dict = door_lock_settings_encoder_request_schema_instance.to_dict()
# create an instance of DoorLockSettingsEncoderRequestSchema from a dict
door_lock_settings_encoder_request_schema_from_dict = DoorLockSettingsEncoderRequestSchema.from_dict(door_lock_settings_encoder_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


