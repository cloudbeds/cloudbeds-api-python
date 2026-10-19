# ScheduledPaymentDisplayItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formatted_date** | **str** | Payment collection date, formatted for display in the property&#39;s locale. | 
**formatted_amount_with_iso_code** | **str** | Payment amount formatted with the ISO 4217 currency code. | 
**formatted_amount_with_symbol** | **str** | Payment amount formatted with the currency symbol. | 
**type** | **str** | Scheduled payment type. | 

## Example

```python
from cloudbeds_pms.models.scheduled_payment_display_item_schema import ScheduledPaymentDisplayItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ScheduledPaymentDisplayItemSchema from a JSON string
scheduled_payment_display_item_schema_instance = ScheduledPaymentDisplayItemSchema.from_json(json)
# print the JSON string representation of the object
print(ScheduledPaymentDisplayItemSchema.to_json())

# convert the object into a dict
scheduled_payment_display_item_schema_dict = scheduled_payment_display_item_schema_instance.to_dict()
# create an instance of ScheduledPaymentDisplayItemSchema from a dict
scheduled_payment_display_item_schema_from_dict = ScheduledPaymentDisplayItemSchema.from_dict(scheduled_payment_display_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


