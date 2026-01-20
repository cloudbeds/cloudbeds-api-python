# EventListResponseSchema

Paginated list of events

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success status | 
**offset** | **int** | Number of items skipped (pagination offset) | 
**limit** | **int** | Maximum number of items returned | 
**data** | [**List[EventResponseSchema]**](EventResponseSchema.md) | List of events | 

## Example

```python
from cloudbeds_pms.models.event_list_response_schema import EventListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventListResponseSchema from a JSON string
event_list_response_schema_instance = EventListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(EventListResponseSchema.to_json())

# convert the object into a dict
event_list_response_schema_dict = event_list_response_schema_instance.to_dict()
# create an instance of EventListResponseSchema from a dict
event_list_response_schema_from_dict = EventListResponseSchema.from_dict(event_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


