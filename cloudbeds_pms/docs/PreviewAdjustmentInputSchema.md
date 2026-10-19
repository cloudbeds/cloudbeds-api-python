# PreviewAdjustmentInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target** | **str** | The type of adjustment to preview. | 
**token** | **str** | Folio adjustment id token, exactly as the save receives it (e.g. &#39;tax_42&#39;, &#39;fee_7&#39;, &#39;rate&#39;, &#39;roomRevenue_manual&#39;). | 
**amount** | [**SmartPolicyMoneyInputSchema**](SmartPolicyMoneyInputSchema.md) |  | 
**booking_room_id** | **str** | Booking room id the adjustment targets (rate / room-revenue). | [optional] 
**rate_source_id** | **str** | Rate source id — required for RATE adjustments to resolve the applicable taxes/fees. | [optional] 
**is_root_source** | **bool** | Whether the rate source is a root source (RATE adjustments). | [optional] 
**is_hotel_collect_booking** | **bool** | Whether the booking is hotel-collect (RATE adjustments). | [optional] 

## Example

```python
from cloudbeds_pms.models.preview_adjustment_input_schema import PreviewAdjustmentInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PreviewAdjustmentInputSchema from a JSON string
preview_adjustment_input_schema_instance = PreviewAdjustmentInputSchema.from_json(json)
# print the JSON string representation of the object
print(PreviewAdjustmentInputSchema.to_json())

# convert the object into a dict
preview_adjustment_input_schema_dict = preview_adjustment_input_schema_instance.to_dict()
# create an instance of PreviewAdjustmentInputSchema from a dict
preview_adjustment_input_schema_from_dict = PreviewAdjustmentInputSchema.from_dict(preview_adjustment_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


