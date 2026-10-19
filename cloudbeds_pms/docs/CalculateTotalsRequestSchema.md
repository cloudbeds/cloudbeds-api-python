# CalculateTotalsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Entity type. Determines the calculation strategy. | 
**taxes_and_fees** | [**List[TaxFeeConfigSchema]**](TaxFeeConfigSchema.md) | Array of tax/fee configuration objects. Can be empty. | 
**convenience_fee_config** | [**ConvenienceFeeConfigSchema**](ConvenienceFeeConfigSchema.md) |  | [optional] 
**var_date** | **str** | Calculation date (YYYY-MM-DD). Used for context and monitoring. Defaults to current date. | [optional] 
**rounding_method** | **int** | Rounding method. 0 &#x3D; legacy (default), 1 &#x3D; item-level rounding. | [optional] 
**exclusive_taxes_on_total** | **bool** | Whether exclusive taxes are calculated on the net rate (after inclusive extraction). Defaults to true. | [optional] 
**amount** | [**MoneyInputSchema**](MoneyInputSchema.md) |  | [optional] 
**adults** | **int** | Number of adults. Used by fixed_per_person. Defaults to 1. | [optional] 
**children** | **int** | Number of children. Used by fixed_per_person. Defaults to 0. | [optional] 
**nights** | **int** | Number of nights. Used by fixed_per_person, fixed_per_accommodation. Defaults to 1. | [optional] 
**accommodations** | **int** | Number of accommodations. Used by fixed_per_accommodation. Defaults to 1. | [optional] 
**rooms** | [**List[RoomSchema]**](RoomSchema.md) | Room configurations. Required for reservation type. Must be null (not empty array) for entity types. | [optional] 
**currency_code** | **str** | ISO 4217 currency code. Required for reservation type. For entity types, derived from amount.currencyCode. | [optional] 
**deposit_config** | [**DepositConfigSchema**](DepositConfigSchema.md) |  | [optional] 
**allotment_block_code** | **str** | Allotment block code. Reservation type only. | [optional] 

## Example

```python
from cloudbeds_pms.models.calculate_totals_request_schema import CalculateTotalsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CalculateTotalsRequestSchema from a JSON string
calculate_totals_request_schema_instance = CalculateTotalsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(CalculateTotalsRequestSchema.to_json())

# convert the object into a dict
calculate_totals_request_schema_dict = calculate_totals_request_schema_instance.to_dict()
# create an instance of CalculateTotalsRequestSchema from a dict
calculate_totals_request_schema_from_dict = CalculateTotalsRequestSchema.from_dict(calculate_totals_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


