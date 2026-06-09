# PostUpdateAllotmentBlockRequestAllotmentIntervalsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | Policy ID to associate with the interval | [optional] 
**split_inventory** | **bool** | Enables split inventory for this virtual room type. When true, the linked physical room types become individually bookable within the allotment block, with their availability drawn from the allotment capacity of this room type. If omitted, the existing value is preserved. Must be explicitly set to true when adding a virtual room type via updateAllotmentBlock. | [optional] 
**room_type_id** | **str** | Room type id | [optional] 
**availability** | [**List[PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner]**](PostUpdateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner.md) | Interval availability data by day in interval | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_update_allotment_block_request_allotment_intervals_inner import PostUpdateAllotmentBlockRequestAllotmentIntervalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostUpdateAllotmentBlockRequestAllotmentIntervalsInner from a JSON string
post_update_allotment_block_request_allotment_intervals_inner_instance = PostUpdateAllotmentBlockRequestAllotmentIntervalsInner.from_json(json)
# print the JSON string representation of the object
print(PostUpdateAllotmentBlockRequestAllotmentIntervalsInner.to_json())

# convert the object into a dict
post_update_allotment_block_request_allotment_intervals_inner_dict = post_update_allotment_block_request_allotment_intervals_inner_instance.to_dict()
# create an instance of PostUpdateAllotmentBlockRequestAllotmentIntervalsInner from a dict
post_update_allotment_block_request_allotment_intervals_inner_from_dict = PostUpdateAllotmentBlockRequestAllotmentIntervalsInner.from_dict(post_update_allotment_block_request_allotment_intervals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


