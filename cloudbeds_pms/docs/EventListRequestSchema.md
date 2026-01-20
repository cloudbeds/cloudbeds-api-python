# EventListRequestSchema

Request parameters for listing events

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_code** | **str** | Filter by event code (legacy: groupCode) | [optional] 
**profile_id** | **str** | Filter by GPS profile ID | [optional] 
**status** | **str** | Filter by event status | [optional] 
**created_from** | **str** | Filter events created after this datetime (RFC 3339 format) | [optional] 
**created_to** | **str** | Filter events created before this datetime (RFC 3339 format) | [optional] 
**start_date_from** | **str** | Filter events where startDate is on or after this date (YYYY-MM-DD format) | [optional] 
**start_date_to** | **str** | Filter events where startDate is on or before this date (YYYY-MM-DD format) | [optional] 
**end_date_from** | **str** | Filter events where endDate is on or after this date (YYYY-MM-DD format) | [optional] 
**end_date_to** | **str** | Filter events where endDate is on or before this date (YYYY-MM-DD format) | [optional] 
**limit** | **int** | Maximum number of items to return (default: 100, max: 100) | [optional] 
**offset** | **int** | Number of items to skip (default: 0) | [optional] 

## Example

```python
from cloudbeds_pms.models.event_list_request_schema import EventListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventListRequestSchema from a JSON string
event_list_request_schema_instance = EventListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(EventListRequestSchema.to_json())

# convert the object into a dict
event_list_request_schema_dict = event_list_request_schema_instance.to_dict()
# create an instance of EventListRequestSchema from a dict
event_list_request_schema_from_dict = EventListRequestSchema.from_dict(event_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


