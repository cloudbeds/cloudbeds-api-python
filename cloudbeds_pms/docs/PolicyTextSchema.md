# PolicyTextSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Smart policy ID; null when the text comes from the legacy policy fallback. | 
**name** | **str** | Smart policy name; null when the text comes from the legacy policy fallback. | 
**root_id** | **str** | Root ID of the smart policy version chain; null when the text comes from the legacy policy fallback. | 
**guarantee_text** | **str** | Human-readable guarantee / payment policy text; empty when the text comes from the legacy policy fallback (which only provides cancellation text). | 
**cancellation_text** | **str** | Human-readable cancellation policy text. | 
**no_show_text** | **str** | Human-readable no-show policy text; empty when the policy has none. | 
**additional_policy_text** | **str** | Additional free-form policy text configured by the property; empty when none. | 
**cancellation_type** | [**PolicyCancellationTypeSchema**](PolicyCancellationTypeSchema.md) |  | [optional] 
**payment_summary_rows** | [**List[PolicySummaryRowSchema]**](PolicySummaryRowSchema.md) | Payment milestone rows for timeline display; null when not available. | [optional] 
**cancellation_summary_rows** | [**List[PolicySummaryRowSchema]**](PolicySummaryRowSchema.md) | Cancellation milestone rows for timeline display; null when not available. | [optional] 
**no_show_summary_rows** | [**List[PolicySummaryRowSchema]**](PolicySummaryRowSchema.md) | No-show milestone rows for timeline display; null when not available. | [optional] 

## Example

```python
from cloudbeds_pms.models.policy_text_schema import PolicyTextSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyTextSchema from a JSON string
policy_text_schema_instance = PolicyTextSchema.from_json(json)
# print the JSON string representation of the object
print(PolicyTextSchema.to_json())

# convert the object into a dict
policy_text_schema_dict = policy_text_schema_instance.to_dict()
# create an instance of PolicyTextSchema from a dict
policy_text_schema_from_dict = PolicyTextSchema.from_dict(policy_text_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


