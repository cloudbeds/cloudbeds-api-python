# DoorLockKeyInvalidationTimeoutResponseSchema

INT-4076: separate schema for the \"no partner response yet\" case so the FE axios transient-retry interceptor treats it as a retryable network transient (504 is in TRANSIENT_STATUS_CODES) and re-issues the DELETE — effectively extending the wait while the partner is still working. Distinct from DoorLockKeyFailedToInvalidateResponseSchema (422), which is the terminal \"partner reported failure\" response that the FE surfaces to the user without retrying.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.door_lock_key_invalidation_timeout_response_schema import DoorLockKeyInvalidationTimeoutResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DoorLockKeyInvalidationTimeoutResponseSchema from a JSON string
door_lock_key_invalidation_timeout_response_schema_instance = DoorLockKeyInvalidationTimeoutResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DoorLockKeyInvalidationTimeoutResponseSchema.to_json())

# convert the object into a dict
door_lock_key_invalidation_timeout_response_schema_dict = door_lock_key_invalidation_timeout_response_schema_instance.to_dict()
# create an instance of DoorLockKeyInvalidationTimeoutResponseSchema from a dict
door_lock_key_invalidation_timeout_response_schema_from_dict = DoorLockKeyInvalidationTimeoutResponseSchema.from_dict(door_lock_key_invalidation_timeout_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


