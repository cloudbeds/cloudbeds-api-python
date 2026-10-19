# PolicySummaryRowSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timing_label** | **str** | When the row applies, as display copy. | 
**action_copy** | **str** | What happens at that time, as display copy. | 
**detail** | **str** | Additional detail for the row; null when there is none. | [optional] 
**anchor** | **str** | Machine-readable anchor the timing is relative to; null when not applicable. | [optional] 
**anchor_offset_minutes** | **int** | Offset from the anchor in minutes; null when not applicable. | [optional] 
**date_time** | **datetime** | Resolved ISO 8601 datetime for the row; null when not resolvable. | [optional] 

## Example

```python
from cloudbeds_pms.models.policy_summary_row_schema import PolicySummaryRowSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicySummaryRowSchema from a JSON string
policy_summary_row_schema_instance = PolicySummaryRowSchema.from_json(json)
# print the JSON string representation of the object
print(PolicySummaryRowSchema.to_json())

# convert the object into a dict
policy_summary_row_schema_dict = policy_summary_row_schema_instance.to_dict()
# create an instance of PolicySummaryRowSchema from a dict
policy_summary_row_schema_from_dict = PolicySummaryRowSchema.from_dict(policy_summary_row_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


