# ExecuteScheduledPaymentDataSchema

Payload of a successful execute-scheduled-payment outcome.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_status** | **str** | The persisted payment status after dispatch (successful | failed | canceled | scheduled). Null only when the dispatch was not attempted (e.g. notYetDue with no prior status). | 
**already_processed** | **bool** | True when the persisted payment was already in a terminal state and the dispatch was a no-op idempotent retry. | 
**error_message** | **str** | Human-readable gateway error detail when paymentStatus&#x3D;\&quot;failed\&quot;; null otherwise. | [optional] 

## Example

```python
from cloudbeds_pms.models.execute_scheduled_payment_data_schema import ExecuteScheduledPaymentDataSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ExecuteScheduledPaymentDataSchema from a JSON string
execute_scheduled_payment_data_schema_instance = ExecuteScheduledPaymentDataSchema.from_json(json)
# print the JSON string representation of the object
print(ExecuteScheduledPaymentDataSchema.to_json())

# convert the object into a dict
execute_scheduled_payment_data_schema_dict = execute_scheduled_payment_data_schema_instance.to_dict()
# create an instance of ExecuteScheduledPaymentDataSchema from a dict
execute_scheduled_payment_data_schema_from_dict = ExecuteScheduledPaymentDataSchema.from_dict(execute_scheduled_payment_data_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


