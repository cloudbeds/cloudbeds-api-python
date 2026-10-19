# RatePlanIntervalRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Start date of the interval. | 
**end_date** | **date** | End date of the interval. | 
**name** | **str** | Name of the interval. | 
**room_type_id** | **str** | Room type ID. | [optional] 
**min_los** | **int** | Minimum length of stay. | [optional] 
**max_los** | **int** | Maximum length of stay. | [optional] 
**event_code** | **str** | Event code. | [optional] 
**days** | **Dict[str, float]** | Days of the week pricing (0&#x3D;Sunday, 1&#x3D;Monday, etc.). | [optional] 
**adult_days** | **Dict[str, Dict[str, float]]** | Extra adults pricing (0&#x3D;Sunday, 1&#x3D;Monday, etc.). | [optional] 
**child_days** | **Dict[str, Dict[str, float]]** | Extra children pricing (0&#x3D;Sunday, 1&#x3D;Monday, etc.). | [optional] 
**cut_off** | **int** | Cut-off: minimum number of days in advance a booking must be made. 0 &#x3D; no restriction. | [optional] 
**last_minute_booking** | **int** | Last-minute booking: maximum number of days before arrival a booking may be made. 0 &#x3D; no restriction. | [optional] 
**closed_to_arrival** | **bool** | Closed to arrival: when true, guests cannot start a stay on dates within this interval. | [optional] 
**closed_to_departure** | **bool** | Closed to departure: when true, guests cannot end a stay on dates within this interval. | [optional] 
**limit_to_number_of_rooms** | **int** | Saleable Accommodations: caps how many rooms of the room type this rate may sell. Null, absent or 0 means no limit — the rate may sell the room type&#39;s full capacity. A value above the room type&#39;s capacity is accepted and stored as sent. | [optional] 

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


