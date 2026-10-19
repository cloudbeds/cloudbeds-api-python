# FeeSchema

A fee row applied to a parent object (today: a check line item). Same model as `taxes` — fees are referenced by identifier from the property's configured fees catalog, not by free-text name. The fee is identified by exactly one of `externalId` / `feeId` — sending both or neither is rejected. Multiple fee rows per parent are supported, and each fee can carry its own `taxes[]` for tax-on-fee.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The partner-owned identifier configured on the fee under the property&#39;s fee settings (a 3rd-party reference the property has associated with one of its Cloudbeds fees). Required unless &#x60;feeId&#x60; is sent. Must resolve to an active fee on the property; unknown or inactive values are rejected with FEE_NOT_FOUND. | [optional] 
**fee_id** | **str** | Cloudbeds identifier of the fee, as returned in &#x60;feeID&#x60; by getTaxesAndFees. Required unless &#x60;externalId&#x60; is sent. This identifier is not permanent: when the property edits the fee, Cloudbeds replaces it with a new identifier. A previous identifier is still accepted and is recorded as sent, against the version of the fee it names. A deleted fee is rejected with FEE_NOT_FOUND. Use &#x60;externalId&#x60; when you need a reference that stays the same across edits. | [optional] 
**amount** | **str** | Fee amount applied to this item. Decimal string in major units of the property currency. | 
**taxes** | [**List[TaxSchema]**](TaxSchema.md) | Taxes applied to this fee (tax-on-fee). Each row identifies a configured tax by exactly one of &#x60;externalId&#x60; / &#x60;taxId&#x60;; unmatched values are rejected with TAX_NOT_FOUND. | [optional] 

## Example

```python
from cloudbeds_pms.models.fee_schema import FeeSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FeeSchema from a JSON string
fee_schema_instance = FeeSchema.from_json(json)
# print the JSON string representation of the object
print(FeeSchema.to_json())

# convert the object into a dict
fee_schema_dict = fee_schema_instance.to_dict()
# create an instance of FeeSchema from a dict
fee_schema_from_dict = FeeSchema.from_dict(fee_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


