# GetAllotmentBlocksResponseDataInner


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
**auto_release** | [**List[GetAllotmentBlocksResponseDataInnerAutoReleaseInner]**](GetAllotmentBlocksResponseDataInnerAutoReleaseInner.md) | auto-release data if applicable | [optional] 
**allotment_intervals** | [**List[GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner]**](GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInner.md) | array of interval data by room type | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_allotment_blocks_response_data_inner import GetAllotmentBlocksResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllotmentBlocksResponseDataInner from a JSON string
get_allotment_blocks_response_data_inner_instance = GetAllotmentBlocksResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetAllotmentBlocksResponseDataInner.to_json())

# convert the object into a dict
get_allotment_blocks_response_data_inner_dict = get_allotment_blocks_response_data_inner_instance.to_dict()
# create an instance of GetAllotmentBlocksResponseDataInner from a dict
get_allotment_blocks_response_data_inner_from_dict = GetAllotmentBlocksResponseDataInner.from_dict(get_allotment_blocks_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


