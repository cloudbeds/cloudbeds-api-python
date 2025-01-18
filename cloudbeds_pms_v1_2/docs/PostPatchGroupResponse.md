# PostPatchGroupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success | [optional] 
**data** | [**List[PostPatchGroupResponseDataInner]**](PostPatchGroupResponseDataInner.md) | Data | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_patch_group_response import PostPatchGroupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostPatchGroupResponse from a JSON string
post_patch_group_response_instance = PostPatchGroupResponse.from_json(json)
# print the JSON string representation of the object
print(PostPatchGroupResponse.to_json())

# convert the object into a dict
post_patch_group_response_dict = post_patch_group_response_instance.to_dict()
# create an instance of PostPatchGroupResponse from a dict
post_patch_group_response_from_dict = PostPatchGroupResponse.from_dict(post_patch_group_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


