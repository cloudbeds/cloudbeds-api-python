# PricingDayResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Pricing day ID. | 
**day_of_week** | **int** | Day of week (0&#x3D;Sunday, 6&#x3D;Saturday). | 
**price_amount** | **str** | Price amount, with at least two decimal places and up to four — a price finer than cents keeps the decimals it needs, so do not parse this as a fixed-width two-decimal string. | 
**price_currency** | **str** | ISO 4217 currency code. | 

## Example

```python
from cloudbeds_pms.models.pricing_day_response_schema import PricingDayResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PricingDayResponseSchema from a JSON string
pricing_day_response_schema_instance = PricingDayResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PricingDayResponseSchema.to_json())

# convert the object into a dict
pricing_day_response_schema_dict = pricing_day_response_schema_instance.to_dict()
# create an instance of PricingDayResponseSchema from a dict
pricing_day_response_schema_from_dict = PricingDayResponseSchema.from_dict(pricing_day_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


