# RatePlanSingleRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Rate Plan ID. | 

## Example

```python
from cloudbeds_pms.models.rate_plan_single_request_schema import RatePlanSingleRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanSingleRequestSchema from a JSON string
rate_plan_single_request_schema_instance = RatePlanSingleRequestSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanSingleRequestSchema.to_json())

# convert the object into a dict
rate_plan_single_request_schema_dict = rate_plan_single_request_schema_instance.to_dict()
# create an instance of RatePlanSingleRequestSchema from a dict
rate_plan_single_request_schema_from_dict = RatePlanSingleRequestSchema.from_dict(rate_plan_single_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


