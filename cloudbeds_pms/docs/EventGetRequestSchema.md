# EventGetRequestSchema

Request schema for getting a single event.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event ID or event code (e.g., \&quot;12345\&quot; or \&quot;g162795\&quot;) | 

## Example

```python
from cloudbeds_pms.models.event_get_request_schema import EventGetRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventGetRequestSchema from a JSON string
event_get_request_schema_instance = EventGetRequestSchema.from_json(json)
# print the JSON string representation of the object
print(EventGetRequestSchema.to_json())

# convert the object into a dict
event_get_request_schema_dict = event_get_request_schema_instance.to_dict()
# create an instance of EventGetRequestSchema from a dict
event_get_request_schema_from_dict = EventGetRequestSchema.from_dict(event_get_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


