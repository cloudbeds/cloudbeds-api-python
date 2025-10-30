# RatePlanCreateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_active** | **bool** | The status of the rate plan. | 
**room_type_id** | **int** | The room type ID assigned to this rate plan. | 
**name** | **Dict[str, str]** | Name in multiple languages. | 
**description** | **Dict[str, str]** | Description in multiple languages. | 
**name_private** | **Dict[str, str]** | Internal name in multiple languages. | 
**allotment_block_id** | **str** | The allotment block&#39;s ID this rate belongs to. | [optional] 
**promo_code** | **str** | Promotional code for the rate plan. | [optional] 
**sources** | **List[str]** | List of sources for the rate plan. | [optional] 
**derived_value** | **float** | Value for the derived rate plan. | [optional] [default to 0]
**derived_rate_plan_id** | **int** | Derived rate plan ID. | [optional] 
**derived_type** | **str** | Rate plan derived type. | [optional] [default to 'fixed']
**terms** | **Dict[str, str]** | Terms and conditions in multiple languages. | [optional] 
**intervals** | [**List[RatePlanIntervalRequestSchema]**](RatePlanIntervalRequestSchema.md) | List of rate plan intervals. | [optional] 
**addons** | [**List[RatePlanAddonRequestSchema]**](RatePlanAddonRequestSchema.md) | List of addons. | [optional] 

## Example

```python
from cloudbeds_pms.models.rate_plan_create_request_schema import RatePlanCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanCreateRequestSchema from a JSON string
rate_plan_create_request_schema_instance = RatePlanCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanCreateRequestSchema.to_json())

# convert the object into a dict
rate_plan_create_request_schema_dict = rate_plan_create_request_schema_instance.to_dict()
# create an instance of RatePlanCreateRequestSchema from a dict
rate_plan_create_request_schema_from_dict = RatePlanCreateRequestSchema.from_dict(rate_plan_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


