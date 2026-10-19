# CheckItemRequestSchema

A single line on a POS check. Shared envelope fields — externalLineId, name, quantity, price, amount, taxes, fees, note, customTransactionCode, generalLedgerCustomCode — describe the line. quantity is the unit count; price, when supplied, is the per-unit rate but is informational metadata only. The `details` block is polymorphic: its concrete shape is selected by the `type` discriminator. Today only PRODUCT is accepted, so `details` carries product-specific fields (sku, category, sub-reservation routing). Bookable-resource details will land alongside as a second `oneOf` branch when that flow is reintroduced. amount is the financial source of truth — the server posts it verbatim without recomputing from price * quantity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Discriminator selecting the kind of line — see CheckItemTypeEnum. | 
**name** | **str** | Human-readable line name displayed on the folio (dish or beverage name). | 
**external_line_id** | **str** | Optional partner-supplied identifier for this line occurrence on the check (the POS system&#39;s own line reference — e.g., Clover lineItem.id, Toast Selection.guid, Square line uid, or a per-check line sequence). Per line, not per unit: a quantity-2 line carries one reference. When provided, must be unique within this check&#39;s items[]; a duplicate is rejected with DUPLICATE_EXTERNAL_LINE_ID. When omitted, the line is stored with no reference — Cloudbeds does not generate one. Supplied values are echoed back on the response and on line events so the partner can correlate the posted line without storing any Cloudbeds identifier. | [optional] 
**quantity** | **int** | Number of units. Informational metadata only — not used for accounting math (amount is the line total, not price * quantity). | 
**price** | **str** | Per-unit price. Optional informational metadata — recorded on the folio for display and reporting; not used for accounting math. amount is the financial source of truth for this line; when price is omitted, amount is used as the per-unit price on the folio row. Decimal string in major units of the property currency. | [optional] 
**amount** | **str** | Total line amount — the financial source of truth for this line. The server posts this value to the folio without recomputing it from price * quantity. Decimal string in major units of the property currency. | 
**note** | **str** | Optional free-text note for this line (modifier, allergen, special request). | [optional] 
**custom_transaction_code** | **str** | Custom Transaction Code (chart-of-accounts mapping) snapshotted onto the folio transaction at posting time. If omitted, the property&#39;s default mapping is applied. | [optional] 
**general_ledger_custom_code** | **str** | General Ledger custom code, snapshotted onto the folio transaction at posting time. If omitted, the property&#39;s default mapping is applied. | [optional] 
**taxes** | [**List[TaxSchema]**](TaxSchema.md) | Tax rows for this line. Each row identifies a configured tax by exactly one of &#x60;externalId&#x60; / &#x60;taxId&#x60;; unmatched values are rejected. | [optional] 
**fees** | [**List[FeeSchema]**](FeeSchema.md) | Fee amounts for this line. Each row identifies a configured fee by exactly one of &#x60;externalId&#x60; / &#x60;feeId&#x60;; unmatched values are rejected. | [optional] 
**discounts** | [**List[CheckItemDiscountRequestSchema]**](CheckItemDiscountRequestSchema.md) | Discounts applied to this line. The line&#39;s amount is reduced by their total and each is appended to the line&#39;s note; they do not post separate negative lines. A discount covering the whole check belongs in the check-level &#x60;discounts[]&#x60;. | [optional] 
**details** | [**ProductDetailsSchema**](ProductDetailsSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.check_item_request_schema import CheckItemRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CheckItemRequestSchema from a JSON string
check_item_request_schema_instance = CheckItemRequestSchema.from_json(json)
# print the JSON string representation of the object
print(CheckItemRequestSchema.to_json())

# convert the object into a dict
check_item_request_schema_dict = check_item_request_schema_instance.to_dict()
# create an instance of CheckItemRequestSchema from a dict
check_item_request_schema_from_dict = CheckItemRequestSchema.from_dict(check_item_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


