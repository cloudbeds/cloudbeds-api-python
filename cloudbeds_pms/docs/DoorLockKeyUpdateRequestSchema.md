# DoorLockKeyUpdateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**key_code** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.door_lock_key_update_request_schema import DoorLockKeyUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockKeyUpdateRequestSchema from a JSON string
door_lock_key_update_request_schema_instance = DoorLockKeyUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockKeyUpdateRequestSchema.to_json())

# convert the object into a dict
door_lock_key_update_request_schema_dict = door_lock_key_update_request_schema_instance.to_dict()
# create an instance of DoorLockKeyUpdateRequestSchema from a dict
door_lock_key_update_request_schema_from_dict = DoorLockKeyUpdateRequestSchema.from_dict(door_lock_key_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


