# GratuitySchema

A single tip entry. Recipient is optional; absent recipient is allowed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Gratuity amount in the property currency. Must be &gt; 0; corrections require void + repost (negative amounts rejected). | 
**taxes** | [**List[TaxSchema]**](TaxSchema.md) | Optional tax rows applied to this gratuity. Each tax follows the item-tax pattern — identify the tax by exactly one of &#x60;externalId&#x60; / &#x60;taxId&#x60;; an unmatched value returns TAX_NOT_FOUND. | [optional] 
**note** | **str** | Free-text label displayed on the folio line item. | [optional] 
**custom_transaction_code** | **str** | Override the property default Custom Transaction Code for this posting. | [optional] 
**general_ledger_custom_code** | **str** | Override the property default GL custom code for this posting. | [optional] 
**sub_reservation_id** | **str** | Sub-reservation identifier. If provided, this gratuity entry is routed to the specified sub-reservation within the parent reservation (request-level reservationId). Has no effect when the request-level target is houseAccountId or eventCode. | [optional] 
**recipient** | [**RecipientSchema**](RecipientSchema.md) |  | [optional] 
**gratuity_id** | **str** | Optional partner-supplied public handle for this gratuity (accept-or-generate). When omitted, Cloudbeds generates one and returns it. Must be a non-empty string containing only letters, digits, and . _ ~ -, unique among active (non-voided) gratuities on the property; reusable after this gratuity is voided. Used to address the gratuity for void (DELETE /folio/v1/gratuities/{gratuityId}). | [optional] 

## Example

```python
from cloudbeds_pms.models.gratuity_schema import GratuitySchema

# TODO update the JSON string below
json = "{}"
# create an instance of GratuitySchema from a JSON string
gratuity_schema_instance = GratuitySchema.from_json(json)
# print the JSON string representation of the object
print(GratuitySchema.to_json())

# convert the object into a dict
gratuity_schema_dict = gratuity_schema_instance.to_dict()
# create an instance of GratuitySchema from a dict
gratuity_schema_from_dict = GratuitySchema.from_dict(gratuity_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


