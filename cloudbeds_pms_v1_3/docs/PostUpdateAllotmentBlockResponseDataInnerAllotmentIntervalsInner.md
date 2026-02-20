# PostUpdateAllotmentBlockResponseDataInnerAllotmentIntervalsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | Policy ID associated with the interval | [optional] 
**room_type_id** | **str** | Room type ID | [optional] 
**availability** | [**PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailability**](PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailability.md) |  | [optional] 
**restrictions** | [**PostUpdateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerRestrictions**](PostUpdateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerRestrictions.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_update_allotment_block_response_data_inner_allotment_intervals_inner import PostUpdateAllotmentBlockResponseDataInnerAllotmentIntervalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostUpdateAllotmentBlockResponseDataInnerAllotmentIntervalsInner from a JSON string
post_update_allotment_block_response_data_inner_allotment_intervals_inner_instance = PostUpdateAllotmentBlockResponseDataInnerAllotmentIntervalsInner.from_json(json)
# print the JSON string representation of the object
print(PostUpdateAllotmentBlockResponseDataInnerAllotmentIntervalsInner.to_json())

# convert the object into a dict
post_update_allotment_block_response_data_inner_allotment_intervals_inner_dict = post_update_allotment_block_response_data_inner_allotment_intervals_inner_instance.to_dict()
# create an instance of PostUpdateAllotmentBlockResponseDataInnerAllotmentIntervalsInner from a dict
post_update_allotment_block_response_data_inner_allotment_intervals_inner_from_dict = PostUpdateAllotmentBlockResponseDataInnerAllotmentIntervalsInner.from_dict(post_update_allotment_block_response_data_inner_allotment_intervals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


