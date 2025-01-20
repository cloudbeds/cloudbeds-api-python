# DoorLockKeyListRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** |  | [optional] 
**sub_reservation_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.door_lock_key_list_request_schema import DoorLockKeyListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockKeyListRequestSchema from a JSON string
door_lock_key_list_request_schema_instance = DoorLockKeyListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockKeyListRequestSchema.to_json())

# convert the object into a dict
door_lock_key_list_request_schema_dict = door_lock_key_list_request_schema_instance.to_dict()
# create an instance of DoorLockKeyListRequestSchema from a dict
door_lock_key_list_request_schema_from_dict = DoorLockKeyListRequestSchema.from_dict(door_lock_key_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


