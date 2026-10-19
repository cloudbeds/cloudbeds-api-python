# RatePlanIntervalResponseSchemaAgePolicyPricingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_group_id** | **int** | Age group this price applies to. | 
**is_extra_guests_pricing** | **bool** | True when the price applies to a guest beyond base occupancy rather than to the base rate. | 
**extra_guests_type** | **str** | The property&#39;s extra-guest pricing mode: per_age_group prices every extra guest of a group alike, per_each_guest prices each position separately. | [optional] 
**guest_number** | **int** | Extra-guest position this price applies to, counting from the first guest beyond base occupancy. Only set under per_each_guest pricing. | [optional] 
**days** | [**List[RatePlanIntervalResponseSchemaAgePolicyPricingInnerDaysInner]**](RatePlanIntervalResponseSchemaAgePolicyPricingInnerDaysInner.md) | Price per day-of-week. A day with no price is absent from the list. | 

## Example

```python
from cloudbeds_pms.models.rate_plan_interval_response_schema_age_policy_pricing_inner import RatePlanIntervalResponseSchemaAgePolicyPricingInner

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanIntervalResponseSchemaAgePolicyPricingInner from a JSON string
rate_plan_interval_response_schema_age_policy_pricing_inner_instance = RatePlanIntervalResponseSchemaAgePolicyPricingInner.from_json(json)
# print the JSON string representation of the object
print(RatePlanIntervalResponseSchemaAgePolicyPricingInner.to_json())

# convert the object into a dict
rate_plan_interval_response_schema_age_policy_pricing_inner_dict = rate_plan_interval_response_schema_age_policy_pricing_inner_instance.to_dict()
# create an instance of RatePlanIntervalResponseSchemaAgePolicyPricingInner from a dict
rate_plan_interval_response_schema_age_policy_pricing_inner_from_dict = RatePlanIntervalResponseSchemaAgePolicyPricingInner.from_dict(rate_plan_interval_response_schema_age_policy_pricing_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


