# EventSingleResponseSchema

Single event response with success envelope

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Success status | 
**data** | [**EventResponseSchema**](EventResponseSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.event_single_response_schema import EventSingleResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventSingleResponseSchema from a JSON string
event_single_response_schema_instance = EventSingleResponseSchema.from_json(json)
# print the JSON string representation of the object
print(EventSingleResponseSchema.to_json())

# convert the object into a dict
event_single_response_schema_dict = event_single_response_schema_instance.to_dict()
# create an instance of EventSingleResponseSchema from a dict
event_single_response_schema_from_dict = EventSingleResponseSchema.from_dict(event_single_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


