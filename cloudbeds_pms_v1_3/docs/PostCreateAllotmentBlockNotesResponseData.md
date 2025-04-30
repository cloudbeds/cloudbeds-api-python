# PostCreateAllotmentBlockNotesResponseData

The created note

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Note ID | [optional] 
**text** | **str** | Note contents | [optional] 
**created_by** | **str** | User Name | [optional] 
**created_at** | **datetime** | Creation datetime (format: Y-m-d H:i:s) | [optional] 
**updated_at** | **datetime** | Last modification datetime  (format: Y-m-d H:i:s) | [optional] 
**archived_at** | **datetime** | Archival datetime (format: Y-m-d H:i:s) | [optional] 
**status** | **str** | Note status | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_create_allotment_block_notes_response_data import PostCreateAllotmentBlockNotesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreateAllotmentBlockNotesResponseData from a JSON string
post_create_allotment_block_notes_response_data_instance = PostCreateAllotmentBlockNotesResponseData.from_json(json)
# print the JSON string representation of the object
print(PostCreateAllotmentBlockNotesResponseData.to_json())

# convert the object into a dict
post_create_allotment_block_notes_response_data_dict = post_create_allotment_block_notes_response_data_instance.to_dict()
# create an instance of PostCreateAllotmentBlockNotesResponseData from a dict
post_create_allotment_block_notes_response_data_from_dict = PostCreateAllotmentBlockNotesResponseData.from_dict(post_create_allotment_block_notes_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


