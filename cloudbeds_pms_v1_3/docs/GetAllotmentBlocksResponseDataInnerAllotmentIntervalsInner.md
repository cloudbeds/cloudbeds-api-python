# GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | Policy ID associated with the interval | [optional] 
**room_type_id** | **str** | Room type ID | [optional] 
**rate_id** | **str** | Rate ID of the block rate for this room type (the &#x60;rateID&#x60; carried by rooms on the block&#39;s reservations) | [optional] 
**start_date** | **date** | Interval start date | [optional] 
**end_date** | **date** | Interval end date | [optional] 
**availability** | [**List[GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner]**](GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner.md) | Interval availability data by day in interval | [optional] 
**restrictions** | [**GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerRestrictions**](GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerRestrictions.md) |  | [optional] 
**split_inventory** | **bool** | Whether split inventory is enabled for this room type. When true, the linked physical room types are individually bookable within the allotment block, with their availability drawn from the allotment capacity of this room type. | [optional] 
**shoulder_dates_before** | **int** | Number of shoulder days before the event start date. | [optional] 
**shoulder_dates_after** | **int** | Number of shoulder days after the event end date. | [optional] 
**shoulder_dates_rate_id** | **str** | Rate plan ID applied during shoulder date periods. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_allotment_blocks_response_data_inner_allotment_intervals_inner import GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner from a JSON string
get_allotment_blocks_response_data_inner_allotment_intervals_inner_instance = GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner.from_json(json)
# print the JSON string representation of the object
print(GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner.to_json())

# convert the object into a dict
get_allotment_blocks_response_data_inner_allotment_intervals_inner_dict = get_allotment_blocks_response_data_inner_allotment_intervals_inner_instance.to_dict()
# create an instance of GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner from a dict
get_allotment_blocks_response_data_inner_allotment_intervals_inner_from_dict = GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner.from_dict(get_allotment_blocks_response_data_inner_allotment_intervals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


