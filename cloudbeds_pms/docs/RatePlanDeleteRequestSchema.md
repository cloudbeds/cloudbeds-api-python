# RatePlanDeleteRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Rate Plan ID. | 

## Example

```python
from cloudbeds_pms.models.rate_plan_delete_request_schema import RatePlanDeleteRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanDeleteRequestSchema from a JSON string
rate_plan_delete_request_schema_instance = RatePlanDeleteRequestSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanDeleteRequestSchema.to_json())

# convert the object into a dict
rate_plan_delete_request_schema_dict = rate_plan_delete_request_schema_instance.to_dict()
# create an instance of RatePlanDeleteRequestSchema from a dict
rate_plan_delete_request_schema_from_dict = RatePlanDeleteRequestSchema.from_dict(rate_plan_delete_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


