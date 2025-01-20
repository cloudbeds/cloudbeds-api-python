# DoorLockKeyCreateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** |  | 
**reservation_id** | **str** | Reservation identifier. | 
**sub_reservation_id** | **str** | Sub-reservation identifier. | 
**issuer_id** | **str** |  | 
**start_date_time** | **str** | Start date and time of key. | 
**end_date_time** | **str** | End date and time of key. | 
**key_type** | **str** | Key type ID. | 
**rooms** | **List[str]** | List of common room IDs. | [optional] [default to []]
**common_rooms** | **List[str]** | List of common room ids. | [optional] [default to []]
**external_id** | **str** |  | [optional] 
**key_code** | **str** | Custom key code. | [optional] 
**status** | **str** | Key status. | [optional] [default to 'processing']
**encoder** | **str** |  | [optional] 
**mobile_id** | **str** |  | [optional] 
**guest_id** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.door_lock_key_create_request_schema import DoorLockKeyCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockKeyCreateRequestSchema from a JSON string
door_lock_key_create_request_schema_instance = DoorLockKeyCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockKeyCreateRequestSchema.to_json())

# convert the object into a dict
door_lock_key_create_request_schema_dict = door_lock_key_create_request_schema_instance.to_dict()
# create an instance of DoorLockKeyCreateRequestSchema from a dict
door_lock_key_create_request_schema_from_dict = DoorLockKeyCreateRequestSchema.from_dict(door_lock_key_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


