# CalculateTotalsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Echoed from request | 
**net_amount** | [**MoneySchema**](MoneySchema.md) |  | 
**subtotal** | [**MoneySchema**](MoneySchema.md) |  | 
**inclusive_taxes_and_fees** | [**MoneySchema**](MoneySchema.md) |  | 
**exclusive_taxes_and_fees** | [**MoneySchema**](MoneySchema.md) |  | 
**taxes** | [**TaxFeeBreakdownResponseSchema**](TaxFeeBreakdownResponseSchema.md) |  | 
**fees** | [**TaxFeeBreakdownResponseSchema**](TaxFeeBreakdownResponseSchema.md) |  | 
**total** | [**MoneySchema**](MoneySchema.md) |  | 
**convenience_fee** | [**ConvenienceFeeResponseSchema**](ConvenienceFeeResponseSchema.md) |  | [optional] 
**payment_total** | [**MoneySchema**](MoneySchema.md) |  | 
**currency_code** | **str** | ISO 4217 currency code | 
**deposit** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**balance_due** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**default_addons_total** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**requested_addons_total** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**rooms** | [**List[RoomTotalsResponseSchema]**](RoomTotalsResponseSchema.md) | Per-room totals breakdown. Reservation only. | [optional] 

## Example

```python
from cloudbeds_pms.models.calculate_totals_response_schema import CalculateTotalsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateTotalsResponseSchema from a JSON string
calculate_totals_response_schema_instance = CalculateTotalsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(CalculateTotalsResponseSchema.to_json())

# convert the object into a dict
calculate_totals_response_schema_dict = calculate_totals_response_schema_instance.to_dict()
# create an instance of CalculateTotalsResponseSchema from a dict
calculate_totals_response_schema_from_dict = CalculateTotalsResponseSchema.from_dict(calculate_totals_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


