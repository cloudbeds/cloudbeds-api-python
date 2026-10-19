# DoorLockKeyBatchDeleteItemSchema

The outcome of invalidating one key in a batch request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** |  | 
**status** | **str** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.door_lock_key_batch_delete_item_schema import DoorLockKeyBatchDeleteItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockKeyBatchDeleteItemSchema from a JSON string
door_lock_key_batch_delete_item_schema_instance = DoorLockKeyBatchDeleteItemSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockKeyBatchDeleteItemSchema.to_json())

# convert the object into a dict
door_lock_key_batch_delete_item_schema_dict = door_lock_key_batch_delete_item_schema_instance.to_dict()
# create an instance of DoorLockKeyBatchDeleteItemSchema from a dict
door_lock_key_batch_delete_item_schema_from_dict = DoorLockKeyBatchDeleteItemSchema.from_dict(door_lock_key_batch_delete_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


