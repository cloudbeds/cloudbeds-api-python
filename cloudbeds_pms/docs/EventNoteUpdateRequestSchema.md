# EventNoteUpdateRequestSchema

Request body for updating an event note. At least one field must be provided.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event ID or event code (e.g., \&quot;12345\&quot; or \&quot;g162795\&quot;) | [optional] 
**note_id** | **str** | Note ID | [optional] 
**text** | **str** | Updated note content | [optional] 
**archived** | **bool** | Archive the note | [optional] 

## Example

```python
from cloudbeds_pms.models.event_note_update_request_schema import EventNoteUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventNoteUpdateRequestSchema from a JSON string
event_note_update_request_schema_instance = EventNoteUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(EventNoteUpdateRequestSchema.to_json())

# convert the object into a dict
event_note_update_request_schema_dict = event_note_update_request_schema_instance.to_dict()
# create an instance of EventNoteUpdateRequestSchema from a dict
event_note_update_request_schema_from_dict = EventNoteUpdateRequestSchema.from_dict(event_note_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


