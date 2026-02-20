# PostCreateAllotmentBlockRequestAllotmentIntervalsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_id** | **str** | Policy ID to associate with the interval | [optional] 
**availability** | [**List[PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner]**](PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInner.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_create_allotment_block_request_allotment_intervals_inner import PostCreateAllotmentBlockRequestAllotmentIntervalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockRequestAllotmentIntervalsInner from a JSON string
post_create_allotment_block_request_allotment_intervals_inner_instance = PostCreateAllotmentBlockRequestAllotmentIntervalsInner.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockRequestAllotmentIntervalsInner.to_json())

# convert the object into a dict
post_create_allotment_block_request_allotment_intervals_inner_dict = post_create_allotment_block_request_allotment_intervals_inner_instance.to_dict()
# create an instance of PostCreateAllotmentBlockRequestAllotmentIntervalsInner from a dict
post_create_allotment_block_request_allotment_intervals_inner_from_dict = PostCreateAllotmentBlockRequestAllotmentIntervalsInner.from_dict(post_create_allotment_block_request_allotment_intervals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


