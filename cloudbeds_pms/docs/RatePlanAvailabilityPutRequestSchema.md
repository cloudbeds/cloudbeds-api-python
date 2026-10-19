# RatePlanAvailabilityPutRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RatePlanStopSellUpdateSchema]**](RatePlanStopSellUpdateSchema.md) | Stop-sell updates per rate plan / room type. | 
**test_request** | **bool** | Mark as test request (honored in non-production only). | [optional] 

## Example

```python
from cloudbeds_pms.models.rate_plan_availability_put_request_schema import RatePlanAvailabilityPutRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanAvailabilityPutRequestSchema from a JSON string
rate_plan_availability_put_request_schema_instance = RatePlanAvailabilityPutRequestSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanAvailabilityPutRequestSchema.to_json())

# convert the object into a dict
rate_plan_availability_put_request_schema_dict = rate_plan_availability_put_request_schema_instance.to_dict()
# create an instance of RatePlanAvailabilityPutRequestSchema from a dict
rate_plan_availability_put_request_schema_from_dict = RatePlanAvailabilityPutRequestSchema.from_dict(rate_plan_availability_put_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


