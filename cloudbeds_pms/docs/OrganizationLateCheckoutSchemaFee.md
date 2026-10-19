# OrganizationLateCheckoutSchemaFee

Money (amount + currencyCode) when feeType is \"flat\"; a percentage number (e.g. 10 for 10%) when \"percent\".

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount in the smallest representable units of the currency (e.g., cents for USD). For example, USD $124.39 would be \&quot;12439\&quot;. | 
**currency_code** | **str** | ISO 4217 currency code | 

## Example

```python
from cloudbeds_pms.models.organization_late_checkout_schema_fee import OrganizationLateCheckoutSchemaFee

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationLateCheckoutSchemaFee from a JSON string
organization_late_checkout_schema_fee_instance = OrganizationLateCheckoutSchemaFee.from_json(json)
# print the JSON string representation of the object
print(OrganizationLateCheckoutSchemaFee.to_json())

# convert the object into a dict
organization_late_checkout_schema_fee_dict = organization_late_checkout_schema_fee_instance.to_dict()
# create an instance of OrganizationLateCheckoutSchemaFee from a dict
organization_late_checkout_schema_fee_from_dict = OrganizationLateCheckoutSchemaFee.from_dict(organization_late_checkout_schema_fee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


