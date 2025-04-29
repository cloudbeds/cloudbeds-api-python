# GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Day within interval | [optional] 
**block_remaining** | **int** | Number of units remaining for the room type for this day | [optional] 
**block_allotted** | **int** | Total number of units available for the room type for this day | [optional] 
**block_confirmed** | **int** | Number of units booked for the room type for this day | [optional] 
**rate** | **str** | the price | [optional] 
**guest_pricing** | [**PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailabilityGuestPricing**](PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailabilityGuestPricing.md) |  | [optional] 
**split_block_allotted** | **int** | Number of split units available for the room type this day | [optional] 
**split_block_confirmed** | **int** | Number of split units blocked for the room type this day | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_allotment_blocks_response_data_inner_allotment_intervals_inner_availability_inner import GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner from a JSON string
get_allotment_blocks_response_data_inner_allotment_intervals_inner_availability_inner_instance = GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner.from_json(json)
# print the JSON string representation of the object
print(GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner.to_json())

# convert the object into a dict
get_allotment_blocks_response_data_inner_allotment_intervals_inner_availability_inner_dict = get_allotment_blocks_response_data_inner_allotment_intervals_inner_availability_inner_instance.to_dict()
# create an instance of GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner from a dict
get_allotment_blocks_response_data_inner_allotment_intervals_inner_availability_inner_from_dict = GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner.from_dict(get_allotment_blocks_response_data_inner_allotment_intervals_inner_availability_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


