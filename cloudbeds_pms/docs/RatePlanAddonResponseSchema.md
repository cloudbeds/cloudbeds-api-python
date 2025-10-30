# RatePlanAddonResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**addon_id** | **str** |  | 
**settings** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.rate_plan_addon_response_schema import RatePlanAddonResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanAddonResponseSchema from a JSON string
rate_plan_addon_response_schema_instance = RatePlanAddonResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanAddonResponseSchema.to_json())

# convert the object into a dict
rate_plan_addon_response_schema_dict = rate_plan_addon_response_schema_instance.to_dict()
# create an instance of RatePlanAddonResponseSchema from a dict
rate_plan_addon_response_schema_from_dict = RatePlanAddonResponseSchema.from_dict(rate_plan_addon_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


