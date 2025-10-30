# RatePlanUpdateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Rate Plan ID. | 
**is_active** | **bool** | Whether the rate plan is active. | [optional] 
**promo_code** | **str** | Promotional code for the rate plan. | [optional] [default to 'true']
**sources** | **List[str]** | List of sources for the rate plan. | [optional] 
**derived_value** | **float** | Value for the derived rate plan. | [optional] [default to 0]
**derived_rate_plan_id** | **int** | Derived rate plan ID. | [optional] 
**derived_type** | **str** | Rate plan derived type. | [optional] [default to 'fixed']
**name** | **Dict[str, str]** | Name in multiple languages. | [optional] 
**description** | **Dict[str, str]** | Description in multiple languages. | [optional] 
**name_private** | **Dict[str, str]** | Internal name in multiple languages. | [optional] 
**terms** | **Dict[str, str]** | Terms and conditions in multiple languages. | [optional] 
**addons** | [**List[RatePlanAddonRequestSchema]**](RatePlanAddonRequestSchema.md) | List of addons for the rate plan. | [optional] 

## Example

```python
from cloudbeds_pms.models.rate_plan_update_request_schema import RatePlanUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanUpdateRequestSchema from a JSON string
rate_plan_update_request_schema_instance = RatePlanUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanUpdateRequestSchema.to_json())

# convert the object into a dict
rate_plan_update_request_schema_dict = rate_plan_update_request_schema_instance.to_dict()
# create an instance of RatePlanUpdateRequestSchema from a dict
rate_plan_update_request_schema_from_dict = RatePlanUpdateRequestSchema.from_dict(rate_plan_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


