# SmartPolicyPaymentItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | Payment ID. | 
**amount** | [**MoneySchema**](MoneySchema.md) |  | 
**card_type** | **str** | Card brand when the payment is card-backed. | 
**card_last4** | **str** | Last 4 digits of the card when the payment is card-backed. | 
**created_at** | **str** | Payment creation datetime in the property&#39;s local time (Y-m-d H:i:s). | 
**scheduled_for** | **str** | When the payment is or was scheduled to be collected, property-local (Y-m-d H:i:s). | 
**transaction_type** | **str** | Transaction type (Purchase, Authorize, or Capture). | 

## Example

```python
from cloudbeds_pms.models.smart_policy_payment_item_schema import SmartPolicyPaymentItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SmartPolicyPaymentItemSchema from a JSON string
smart_policy_payment_item_schema_instance = SmartPolicyPaymentItemSchema.from_json(json)
# print the JSON string representation of the object
print(SmartPolicyPaymentItemSchema.to_json())

# convert the object into a dict
smart_policy_payment_item_schema_dict = smart_policy_payment_item_schema_instance.to_dict()
# create an instance of SmartPolicyPaymentItemSchema from a dict
smart_policy_payment_item_schema_from_dict = SmartPolicyPaymentItemSchema.from_dict(smart_policy_payment_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


