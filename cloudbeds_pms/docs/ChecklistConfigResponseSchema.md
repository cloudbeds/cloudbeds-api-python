# ChecklistConfigResponseSchema

A property's check-in checklist configuration, as the platform applies it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_configured** | **bool** | False when the property has no checklist at all, which is the default and the behaviour that predates the feature. Both item lists are then empty. | 
**check_in** | [**List[ChecklistItemResponseSchema]**](ChecklistItemResponseSchema.md) | Items guarding check-in, in display order. | 
**check_out** | [**List[ChecklistItemResponseSchema]**](ChecklistItemResponseSchema.md) | Items guarding check-out, in display order. | 

## Example

```python
from cloudbeds_pms.models.checklist_config_response_schema import ChecklistConfigResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistConfigResponseSchema from a JSON string
checklist_config_response_schema_instance = ChecklistConfigResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ChecklistConfigResponseSchema.to_json())

# convert the object into a dict
checklist_config_response_schema_dict = checklist_config_response_schema_instance.to_dict()
# create an instance of ChecklistConfigResponseSchema from a dict
checklist_config_response_schema_from_dict = ChecklistConfigResponseSchema.from_dict(checklist_config_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


