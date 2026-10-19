# ChecklistItemResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The checklist item. | 
**severity** | **str** | The severity actually applied to this item, which is not always the one stored. | 
**severity_is_fixed** | **bool** | True when the severity is a property of the platform rather than a choice. The settings page must not offer a severity control for these items: the value cannot be changed, and showing a control implies otherwise. | 

## Example

```python
from cloudbeds_pms.models.checklist_item_response_schema import ChecklistItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ChecklistItemResponseSchema from a JSON string
checklist_item_response_schema_instance = ChecklistItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ChecklistItemResponseSchema.to_json())

# convert the object into a dict
checklist_item_response_schema_dict = checklist_item_response_schema_instance.to_dict()
# create an instance of ChecklistItemResponseSchema from a dict
checklist_item_response_schema_from_dict = ChecklistItemResponseSchema.from_dict(checklist_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


