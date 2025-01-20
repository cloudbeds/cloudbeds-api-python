# GetListAllotmentBlockNotesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetListAllotmentBlockNotesResponseDataInner]**](GetListAllotmentBlockNotesResponseDataInner.md) | List of notes | [optional] 
**page_size** | **int** | Number of Notes per Page | [optional] 
**page_number** | **int** | Current page | [optional] 
**total** | **int** | Total number of Notes | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_list_allotment_block_notes_response import GetListAllotmentBlockNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetListAllotmentBlockNotesResponse from a JSON string
get_list_allotment_block_notes_response_instance = GetListAllotmentBlockNotesResponse.from_json(json)
# print the JSON string representation of the object
print(GetListAllotmentBlockNotesResponse.to_json())

# convert the object into a dict
get_list_allotment_block_notes_response_dict = get_list_allotment_block_notes_response_instance.to_dict()
# create an instance of GetListAllotmentBlockNotesResponse from a dict
get_list_allotment_block_notes_response_from_dict = GetListAllotmentBlockNotesResponse.from_dict(get_list_allotment_block_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


