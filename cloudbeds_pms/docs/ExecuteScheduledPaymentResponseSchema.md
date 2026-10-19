# ExecuteScheduledPaymentResponseSchema

Response envelope for a successful execute-scheduled-payment outcome.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**ExecuteScheduledPaymentDataSchema**](ExecuteScheduledPaymentDataSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.execute_scheduled_payment_response_schema import ExecuteScheduledPaymentResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteScheduledPaymentResponseSchema from a JSON string
execute_scheduled_payment_response_schema_instance = ExecuteScheduledPaymentResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ExecuteScheduledPaymentResponseSchema.to_json())

# convert the object into a dict
execute_scheduled_payment_response_schema_dict = execute_scheduled_payment_response_schema_instance.to_dict()
# create an instance of ExecuteScheduledPaymentResponseSchema from a dict
execute_scheduled_payment_response_schema_from_dict = ExecuteScheduledPaymentResponseSchema.from_dict(execute_scheduled_payment_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


