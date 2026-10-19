# PricingCreateRequestSchemaPricingInnerDaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | **int** | Day of week (0&#x3D;Sunday, 6&#x3D;Saturday). | 
**price_amount** | **str** | Price amount: a non-negative amount with at most 24 integer digits and 4 decimal places. | 
**price_currency** | **str** | ISO 4217 currency code. | 

## Example

```python
from cloudbeds_pms.models.pricing_create_request_schema_pricing_inner_days_inner import PricingCreateRequestSchemaPricingInnerDaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of PricingCreateRequestSchemaPricingInnerDaysInner from a JSON string
pricing_create_request_schema_pricing_inner_days_inner_instance = PricingCreateRequestSchemaPricingInnerDaysInner.from_json(json)
# print the JSON string representation of the object
print(PricingCreateRequestSchemaPricingInnerDaysInner.to_json())

# convert the object into a dict
pricing_create_request_schema_pricing_inner_days_inner_dict = pricing_create_request_schema_pricing_inner_days_inner_instance.to_dict()
# create an instance of PricingCreateRequestSchemaPricingInnerDaysInner from a dict
pricing_create_request_schema_pricing_inner_days_inner_from_dict = PricingCreateRequestSchemaPricingInnerDaysInner.from_dict(pricing_create_request_schema_pricing_inner_days_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


