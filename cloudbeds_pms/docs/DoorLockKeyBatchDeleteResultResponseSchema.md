# DoorLockKeyBatchDeleteResultResponseSchema

Per-key outcomes for a batch invalidation, one entry per requested key.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[DoorLockKeyBatchDeleteItemSchema]**](DoorLockKeyBatchDeleteItemSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.door_lock_key_batch_delete_result_response_schema import DoorLockKeyBatchDeleteResultResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockKeyBatchDeleteResultResponseSchema from a JSON string
door_lock_key_batch_delete_result_response_schema_instance = DoorLockKeyBatchDeleteResultResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockKeyBatchDeleteResultResponseSchema.to_json())

# convert the object into a dict
door_lock_key_batch_delete_result_response_schema_dict = door_lock_key_batch_delete_result_response_schema_instance.to_dict()
# create an instance of DoorLockKeyBatchDeleteResultResponseSchema from a dict
door_lock_key_batch_delete_result_response_schema_from_dict = DoorLockKeyBatchDeleteResultResponseSchema.from_dict(door_lock_key_batch_delete_result_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


