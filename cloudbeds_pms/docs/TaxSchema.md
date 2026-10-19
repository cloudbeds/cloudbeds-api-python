# TaxSchema

A tax row applied to a gratuity, an item, or a service charge. Multiple tax rows per parent object are supported. The tax is identified by exactly one of `externalId` / `taxId` — sending both or neither is rejected.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_id** | **str** | The partner-owned identifier configured on the tax under the property&#39;s tax settings (a 3rd-party reference the property has associated with one of its Cloudbeds taxes). Required unless &#x60;taxId&#x60; is sent. Must resolve to an active tax on the property; unknown or inactive values are rejected with TAX_NOT_FOUND. | [optional] 
**tax_id** | **str** | Cloudbeds identifier of the tax, as returned in &#x60;taxID&#x60; by getTaxesAndFees. Required unless &#x60;externalId&#x60; is sent. This identifier is not permanent: when the property edits the tax, Cloudbeds replaces it with a new identifier. A previous identifier is still accepted and is recorded as sent, against the version of the tax it names. A deleted tax is rejected with TAX_NOT_FOUND. Use &#x60;externalId&#x60; when you need a reference that stays the same across edits. | [optional] 
**amount** | **str** | Tax amount applied to the parent object — item, fee, service charge or gratuity, whichever this row is nested under. Decimal string in major units of the property currency. | 

## Example

```python
from cloudbeds_pms.models.tax_schema import TaxSchema

# TODO update the JSON string below
json = "{}"
# create an instance of TaxSchema from a JSON string
tax_schema_instance = TaxSchema.from_json(json)
# print the JSON string representation of the object
print(TaxSchema.to_json())

# convert the object into a dict
tax_schema_dict = tax_schema_instance.to_dict()
# create an instance of TaxSchema from a dict
tax_schema_from_dict = TaxSchema.from_dict(tax_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


