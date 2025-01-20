# GetListAllotmentBlockNotesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Note ID | [optional] 
**message** | **str** | Note contents | [optional] 
**created_by** | **str** | User Name | [optional] 
**created_at** | **datetime** | Creation datetime (format: Y-m-d H:i:s) | [optional] 
**updated_at** | **datetime** | Last modification datetime (format: Y-m-d H:i:s) | [optional] 
**archived_at** | **datetime** | Archival datetime (format: Y-m-d H:i:s) | [optional] 
**status** | **str** | Note status | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_list_allotment_block_notes_response_data_inner import GetListAllotmentBlockNotesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetListAllotmentBlockNotesResponseDataInner from a JSON string
get_list_allotment_block_notes_response_data_inner_instance = GetListAllotmentBlockNotesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetListAllotmentBlockNotesResponseDataInner.to_json())

# convert the object into a dict
get_list_allotment_block_notes_response_data_inner_dict = get_list_allotment_block_notes_response_data_inner_instance.to_dict()
# create an instance of GetListAllotmentBlockNotesResponseDataInner from a dict
get_list_allotment_block_notes_response_data_inner_from_dict = GetListAllotmentBlockNotesResponseDataInner.from_dict(get_list_allotment_block_notes_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


