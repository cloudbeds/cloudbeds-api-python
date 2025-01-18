# PostGroupNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success | [optional] 
**code** | **int** | code HTTP status code | [optional] 
**data** | [**List[PostGroupNoteResponseDataInner]**](PostGroupNoteResponseDataInner.md) | Data | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_group_note_response import PostGroupNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostGroupNoteResponse from a JSON string
post_group_note_response_instance = PostGroupNoteResponse.from_json(json)
# print the JSON string representation of the object
print(PostGroupNoteResponse.to_json())

# convert the object into a dict
post_group_note_response_dict = post_group_note_response_instance.to_dict()
# create an instance of PostGroupNoteResponse from a dict
post_group_note_response_from_dict = PostGroupNoteResponse.from_dict(post_group_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


