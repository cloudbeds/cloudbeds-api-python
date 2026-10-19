# RatePlanIntervalResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**rate_plan_id** | **int** |  | 
**room_type_id** | **int** |  | 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**min_los** | **int** |  | [optional] 
**max_los** | **int** |  | [optional] 
**days** | **List[Optional[float]]** | Base price per day-of-week, indexed 0&#x3D;Sunday … 6&#x3D;Saturday. A day with no base price is null. | 
**adult_days** | **Dict[str, Dict[str, float]]** | Extra adults pricing. Outer key &#x3D; day-of-week (0&#x3D;Sunday … 6&#x3D;Saturday); inner key &#x3D; extra-guest count; value &#x3D; additional price for that guest. Note: when fees are set on a contiguous run of days starting at day 0 (e.g. all 7 days), the payload serializes as a JSON array of per-day objects rather than the day-of-week-keyed object shown here. | [optional] 
**child_days** | **Dict[str, Dict[str, float]]** | Extra children pricing. Outer key &#x3D; day-of-week (0&#x3D;Sunday … 6&#x3D;Saturday); inner key &#x3D; extra-guest count; value &#x3D; additional price for that guest. Note: when fees are set on a contiguous run of days starting at day 0 (e.g. all 7 days), the payload serializes as a JSON array of per-day objects rather than the day-of-week-keyed object shown here. | [optional] 
**cut_off** | **int** | Cut-off: minimum number of days in advance a booking must be made. 0 &#x3D; no restriction. | [optional] 
**last_minute_booking** | **int** | Last-minute booking: maximum number of days before arrival a booking may be made. 0 &#x3D; no restriction. | [optional] 
**closed_to_arrival** | **bool** | Closed to arrival: when true, guests cannot start a stay on dates within this interval. | [optional] 
**closed_to_departure** | **bool** | Closed to departure: when true, guests cannot end a stay on dates within this interval. | [optional] 
**limit_to_number_of_rooms** | **int** | Saleable Accommodations: caps how many rooms of the room type this rate may sell. Null means no limit — the rate may sell the room type&#39;s full capacity. | [optional] 
**age_policy_pricing** | [**List[RatePlanIntervalResponseSchemaAgePolicyPricingInner]**](RatePlanIntervalResponseSchemaAgePolicyPricingInner.md) | Age-group pricing for this interval, one entry per priced age group — or, under per_each_guest pricing, one entry per extra-guest position within a group, so several entries can share an ageGroupId and differ by guestNumber. Null when the property does not use age-group pricing, or when this interval&#39;s rate still prices guests with the adultDays / childDays model — in which case those two fields carry the pricing. An empty array means age-group pricing applies to this interval but nothing is priced on it yet. Infant groups are absent while infant support is off for the property. Join ageGroupId against GET /age-policy/v1/policies for each group&#39;s name and age range. | [optional] 

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


