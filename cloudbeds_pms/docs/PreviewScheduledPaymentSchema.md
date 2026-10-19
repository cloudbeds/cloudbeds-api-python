# PreviewScheduledPaymentSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**original_amount** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**new_amount** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**status** | **str** | Status of the scheduled payment after the adjustment. | [optional] 

## Example

```python
from cloudbeds_pms.models.preview_scheduled_payment_schema import PreviewScheduledPaymentSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewScheduledPaymentSchema from a JSON string
preview_scheduled_payment_schema_instance = PreviewScheduledPaymentSchema.from_json(json)
# print the JSON string representation of the object
print(PreviewScheduledPaymentSchema.to_json())

# convert the object into a dict
preview_scheduled_payment_schema_dict = preview_scheduled_payment_schema_instance.to_dict()
# create an instance of PreviewScheduledPaymentSchema from a dict
preview_scheduled_payment_schema_from_dict = PreviewScheduledPaymentSchema.from_dict(preview_scheduled_payment_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


