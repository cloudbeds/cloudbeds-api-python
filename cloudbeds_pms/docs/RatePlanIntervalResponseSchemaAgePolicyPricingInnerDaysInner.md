# RatePlanIntervalResponseSchemaAgePolicyPricingInnerDaysInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day_of_week** | **int** | 0&#x3D;Sunday … 6&#x3D;Saturday. | 
**price_amount** | **str** | Decimal amount, with at least two decimal places and up to four — a price finer than cents keeps the decimals it needs, so do not parse this as a fixed-width two-decimal string. | 
**price_currency** | **str** | ISO 4217 currency code. | 

## Example

```python
from cloudbeds_pms.models.rate_plan_interval_response_schema_age_policy_pricing_inner_days_inner import RatePlanIntervalResponseSchemaAgePolicyPricingInnerDaysInner

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanIntervalResponseSchemaAgePolicyPricingInnerDaysInner from a JSON string
rate_plan_interval_response_schema_age_policy_pricing_inner_days_inner_instance = RatePlanIntervalResponseSchemaAgePolicyPricingInnerDaysInner.from_json(json)
# print the JSON string representation of the object
print(RatePlanIntervalResponseSchemaAgePolicyPricingInnerDaysInner.to_json())

# convert the object into a dict
rate_plan_interval_response_schema_age_policy_pricing_inner_days_inner_dict = rate_plan_interval_response_schema_age_policy_pricing_inner_days_inner_instance.to_dict()
# create an instance of RatePlanIntervalResponseSchemaAgePolicyPricingInnerDaysInner from a dict
rate_plan_interval_response_schema_age_policy_pricing_inner_days_inner_from_dict = RatePlanIntervalResponseSchemaAgePolicyPricingInnerDaysInner.from_dict(rate_plan_interval_response_schema_age_policy_pricing_inner_days_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


