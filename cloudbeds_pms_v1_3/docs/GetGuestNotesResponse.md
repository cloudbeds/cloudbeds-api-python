# GetGuestNotesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetGuestNotesResponseDataInner]**](GetGuestNotesResponseDataInner.md) | Details for the notes on that reservation | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_guest_notes_response import GetGuestNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGuestNotesResponse from a JSON string
get_guest_notes_response_instance = GetGuestNotesResponse.from_json(json)
# print the JSON string representation of the object
print(GetGuestNotesResponse.to_json())

# convert the object into a dict
get_guest_notes_response_dict = get_guest_notes_response_instance.to_dict()
# create an instance of GetGuestNotesResponse from a dict
get_guest_notes_response_from_dict = GetGuestNotesResponse.from_dict(get_guest_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


