# EventUpdateRequestSchema

Request body for updating an event. Only provided fields are updated. For profileId: omit to keep, null to clear, string to replace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **str** | Event ID or event code (e.g., \&quot;12345\&quot; or \&quot;g162795\&quot;) | [optional] 
**profile_id** | **str** | GPS Profile ID. Omit to keep unchanged, send null to clear, or send string to replace. | [optional] 
**name** | **str** | Event name | [optional] 
**status** | **str** | Event status | [optional] 
**source_id** | **str** | Source ID for the event booking source | [optional] 
**start_date** | **str** | Event start date (YYYY-MM-DD). NOTE: Informational only - effective event dates are calculated from linked reservations. | [optional] 
**end_date** | **str** | Event end date (YYYY-MM-DD). NOTE: Informational only - effective event dates are calculated from linked reservations. | [optional] 
**transaction_mode** | **str** | Transaction routing mode | [optional] 
**transaction_types** | **List[str]** | Transaction types to route (required when transactionMode is post_into_group) | [optional] 
**folio_config_id** | **str** | Folio configuration ID | [optional] 
**enable_aggregate_allotment_block** | **bool** | Enable aggregate allotment block feature | [optional] 
**aggregate_allotment_block_package_id** | **str** | Package ID for aggregate allotment block | [optional] 
**segment_id** | **str** | Market segment ID | [optional] 

## Example

```python
from cloudbeds_pms.models.event_update_request_schema import EventUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventUpdateRequestSchema from a JSON string
event_update_request_schema_instance = EventUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(EventUpdateRequestSchema.to_json())

# convert the object into a dict
event_update_request_schema_dict = event_update_request_schema_instance.to_dict()
# create an instance of EventUpdateRequestSchema from a dict
event_update_request_schema_from_dict = EventUpdateRequestSchema.from_dict(event_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


