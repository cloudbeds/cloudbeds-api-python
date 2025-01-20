# PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing

Guest pricing data if applicable. Note: the number of applicable keys varies here based on the occupancy settings for the room type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**adult1** | **str** | Price for adult 1 | [optional] 
**adult2** | **str** | Price for adult 2 | [optional] 
**adult3** | **str** | Price for adult 3 | [optional] 
**child1** | **str** | Price for child 1 | [optional] 
**child2** | **str** | Price for child 2 | [optional] 
**child3** | **str** | Price for child 3 | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_create_allotment_block_request_allotment_intervals_inner_availability_inner_guest_pricing import PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing from a JSON string
post_create_allotment_block_request_allotment_intervals_inner_availability_inner_guest_pricing_instance = PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing.to_json())

# convert the object into a dict
post_create_allotment_block_request_allotment_intervals_inner_availability_inner_guest_pricing_dict = post_create_allotment_block_request_allotment_intervals_inner_availability_inner_guest_pricing_instance.to_dict()
# create an instance of PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing from a dict
post_create_allotment_block_request_allotment_intervals_inner_availability_inner_guest_pricing_from_dict = PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing.from_dict(post_create_allotment_block_request_allotment_intervals_inner_availability_inner_guest_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


