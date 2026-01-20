# EventNoteCreateRequestSchema

Request body for creating an event note

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event ID or event code (e.g., \&quot;12345\&quot; or \&quot;g162795\&quot;) | [optional] 
**text** | **str** | Note content | 

## Example

```python
from cloudbeds_pms.models.event_note_create_request_schema import EventNoteCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventNoteCreateRequestSchema from a JSON string
event_note_create_request_schema_instance = EventNoteCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(EventNoteCreateRequestSchema.to_json())

# convert the object into a dict
event_note_create_request_schema_dict = event_note_create_request_schema_instance.to_dict()
# create an instance of EventNoteCreateRequestSchema from a dict
event_note_create_request_schema_from_dict = EventNoteCreateRequestSchema.from_dict(event_note_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


