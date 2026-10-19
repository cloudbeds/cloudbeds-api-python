# PreviewAdjustmentResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result_type** | **str** | The outcome of the adjustment preview. | [optional] 
**new_reservation_total** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**already_paid** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**refund_required** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**scheduled_payments** | [**List[PreviewScheduledPaymentSchema]**](PreviewScheduledPaymentSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.preview_adjustment_response_schema import PreviewAdjustmentResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewAdjustmentResponseSchema from a JSON string
preview_adjustment_response_schema_instance = PreviewAdjustmentResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PreviewAdjustmentResponseSchema.to_json())

# convert the object into a dict
preview_adjustment_response_schema_dict = preview_adjustment_response_schema_instance.to_dict()
# create an instance of PreviewAdjustmentResponseSchema from a dict
preview_adjustment_response_schema_from_dict = PreviewAdjustmentResponseSchema.from_dict(preview_adjustment_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


