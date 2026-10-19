# GetPaymentScheduleRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | Reservation ID. | 
**skip_payment_processor_check** | **bool** | Skip the payment processor check and return the full theoretical schedule even when the property has no active processor. | [optional] [default to False]

## Example

```python
from cloudbeds_pms.models.get_payment_schedule_request_schema import GetPaymentScheduleRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentScheduleRequestSchema from a JSON string
get_payment_schedule_request_schema_instance = GetPaymentScheduleRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GetPaymentScheduleRequestSchema.to_json())

# convert the object into a dict
get_payment_schedule_request_schema_dict = get_payment_schedule_request_schema_instance.to_dict()
# create an instance of GetPaymentScheduleRequestSchema from a dict
get_payment_schedule_request_schema_from_dict = GetPaymentScheduleRequestSchema.from_dict(get_payment_schedule_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


