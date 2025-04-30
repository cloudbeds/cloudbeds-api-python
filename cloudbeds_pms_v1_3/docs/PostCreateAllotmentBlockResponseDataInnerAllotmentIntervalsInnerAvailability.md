# PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailability

Interval availability data by day in interval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Day within interval | [optional] 
**block_remaining** | **int** | Number of units remaining for the room type for this day | [optional] 
**block_allotted** | **int** | Total number of units available for the room type for this day | [optional] 
**block_confirmed** | **int** | Number of units booked for the room type for this day | [optional] 
**rate** | **str** | the price | [optional] 
**guest_pricing** | [**PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailabilityGuestPricing**](PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailabilityGuestPricing.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_create_allotment_block_response_data_inner_allotment_intervals_inner_availability import PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailability from a JSON string
post_create_allotment_block_response_data_inner_allotment_intervals_inner_availability_instance = PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailability.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailability.to_json())

# convert the object into a dict
post_create_allotment_block_response_data_inner_allotment_intervals_inner_availability_dict = post_create_allotment_block_response_data_inner_allotment_intervals_inner_availability_instance.to_dict()
# create an instance of PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailability from a dict
post_create_allotment_block_response_data_inner_allotment_intervals_inner_availability_from_dict = PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailability.from_dict(post_create_allotment_block_response_data_inner_allotment_intervals_inner_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


