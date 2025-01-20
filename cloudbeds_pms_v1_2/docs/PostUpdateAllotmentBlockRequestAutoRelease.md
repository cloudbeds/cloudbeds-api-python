# PostUpdateAllotmentBlockRequestAutoRelease

Optional auto-release configuration NOTE: pass empty object to remove auto-release configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_type** | **str** | The type of auto-release | [optional] 
**days** | **int** | The number of days prior to the end of the allotment block to begin releasing dates from the allotment block | [optional] 
**release_time** | **str** | The hour to being the auto-release in HH:00 format, e.g. &#39;00:00&#39;, &#39;01:00&#39;... | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_update_allotment_block_request_auto_release import PostUpdateAllotmentBlockRequestAutoRelease

# TODO update the JSON string below
json = "{}"
# create an instance of PostUpdateAllotmentBlockRequestAutoRelease from a JSON string
post_update_allotment_block_request_auto_release_instance = PostUpdateAllotmentBlockRequestAutoRelease.from_json(json)
# print the JSON string representation of the object
print(PostUpdateAllotmentBlockRequestAutoRelease.to_json())

# convert the object into a dict
post_update_allotment_block_request_auto_release_dict = post_update_allotment_block_request_auto_release_instance.to_dict()
# create an instance of PostUpdateAllotmentBlockRequestAutoRelease from a dict
post_update_allotment_block_request_auto_release_from_dict = PostUpdateAllotmentBlockRequestAutoRelease.from_dict(post_update_allotment_block_request_auto_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


