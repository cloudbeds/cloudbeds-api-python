# SmartPolicyPaymentsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled** | [**List[SmartPolicyPaymentItemSchema]**](SmartPolicyPaymentItemSchema.md) | Smart Policy payments still scheduled for automatic execution, including future authorization holds. | 
**processed** | [**List[SmartPolicyPaymentItemSchema]**](SmartPolicyPaymentItemSchema.md) | Smart Policy payments already executed: successful purchases and captures, plus active authorization holds. | 
**canceled_scheduled** | [**List[SmartPolicyPaymentItemSchema]**](SmartPolicyPaymentItemSchema.md) | Formerly scheduled Smart Policy payments that were canceled (e.g. by turning Smart Policy off). | 
**total_scheduled** | [**MoneySchema**](MoneySchema.md) |  | 
**total_processed** | [**MoneySchema**](MoneySchema.md) |  | 
**total_canceled_scheduled** | [**MoneySchema**](MoneySchema.md) |  | 
**smart_policy_enabled** | **bool** | Whether Smart Policy automation is currently on for the reservation: true while at least one of its rooms still has the policy active, false once it was turned off (or the reservation has no policy rows). | 

## Example

```python
from cloudbeds_pms.models.smart_policy_payments_response_schema import SmartPolicyPaymentsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SmartPolicyPaymentsResponseSchema from a JSON string
smart_policy_payments_response_schema_instance = SmartPolicyPaymentsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(SmartPolicyPaymentsResponseSchema.to_json())

# convert the object into a dict
smart_policy_payments_response_schema_dict = smart_policy_payments_response_schema_instance.to_dict()
# create an instance of SmartPolicyPaymentsResponseSchema from a dict
smart_policy_payments_response_schema_from_dict = SmartPolicyPaymentsResponseSchema.from_dict(smart_policy_payments_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


