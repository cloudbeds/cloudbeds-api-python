# GetAllotmentBlocksResponseDataInnerAutoReleaseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_type** | **str** | The type of auto-release | [optional] 
**days** | **int** | The number of days prior to the end of the allotment block to begin releasing dates from the allotment block | [optional] 
**release_time** | **str** | The hour to being the auto-release in HH:00 format, e.g. &#39;00:00&#39;, &#39;01:00&#39;... | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_allotment_blocks_response_data_inner_auto_release_inner import GetAllotmentBlocksResponseDataInnerAutoReleaseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllotmentBlocksResponseDataInnerAutoReleaseInner from a JSON string
get_allotment_blocks_response_data_inner_auto_release_inner_instance = GetAllotmentBlocksResponseDataInnerAutoReleaseInner.from_json(json)
# print the JSON string representation of the object
print(GetAllotmentBlocksResponseDataInnerAutoReleaseInner.to_json())

# convert the object into a dict
get_allotment_blocks_response_data_inner_auto_release_inner_dict = get_allotment_blocks_response_data_inner_auto_release_inner_instance.to_dict()
# create an instance of GetAllotmentBlocksResponseDataInnerAutoReleaseInner from a dict
get_allotment_blocks_response_data_inner_auto_release_inner_from_dict = GetAllotmentBlocksResponseDataInnerAutoReleaseInner.from_dict(get_allotment_blocks_response_data_inner_auto_release_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


