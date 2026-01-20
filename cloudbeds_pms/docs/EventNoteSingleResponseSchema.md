# EventNoteSingleResponseSchema

Single event note response with success envelope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success status | 
**data** | [**EventNoteResponseSchema**](EventNoteResponseSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.event_note_single_response_schema import EventNoteSingleResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventNoteSingleResponseSchema from a JSON string
event_note_single_response_schema_instance = EventNoteSingleResponseSchema.from_json(json)
# print the JSON string representation of the object
print(EventNoteSingleResponseSchema.to_json())

# convert the object into a dict
event_note_single_response_schema_dict = event_note_single_response_schema_instance.to_dict()
# create an instance of EventNoteSingleResponseSchema from a dict
event_note_single_response_schema_from_dict = EventNoteSingleResponseSchema.from_dict(event_note_single_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


