# PutGuestNoteResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.put_guest_note_response import PutGuestNoteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutGuestNoteResponse from a JSON string
put_guest_note_response_instance = PutGuestNoteResponse.from_json(json)
# print the JSON string representation of the object
print(PutGuestNoteResponse.to_json())

# convert the object into a dict
put_guest_note_response_dict = put_guest_note_response_instance.to_dict()
# create an instance of PutGuestNoteResponse from a dict
put_guest_note_response_from_dict = PutGuestNoteResponse.from_dict(put_guest_note_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


