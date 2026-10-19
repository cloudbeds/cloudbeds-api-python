# AvailabilityUpdatePatchRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **int** | Room Type ID. | 
**intervals** | [**List[PatchIntervalRequestSchema]**](PatchIntervalRequestSchema.md) | Date intervals to adjust. | 

## Example

```python
from cloudbeds_pms.models.availability_update_patch_request_schema import AvailabilityUpdatePatchRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilityUpdatePatchRequestSchema from a JSON string
availability_update_patch_request_schema_instance = AvailabilityUpdatePatchRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AvailabilityUpdatePatchRequestSchema.to_json())

# convert the object into a dict
availability_update_patch_request_schema_dict = availability_update_patch_request_schema_instance.to_dict()
# create an instance of AvailabilityUpdatePatchRequestSchema from a dict
availability_update_patch_request_schema_from_dict = AvailabilityUpdatePatchRequestSchema.from_dict(availability_update_patch_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


