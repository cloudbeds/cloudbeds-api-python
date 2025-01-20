# PostCreateAllotmentBlockResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property ID associated to the allotment block | [optional] 
**allotment_block_code** | **str** | Allotment block code | [optional] 
**allotment_block_status** | **str** | Allotment block status | [optional] 
**allotment_block_name** | **str** | Allotment block name | [optional] 
**allotment_block_id** | **str** | Allotment block ID | [optional] 
**rate_type** | **str** | Rate type for the allotment block | [optional] 
**rate_plan_id** | **str** | Rate plan ID if applicable | [optional] 
**allotment_type** | **str** | the type of allotment block | [optional] 
**group_id** | **str** | Group profile ID associated to the allotment block | [optional] 
**group_code** | **str** | Group profile code associated to the allotment block | [optional] 
**is_auto_release** | **bool** | If the allotment block is configured for auto-release | [optional] 
**auto_release** | [**PostCreateAllotmentBlockResponseDataInnerAutoRelease**](PostCreateAllotmentBlockResponseDataInnerAutoRelease.md) |  | [optional] 
**allotment_intervals** | [**List[PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInner]**](PostCreateAllotmentBlockResponseDataInnerAllotmentIntervalsInner.md) | array of interval data by room type | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_create_allotment_block_response_data_inner import PostCreateAllotmentBlockResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockResponseDataInner from a JSON string
post_create_allotment_block_response_data_inner_instance = PostCreateAllotmentBlockResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockResponseDataInner.to_json())

# convert the object into a dict
post_create_allotment_block_response_data_inner_dict = post_create_allotment_block_response_data_inner_instance.to_dict()
# create an instance of PostCreateAllotmentBlockResponseDataInner from a dict
post_create_allotment_block_response_data_inner_from_dict = PostCreateAllotmentBlockResponseDataInner.from_dict(post_create_allotment_block_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


