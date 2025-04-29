# GetGroupNotesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success | [optional] 
**code** | **int** | HTTP status code | [optional] 
**data** | [**GetGroupNotesResponseData**](GetGroupNotesResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_group_notes_response import GetGroupNotesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroupNotesResponse from a JSON string
get_group_notes_response_instance = GetGroupNotesResponse.from_json(json)
# print the JSON string representation of the object
print(GetGroupNotesResponse.to_json())

# convert the object into a dict
get_group_notes_response_dict = get_group_notes_response_instance.to_dict()
# create an instance of GetGroupNotesResponse from a dict
get_group_notes_response_from_dict = GetGroupNotesResponse.from_dict(get_group_notes_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


