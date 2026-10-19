# CheckTotalsSchema

Partner-supplied check totals broken out by component. Used for two purposes: (1) totals-only postings — when items[] is empty, totalItems carries the items subtotal and the server posts a single synthetic items folio line; inline serviceCharge / discounts[] continue to write their own rows; (2) cross-validation — when items[] is also supplied, each total field cross-validates against the corresponding server-computed sum (items / SC / gratuity / discount / tax / fees). Mismatches surface as INVALID_TOTAL_MISMATCH with the failing component identified. totalTax / totalFee are cross-cutting aggregates: in items mode they cross-validate the sum across the whole check; in totals-only mode the partner amount routes to the per-property \"Default POS tax\" / \"Default POS fee\" catch-all catalog records (lazy-created), keeping the ledger invariant that every tax_id / fee_id reference resolves to a real row.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **str** | Items subtotal. Per item: amount + its taxes[] + its fees[] + the taxes on those fees — the nested fee-tax term is the one most often left out. When items[] is supplied alongside, this value must equal the server-computed subtotal within 1 minor unit per currency; a larger difference is rejected with INVALID_TOTAL_MISMATCH. When an item carries a discount this figure is the amount BEFORE that discount — the comparison runs on the items as sent, and the discount is applied afterwards, so a 20.00 item with a 5.00 discount is declared as 20.00 and posts 15.00. When items[] is empty, this is the gross figure the single synthesised line carries. Not a grand total — service charge, gratuity and discount have their own fields below. | 
**total_service_charge** | **str** | Service-charge subtotal — serviceCharge.amount + sum(serviceCharge.taxes). Optional; cross-validates against the inline serviceCharge data ONLY when both are supplied. In totals-only mode without inline serviceCharge, this value is the partner-declared SC aggregate (validation deferred to the persistence layer). | [optional] 
**total_gratuity** | **str** | Gratuity subtotal — sum(gratuities[].amount + gratuities[].taxes). Optional; accepted on the wire but server-side validation is deferred until the embedded-gratuity domain handling lands (today gratuities are accepted but not mapped to the domain payload). | [optional] 
**total_discount** | **str** | Discount subtotal — sum(discounts[].amount), partner-supplied as a positive value. Optional; cross-validates against the inline discounts[] ONLY when both are supplied. In totals-only mode without inline discounts, this value is the partner-declared discount aggregate. | [optional] 
**total_tax** | **str** | Total tax across the check — sum of every tax line (items[].taxes, items[].fees[].taxes, serviceCharge.taxes, gratuities[].taxes). Optional. When items[] is supplied, the partner value cross-validates against the server-computed sum (INVALID_TOTAL_MISMATCH on drift). In totals-only mode (items[] empty), the partner value is persisted as a single tax line on the synthetic POS-sale item, linked to the property&#39;s lazily-created \&quot;Default POS tax\&quot; catalog record. Zero or omitted skips the synthesis. | [optional] 
**total_fee** | **str** | Total fees across the check — sum of items[].fees[].amount. Fees only attach to items in the postCheck data model, so the sum is items-scoped. Optional. Same items-mode cross-validation and totals-only synthesis semantics as totalTax, routed through the property&#39;s \&quot;Default POS fee\&quot; catalog record. Zero or omitted skips the synthesis. | [optional] 

## Example

```python
from cloudbeds_pms.models.check_totals_schema import CheckTotalsSchema

# TODO update the JSON string below
json = "{}"
# create an instance of CheckTotalsSchema from a JSON string
check_totals_schema_instance = CheckTotalsSchema.from_json(json)
# print the JSON string representation of the object
print(CheckTotalsSchema.to_json())

# convert the object into a dict
check_totals_schema_dict = check_totals_schema_instance.to_dict()
# create an instance of CheckTotalsSchema from a dict
check_totals_schema_from_dict = CheckTotalsSchema.from_dict(check_totals_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


