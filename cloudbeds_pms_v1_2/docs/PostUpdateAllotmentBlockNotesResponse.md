# PostUpdateAllotmentBlockNotesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**PostUpdateAllotmentBlockNotesResponseData**](PostUpdateAllotmentBlockNotesResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_update_allotment_block_notes_response import PostUpdateAllotmentBlockNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostUpdateAllotmentBlockNotesResponse from a JSON string
post_update_allotment_block_notes_response_instance = PostUpdateAllotmentBlockNotesResponse.from_json(json)
# print the JSON string representation of the object
print(PostUpdateAllotmentBlockNotesResponse.to_json())

# convert the object into a dict
post_update_allotment_block_notes_response_dict = post_update_allotment_block_notes_response_instance.to_dict()
# create an instance of PostUpdateAllotmentBlockNotesResponse from a dict
post_update_allotment_block_notes_response_from_dict = PostUpdateAllotmentBlockNotesResponse.from_dict(post_update_allotment_block_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


