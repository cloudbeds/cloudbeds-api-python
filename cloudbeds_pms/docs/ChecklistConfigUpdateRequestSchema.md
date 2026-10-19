# ChecklistConfigUpdateRequestSchema

A full replacement of the property's check-in checklist configuration. A replace rather than a patch, because the order of the items is part of the configuration. Sending both stages empty removes the configuration, leaving the property with no checklist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_in** | **List[object]** | Items guarding check-in, in the order they should appear. | 
**check_out** | **List[object]** | Items guarding check-out, in the order they should appear. | 

## Example

```python
from cloudbeds_pms.models.checklist_config_update_request_schema import ChecklistConfigUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistConfigUpdateRequestSchema from a JSON string
checklist_config_update_request_schema_instance = ChecklistConfigUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ChecklistConfigUpdateRequestSchema.to_json())

# convert the object into a dict
checklist_config_update_request_schema_dict = checklist_config_update_request_schema_instance.to_dict()
# create an instance of ChecklistConfigUpdateRequestSchema from a dict
checklist_config_update_request_schema_from_dict = ChecklistConfigUpdateRequestSchema.from_dict(checklist_config_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


