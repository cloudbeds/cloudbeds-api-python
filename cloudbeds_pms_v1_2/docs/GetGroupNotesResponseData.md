# GetGroupNotesResponseData

Data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID for the note | [optional] 
**group_profile_id** | **str** | Group profile ID | [optional] 
**text** | **str** | Note text | [optional] 
**created_by** | **str** | Created by | [optional] 
**created_at** | **str** | Created at | [optional] 
**updated_at** | **str** | Updated at | [optional] 
**archived** | **bool** | Note archived | [optional] 
**archived_at** | **str** | Note archived at | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_group_notes_response_data import GetGroupNotesResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupNotesResponseData from a JSON string
get_group_notes_response_data_instance = GetGroupNotesResponseData.from_json(json)
# print the JSON string representation of the object
print(GetGroupNotesResponseData.to_json())

# convert the object into a dict
get_group_notes_response_data_dict = get_group_notes_response_data_instance.to_dict()
# create an instance of GetGroupNotesResponseData from a dict
get_group_notes_response_data_from_dict = GetGroupNotesResponseData.from_dict(get_group_notes_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


