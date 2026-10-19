# RatePlanStopSellUpdateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_plan_id** | **int** | Rate Plan ID (the rate plan package id). | 
**room_type_id** | **int** | Room Type ID. | 
**intervals** | [**List[StopSellIntervalSchema]**](StopSellIntervalSchema.md) | Date intervals to set stop-sell for. | 

## Example

```python
from cloudbeds_pms.models.rate_plan_stop_sell_update_schema import RatePlanStopSellUpdateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RatePlanStopSellUpdateSchema from a JSON string
rate_plan_stop_sell_update_schema_instance = RatePlanStopSellUpdateSchema.from_json(json)
# print the JSON string representation of the object
print(RatePlanStopSellUpdateSchema.to_json())

# convert the object into a dict
rate_plan_stop_sell_update_schema_dict = rate_plan_stop_sell_update_schema_instance.to_dict()
# create an instance of RatePlanStopSellUpdateSchema from a dict
rate_plan_stop_sell_update_schema_from_dict = RatePlanStopSellUpdateSchema.from_dict(rate_plan_stop_sell_update_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


