# RatePlanResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**property_id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**status** | **str** | Derived from isActive and the intervals&#39; end dates, using the property&#39;s current date. &#x60;disabled&#x60;: isActive is false. &#x60;no-intervals&#x60;: active with no intervals. &#x60;expired&#x60;: active and every interval&#39;s endDate is in the past. &#x60;active&#x60;: active with at least one interval whose endDate is today or later (or has no endDate). | [optional] 
**is_deleted** | **bool** |  | [optional] 
**derived_rate_plan_id** | **str** |  | [optional] 
**is_derived** | **bool** |  | [optional] 
**derived_type** | **str** |  | [optional] 
**derived_value** | **float** |  | [optional] 
**addons** | [**List[RatePlanAddonResponseSchema]**](RatePlanAddonResponseSchema.md) |  | [optional] 
**promo_code** | **str** |  | [optional] 
**sources** | **List[str]** |  | [optional] 
**name** | **Dict[str, str]** |  | [optional] 
**description** | **Dict[str, str]** |  | [optional] 
**name_private** | **Dict[str, str]** |  | [optional] 
**terms** | **Dict[str, str]** |  | [optional] 
**intervals** | [**List[RatePlanIntervalResponseSchema]**](RatePlanIntervalResponseSchema.md) |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**policy_id** | **str** |  | [optional] 
**segment_id** | **str** |  | [optional] 
**meal_plans** | **List[str]** | Meal plans carried by the add-ons listed in &#x60;addons&#x60; (any attachment setting), as raw keys (not localized labels), deduplicated. Empty when none of them is a meal plan. | 

## Example

```python
from cloudbeds_pms.models.rate_plan_response_schema import RatePlanResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanResponseSchema from a JSON string
rate_plan_response_schema_instance = RatePlanResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanResponseSchema.to_json())

# convert the object into a dict
rate_plan_response_schema_dict = rate_plan_response_schema_instance.to_dict()
# create an instance of RatePlanResponseSchema from a dict
rate_plan_response_schema_from_dict = RatePlanResponseSchema.from_dict(rate_plan_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


