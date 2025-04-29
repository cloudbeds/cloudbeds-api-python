# PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Room type ID | [optional] 
**start_date** | **date** | Interval start date | [optional] 
**end_date** | **date** | Interval end date | [optional] 
**availability** | [**PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailability**](PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerAvailability.md) |  | [optional] 
**restrictions** | [**PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerRestrictions**](PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInnerRestrictions.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_create_allotment_block_response_data_inner_allotment_intervals_inner import PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInner from a JSON string
post_create_allotment_block_response_data_inner_allotment_intervals_inner_instance = PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInner.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInner.to_json())

# convert the object into a dict
post_create_allotment_block_response_data_inner_allotment_intervals_inner_dict = post_create_allotment_block_response_data_inner_allotment_intervals_inner_instance.to_dict()
# create an instance of PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInner from a dict
post_create_allotment_block_response_data_inner_allotment_intervals_inner_from_dict = PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInner.from_dict(post_create_allotment_block_response_data_inner_allotment_intervals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


