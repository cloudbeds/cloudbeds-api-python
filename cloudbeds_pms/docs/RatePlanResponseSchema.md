# RatePlanResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
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
**policy_id** | **int** |  | [optional] 

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


