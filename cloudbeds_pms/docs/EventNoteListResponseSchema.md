# EventNoteListResponseSchema

Paginated list of event notes

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success status | 
**offset** | **int** | Number of items skipped (pagination offset) | 
**limit** | **int** | Maximum number of items returned | 
**data** | [**List[EventNoteResponseSchema]**](EventNoteResponseSchema.md) | List of event notes | 

## Example

```python
from cloudbeds_pms.models.event_note_list_response_schema import EventNoteListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventNoteListResponseSchema from a JSON string
event_note_list_response_schema_instance = EventNoteListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(EventNoteListResponseSchema.to_json())

# convert the object into a dict
event_note_list_response_schema_dict = event_note_list_response_schema_instance.to_dict()
# create an instance of EventNoteListResponseSchema from a dict
event_note_list_response_schema_from_dict = EventNoteListResponseSchema.from_dict(event_note_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


