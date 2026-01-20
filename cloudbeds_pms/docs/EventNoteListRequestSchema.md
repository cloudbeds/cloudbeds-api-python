# EventNoteListRequestSchema

Request parameters for listing event notes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event ID or event code (e.g., \&quot;12345\&quot; or \&quot;g162795\&quot;) | [optional] 
**limit** | **int** | Maximum number of items to return (default: 100, max: 100) | [optional] 
**offset** | **int** | Number of items to skip (default: 0) | [optional] 
**include_archived** | **bool** | Include archived notes (default: false) | [optional] 

## Example

```python
from cloudbeds_pms.models.event_note_list_request_schema import EventNoteListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventNoteListRequestSchema from a JSON string
event_note_list_request_schema_instance = EventNoteListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(EventNoteListRequestSchema.to_json())

# convert the object into a dict
event_note_list_request_schema_dict = event_note_list_request_schema_instance.to_dict()
# create an instance of EventNoteListRequestSchema from a dict
event_note_list_request_schema_from_dict = EventNoteListRequestSchema.from_dict(event_note_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


