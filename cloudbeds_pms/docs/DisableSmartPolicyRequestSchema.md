# DisableSmartPolicyRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | Reservation ID. | 
**trigger** | **str** | What caused the disable. \&quot;manual-action\&quot; marks a side-effect disable (SP-332: manual payment/refund/void/cancel) and skips the override_policy_payment_rules check; absent or \&quot;explicit\&quot; is the deliberate kill-switch and enforces it. | [optional] 

## Example

```python
from cloudbeds_pms.models.disable_smart_policy_request_schema import DisableSmartPolicyRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DisableSmartPolicyRequestSchema from a JSON string
disable_smart_policy_request_schema_instance = DisableSmartPolicyRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DisableSmartPolicyRequestSchema.to_json())

# convert the object into a dict
disable_smart_policy_request_schema_dict = disable_smart_policy_request_schema_instance.to_dict()
# create an instance of DisableSmartPolicyRequestSchema from a dict
disable_smart_policy_request_schema_from_dict = DisableSmartPolicyRequestSchema.from_dict(disable_smart_policy_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


