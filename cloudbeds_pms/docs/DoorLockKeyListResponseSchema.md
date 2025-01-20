# DoorLockKeyListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[List[DoorLockKeyResponseSchema]]** |  | 

## Example

```python
from cloudbeds_pms.models.door_lock_key_list_response_schema import DoorLockKeyListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockKeyListResponseSchema from a JSON string
door_lock_key_list_response_schema_instance = DoorLockKeyListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockKeyListResponseSchema.to_json())

# convert the object into a dict
door_lock_key_list_response_schema_dict = door_lock_key_list_response_schema_instance.to_dict()
# create an instance of DoorLockKeyListResponseSchema from a dict
door_lock_key_list_response_schema_from_dict = DoorLockKeyListResponseSchema.from_dict(door_lock_key_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


