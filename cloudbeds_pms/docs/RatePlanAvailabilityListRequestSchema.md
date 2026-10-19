# RatePlanAvailabilityListRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_plan_id** | **int** | Rate Plan ID (the rate plan package id). | 
**room_type_id** | **int** | Optional Room Type ID filter; omit to return all room types of the rate plan. | [optional] 
**start_date** | **str** | Start date (YYYY-MM-DD). | 
**end_date** | **str** | End date (YYYY-MM-DD), inclusive. The range may span at most 366 days. | 

## Example

```python
from cloudbeds_pms.models.rate_plan_availability_list_request_schema import RatePlanAvailabilityListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanAvailabilityListRequestSchema from a JSON string
rate_plan_availability_list_request_schema_instance = RatePlanAvailabilityListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanAvailabilityListRequestSchema.to_json())

# convert the object into a dict
rate_plan_availability_list_request_schema_dict = rate_plan_availability_list_request_schema_instance.to_dict()
# create an instance of RatePlanAvailabilityListRequestSchema from a dict
rate_plan_availability_list_request_schema_from_dict = RatePlanAvailabilityListRequestSchema.from_dict(rate_plan_availability_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


