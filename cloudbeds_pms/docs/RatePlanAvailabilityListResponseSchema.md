# RatePlanAvailabilityListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[RatePlanAvailabilityDayResponseSchema]**](RatePlanAvailabilityDayResponseSchema.md) | Per-date stop-sell values for the rate plan / room type(s). | 

## Example

```python
from cloudbeds_pms.models.rate_plan_availability_list_response_schema import RatePlanAvailabilityListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanAvailabilityListResponseSchema from a JSON string
rate_plan_availability_list_response_schema_instance = RatePlanAvailabilityListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanAvailabilityListResponseSchema.to_json())

# convert the object into a dict
rate_plan_availability_list_response_schema_dict = rate_plan_availability_list_response_schema_instance.to_dict()
# create an instance of RatePlanAvailabilityListResponseSchema from a dict
rate_plan_availability_list_response_schema_from_dict = RatePlanAvailabilityListResponseSchema.from_dict(rate_plan_availability_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


