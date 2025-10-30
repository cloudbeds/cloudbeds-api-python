# RatePlanIntervalRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date of the interval. | 
**end_date** | **date** | End date of the interval. | 
**name** | **str** | Name of the interval. | 
**room_type_id** | **str** | Room type ID. | [optional] 
**min_overlap** | **int** | Minimum overlap. | [optional] 
**max_overlap** | **int** | Maximum overlap. | [optional] 
**group_code** | **str** | Group code. | [optional] 
**days** | **Dict[str, float]** | Days of the week pricing (0&#x3D;Sunday, 1&#x3D;Monday, etc.). | [optional] 
**adult_days** | **Dict[str, Dict[str, float]]** | Extra adults pricing (0&#x3D;Sunday, 1&#x3D;Monday, etc.). | [optional] 
**child_days** | **Dict[str, Dict[str, float]]** | Extra children pricing (0&#x3D;Sunday, 1&#x3D;Monday, etc.). | [optional] 

## Example

```python
from cloudbeds_pms.models.rate_plan_interval_request_schema import RatePlanIntervalRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanIntervalRequestSchema from a JSON string
rate_plan_interval_request_schema_instance = RatePlanIntervalRequestSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanIntervalRequestSchema.to_json())

# convert the object into a dict
rate_plan_interval_request_schema_dict = rate_plan_interval_request_schema_instance.to_dict()
# create an instance of RatePlanIntervalRequestSchema from a dict
rate_plan_interval_request_schema_from_dict = RatePlanIntervalRequestSchema.from_dict(rate_plan_interval_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


