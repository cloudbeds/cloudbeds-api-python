# EventNoteResponseSchema

Event note response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique note ID | 
**event_id** | **str** | Parent event ID | 
**text** | **str** | Note content | 
**created_by** | **str** | Creator name | 
**created_at** | **datetime** | Creation timestamp (RFC 3339) | 
**updated_at** | **datetime** | Last update timestamp (RFC 3339) | 
**archived** | **bool** | Whether note is archived | 
**archived_at** | **datetime** | Archive timestamp (RFC 3339) | [optional] 

## Example

```python
from cloudbeds_pms.models.event_note_response_schema import EventNoteResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventNoteResponseSchema from a JSON string
event_note_response_schema_instance = EventNoteResponseSchema.from_json(json)
# print the JSON string representation of the object
print(EventNoteResponseSchema.to_json())

# convert the object into a dict
event_note_response_schema_dict = event_note_response_schema_instance.to_dict()
# create an instance of EventNoteResponseSchema from a dict
event_note_response_schema_from_dict = EventNoteResponseSchema.from_dict(event_note_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


