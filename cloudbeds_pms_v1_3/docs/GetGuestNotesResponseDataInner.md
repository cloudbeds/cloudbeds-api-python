# GetGuestNotesResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**guest_note_id** | **str** | Guest note ID | [optional] 
**user_name** | **str** | User Name | [optional] 
**date_created** | **datetime** | Creation datetime | [optional] 
**date_modified** | **datetime** | Last modification datetime | [optional] 
**guest_note** | **str** | Note content | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_guest_notes_response_data_inner import GetGuestNotesResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGuestNotesResponseDataInner from a JSON string
get_guest_notes_response_data_inner_instance = GetGuestNotesResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetGuestNotesResponseDataInner.to_json())

# convert the object into a dict
get_guest_notes_response_data_inner_dict = get_guest_notes_response_data_inner_instance.to_dict()
# create an instance of GetGuestNotesResponseDataInner from a dict
get_guest_notes_response_data_inner_from_dict = GetGuestNotesResponseDataInner.from_dict(get_guest_notes_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


