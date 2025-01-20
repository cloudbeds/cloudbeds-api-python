# PostCreateAllotmentBlockResponseDataInnerAutoRelease

auto-release data if applicable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_type** | **str** | The type of auto-release | [optional] 
**days** | **int** | The number of days prior to the end of the allotment block to begin releasing dates from the allotment block | [optional] 
**release_time** | **str** | The hour to being the auto-release in HH:00 format, e.g. &#39;00:00&#39;, &#39;01:00&#39;... | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_create_allotment_block_response_data_inner_auto_release import PostCreateAllotmentBlockResponseDataInnerAutoRelease

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockResponseDataInnerAutoRelease from a JSON string
post_create_allotment_block_response_data_inner_auto_release_instance = PostCreateAllotmentBlockResponseDataInnerAutoRelease.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockResponseDataInnerAutoRelease.to_json())

# convert the object into a dict
post_create_allotment_block_response_data_inner_auto_release_dict = post_create_allotment_block_response_data_inner_auto_release_instance.to_dict()
# create an instance of PostCreateAllotmentBlockResponseDataInnerAutoRelease from a dict
post_create_allotment_block_response_data_inner_auto_release_from_dict = PostCreateAllotmentBlockResponseDataInnerAutoRelease.from_dict(post_create_allotment_block_response_data_inner_auto_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


