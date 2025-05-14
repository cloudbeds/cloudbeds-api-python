# DoorLockKeyResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** |  | 
**property_id** | **str** |  | 
**reservation_id** | **str** |  | 
**sub_reservation_id** | **str** |  | 
**issuer_id** | **str** |  | 
**guest_id** | **str** |  | [optional] 
**rooms** | **List[str]** |  | 
**common_rooms** | **List[str]** |  | 
**start_date_time** | **str** |  | 
**end_date_time** | **str** |  | 
**encoder** | **str** |  | [optional] 
**key_code** | **str** |  | [optional] 
**key_type** | **str** |  | 
**mobile_id** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**status** | **str** |  | 
**error_message** | **str** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.door_lock_key_response_schema import DoorLockKeyResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockKeyResponseSchema from a JSON string
door_lock_key_response_schema_instance = DoorLockKeyResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockKeyResponseSchema.to_json())

# convert the object into a dict
door_lock_key_response_schema_dict = door_lock_key_response_schema_instance.to_dict()
# create an instance of DoorLockKeyResponseSchema from a dict
door_lock_key_response_schema_from_dict = DoorLockKeyResponseSchema.from_dict(door_lock_key_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


