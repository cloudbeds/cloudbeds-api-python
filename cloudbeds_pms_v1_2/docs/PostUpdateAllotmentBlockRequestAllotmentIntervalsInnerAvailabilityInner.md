# PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**block_allotted** | **int** | Total number of units available for the room type for this day | [optional] 
**var_date** | **date** | the day within the interval (YYYY-MM-DD) | [optional] 
**rate** | **str** | the price if applicable | [optional] 
**guest_pricing** | [**PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing**](PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing.md) |  | [optional] 
**restrictions** | [**PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions**](PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_update_allotment_block_request_allotment_intervals_inner_availability_inner import PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner from a JSON string
post_update_allotment_block_request_allotment_intervals_inner_availability_inner_instance = PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner.from_json(json)
# print the JSON string representation of the object
print(PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner.to_json())

# convert the object into a dict
post_update_allotment_block_request_allotment_intervals_inner_availability_inner_dict = post_update_allotment_block_request_allotment_intervals_inner_availability_inner_instance.to_dict()
# create an instance of PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner from a dict
post_update_allotment_block_request_allotment_intervals_inner_availability_inner_from_dict = PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner.from_dict(post_update_allotment_block_request_allotment_intervals_inner_availability_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


