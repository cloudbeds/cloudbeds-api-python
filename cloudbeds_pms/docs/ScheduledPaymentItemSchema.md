# ScheduledPaymentItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_ids** | **List[str]** | Identifiers of the actions covered by this scheduled payment. | 
**timestamp** | **datetime** | When the payment is scheduled to be collected; null when not yet determined. | 
**amount** | **int** | Payment amount in minor units. | 
**currency** | **str** | ISO 4217 currency code. | 
**order_id** | **str** | Order identifier the payment belongs to. | 
**is_initial_deposit** | **bool** | Whether this payment is the initial deposit. | 

## Example

```python
from cloudbeds_pms.models.scheduled_payment_item_schema import ScheduledPaymentItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledPaymentItemSchema from a JSON string
scheduled_payment_item_schema_instance = ScheduledPaymentItemSchema.from_json(json)
# print the JSON string representation of the object
print(ScheduledPaymentItemSchema.to_json())

# convert the object into a dict
scheduled_payment_item_schema_dict = scheduled_payment_item_schema_instance.to_dict()
# create an instance of ScheduledPaymentItemSchema from a dict
scheduled_payment_item_schema_from_dict = ScheduledPaymentItemSchema.from_dict(scheduled_payment_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


