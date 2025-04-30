# PostPatchGroupResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_code** | **str** | Unique ID for a group | [optional] 
**name** | **str** | The name of the group | [optional] 
**type** | **str** | The type of the group | [optional] 
**status** | **str** | Group status | [optional] 
**created** | **datetime** | Group created time | [optional] 
**source_id** | **str** | The third-party source ID for this group, can be null | [optional] 
**address1** | **str** | Address | [optional] 
**address2** | **str** | Address2 | [optional] 
**city** | **str** | City | [optional] 
**zip** | **str** | Zip | [optional] 
**state** | **str** | State | [optional] 
**id** | **str** | ID | [optional] 
**property_id** | **str** | Property Id | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_patch_group_response_data_inner import PostPatchGroupResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostPatchGroupResponseDataInner from a JSON string
post_patch_group_response_data_inner_instance = PostPatchGroupResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(PostPatchGroupResponseDataInner.to_json())

# convert the object into a dict
post_patch_group_response_data_inner_dict = post_patch_group_response_data_inner_instance.to_dict()
# create an instance of PostPatchGroupResponseDataInner from a dict
post_patch_group_response_data_inner_from_dict = PostPatchGroupResponseDataInner.from_dict(post_patch_group_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


