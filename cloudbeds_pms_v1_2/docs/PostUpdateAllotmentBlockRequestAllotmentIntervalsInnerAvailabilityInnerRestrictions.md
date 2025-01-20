# PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions

Interval restrictions if applicable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_los** | **int** | Minimum length of stay requirement | [optional] 
**max_los** | **int** | Maximum length of stay requirement | [optional] 
**cut_off_days** | **int** | How many days before arrival should guests be required to book | [optional] 
**last_minute_booking_days** | **int** | How many days before the arrival guests are allowed to book | [optional] 
**closed_to_arrival** | **int** | If the interval dates are closed for arrival | [optional] 
**closed_to_departure** | **int** | If the interval dates are closed for departure the number of applicable keys varies here based on the occupancy settings for the room type. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_update_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions import PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions from a JSON string
post_update_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions_instance = PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions.from_json(json)
# print the JSON string representation of the object
print(PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions.to_json())

# convert the object into a dict
post_update_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions_dict = post_update_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions_instance.to_dict()
# create an instance of PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions from a dict
post_update_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions_from_dict = PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions.from_dict(post_update_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


