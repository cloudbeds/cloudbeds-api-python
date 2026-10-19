# PaymentScheduleResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payments** | [**List[ScheduledPaymentItemSchema]**](ScheduledPaymentItemSchema.md) | Scheduled payments (deposit and installments) for the reservation. | 
**degraded** | **bool** | True when the schedule calculation failed and the result is degraded (partial or unavailable), as opposed to a legitimately empty schedule. Consumers must treat a degraded empty result differently from a genuine \&quot;no payments owed\&quot;. | 

## Example

```python
from cloudbeds_pms.models.payment_schedule_response_schema import PaymentScheduleResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentScheduleResponseSchema from a JSON string
payment_schedule_response_schema_instance = PaymentScheduleResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PaymentScheduleResponseSchema.to_json())

# convert the object into a dict
payment_schedule_response_schema_dict = payment_schedule_response_schema_instance.to_dict()
# create an instance of PaymentScheduleResponseSchema from a dict
payment_schedule_response_schema_from_dict = PaymentScheduleResponseSchema.from_dict(payment_schedule_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


