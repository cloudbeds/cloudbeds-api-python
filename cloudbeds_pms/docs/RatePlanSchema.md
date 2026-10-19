# RatePlanSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_id** | **str** |  | 
**rate_type** | **str** | Rate plan type. | 
**name** | **str** |  | 
**rate_total** | [**MoneySchema**](MoneySchema.md) |  | 
**package_id** | **str** |  | [optional] 
**package_name** | **str** |  | [optional] 
**detailed_rates** | [**List[NightlyRateSchema]**](NightlyRateSchema.md) | Per-night rates for the stay under this plan. | 

## Example

```python
from cloudbeds_pms.models.rate_plan_schema import RatePlanSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanSchema from a JSON string
rate_plan_schema_instance = RatePlanSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanSchema.to_json())

# convert the object into a dict
rate_plan_schema_dict = rate_plan_schema_instance.to_dict()
# create an instance of RatePlanSchema from a dict
rate_plan_schema_from_dict = RatePlanSchema.from_dict(rate_plan_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


