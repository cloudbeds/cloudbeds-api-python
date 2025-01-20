# GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Room type ID | [optional] 
**start_date** | **date** | Interval start date | [optional] 
**end_date** | **date** | Interval end date | [optional] 
**availability** | [**List[GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner]**](GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerAvailabilityInner.md) | Interval availability data by day in interval | [optional] 
**restrictions** | [**GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerRestrictions**](GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerRestrictions.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_allotment_blocks_response_data_inner_allotment_intervals_inner import GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner

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


