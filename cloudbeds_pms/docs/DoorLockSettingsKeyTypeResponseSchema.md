# DoorLockSettingsKeyTypeResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.door_lock_settings_key_type_response_schema import DoorLockSettingsKeyTypeResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockSettingsKeyTypeResponseSchema from a JSON string
door_lock_settings_key_type_response_schema_instance = DoorLockSettingsKeyTypeResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockSettingsKeyTypeResponseSchema.to_json())

# convert the object into a dict
door_lock_settings_key_type_response_schema_dict = door_lock_settings_key_type_response_schema_instance.to_dict()
# create an instance of DoorLockSettingsKeyTypeResponseSchema from a dict
door_lock_settings_key_type_response_schema_from_dict = DoorLockSettingsKeyTypeResponseSchema.from_dict(door_lock_settings_key_type_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


