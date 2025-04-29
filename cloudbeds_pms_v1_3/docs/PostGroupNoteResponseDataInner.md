# PostGroupNoteResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID for the note | [optional] 
**group_profile_id** | **str** | Group profile ID | [optional] 
**text** | **str** | Note text | [optional] 
**created_by** | **str** | Created by | [optional] 
**created_at** | **str** | Created at | [optional] 
**updated_at** | **str** | Updated at | [optional] 
**archived** | **str** | Note archived | [optional] 
**archived_at** | **str** | Note archived at | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_group_note_response_data_inner import PostGroupNoteResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostGroupNoteResponseDataInner from a JSON string
post_group_note_response_data_inner_instance = PostGroupNoteResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(PostGroupNoteResponseDataInner.to_json())

# convert the object into a dict
post_group_note_response_data_inner_dict = post_group_note_response_data_inner_instance.to_dict()
# create an instance of PostGroupNoteResponseDataInner from a dict
post_group_note_response_data_inner_from_dict = PostGroupNoteResponseDataInner.from_dict(post_group_note_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


