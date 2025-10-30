# RatePlanIntervalResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**rate_plan_id** | **int** |  | 
**room_type_id** | **int** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**min_overlap** | **int** |  | [optional] 
**max_overlap** | **int** |  | [optional] 
**days** | **object** |  | 
**adult_days** | **Dict[str, Dict[str, float]]** | Extra adults pricing (0&#x3D;Sunday, 1&#x3D;Monday, etc.). | [optional] 
**child_days** | **Dict[str, Dict[str, float]]** | Extra children pricing (0&#x3D;Sunday, 1&#x3D;Monday, etc.). | [optional] 

## Example

```python
from cloudbeds_pms.models.rate_plan_interval_response_schema import RatePlanIntervalResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanIntervalResponseSchema from a JSON string
rate_plan_interval_response_schema_instance = RatePlanIntervalResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanIntervalResponseSchema.to_json())

# convert the object into a dict
rate_plan_interval_response_schema_dict = rate_plan_interval_response_schema_instance.to_dict()
# create an instance of RatePlanIntervalResponseSchema from a dict
rate_plan_interval_response_schema_from_dict = RatePlanIntervalResponseSchema.from_dict(rate_plan_interval_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


