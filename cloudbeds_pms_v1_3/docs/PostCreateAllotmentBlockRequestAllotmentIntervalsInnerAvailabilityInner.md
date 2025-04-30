# PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | the day within the interval (YYYY-MM-DD) | [optional] 
**block_allotted** | **int** | Total number of units available for the | [optional] 
**rate** | **str** | the price if applicable | [optional] 
**guest_pricing** | [**PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing**](PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing.md) |  | [optional] 
**restrictions** | [**PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions**](PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_create_allotment_block_request_allotment_intervals_inner_availability_inner import PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner from a JSON string
post_create_allotment_block_request_allotment_intervals_inner_availability_inner_instance = PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner.to_json())

# convert the object into a dict
post_create_allotment_block_request_allotment_intervals_inner_availability_inner_dict = post_create_allotment_block_request_allotment_intervals_inner_availability_inner_instance.to_dict()
# create an instance of PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner from a dict
post_create_allotment_block_request_allotment_intervals_inner_availability_inner_from_dict = PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner.from_dict(post_create_allotment_block_request_allotment_intervals_inner_availability_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


