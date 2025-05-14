# PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions

Interval restrictions if applicable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_los** | **int** | Minimum length of stay requirement | [optional] 
**max_los** | **int** | Maximum length of stay requirement | [optional] 
**cut_off_days** | **int** | How many days before arrival should guests be required to book | [optional] 
**last_minute_booking_days** | **int** | How many days before the arrival guests are allowed to book | [optional] 
**closed_to_arrival** | **int** | If the interval dates are closed for arrival | [optional] 
**closed_to_departure** | **int** | If the interval dates are closed for departure | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_create_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions import PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions from a JSON string
post_create_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions_instance = PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions.to_json())

# convert the object into a dict
post_create_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions_dict = post_create_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions_instance.to_dict()
# create an instance of PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions from a dict
post_create_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions_from_dict = PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerRestrictions.from_dict(post_create_allotment_block_request_allotment_intervals_inner_availability_inner_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


