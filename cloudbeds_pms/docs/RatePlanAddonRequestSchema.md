# RatePlanAddonRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**addon_id** | **str** | The addon ID. | 
**settings** | **str** | The addon settings. | 

## Example

```python
from cloudbeds_pms.models.rate_plan_addon_request_schema import RatePlanAddonRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanAddonRequestSchema from a JSON string
rate_plan_addon_request_schema_instance = RatePlanAddonRequestSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanAddonRequestSchema.to_json())

# convert the object into a dict
rate_plan_addon_request_schema_dict = rate_plan_addon_request_schema_instance.to_dict()
# create an instance of RatePlanAddonRequestSchema from a dict
rate_plan_addon_request_schema_from_dict = RatePlanAddonRequestSchema.from_dict(rate_plan_addon_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


