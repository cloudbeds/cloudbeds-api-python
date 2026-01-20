# EventResponseSchema

Event response data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique event ID | 
**event_code** | **str** | Event code (legacy: groupCode) | 
**profile_id** | **str** | GPS Profile ID linked to this event | [optional] 
**name** | **str** | Event name | 
**status** | **str** | Event status | 
**source_id** | **str** | Source ID | [optional] 
**source_name** | **str** | Source name | [optional] 
**start_date** | **date** | Event start date (YYYY-MM-DD) | [optional] 
**end_date** | **date** | Event end date (YYYY-MM-DD) | [optional] 
**transaction_mode** | **str** | Transaction routing mode | [optional] 
**transaction_types** | **List[str]** | Transaction types when mode is post_into_group | [optional] 
**folio_config_id** | **str** | Folio configuration ID | [optional] 
**enable_aggregate_allotment_block** | **bool** | Aggregate allotment block enabled | [optional] 
**aggregate_allotment_block_package_id** | **str** | Package ID for aggregate allotment block | [optional] 
**segment_id** | **str** | Market segment ID | [optional] 
**allotment_block_count** | **int** | Number of allotment blocks | [optional] 
**reservations_count** | **int** | Number of linked reservations | [optional] 
**rooms_held** | **int** | Total rooms held | [optional] 
**rooms_picked_up** | **int** | Rooms picked up | [optional] 
**rooms_remaining** | **int** | Rooms remaining | [optional] 
**total** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**grand_total** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**paid_value** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**balance_due** | [**MoneySchema**](MoneySchema.md) |  | [optional] 
**created_at** | **datetime** | Creation timestamp (RFC 3339) | 
**updated_at** | **datetime** | Last update timestamp (RFC 3339) | 

## Example

```python
from cloudbeds_pms.models.event_response_schema import EventResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of EventResponseSchema from a JSON string
event_response_schema_instance = EventResponseSchema.from_json(json)
# print the JSON string representation of the object
print(EventResponseSchema.to_json())

# convert the object into a dict
event_response_schema_dict = event_response_schema_instance.to_dict()
# create an instance of EventResponseSchema from a dict
event_response_schema_from_dict = EventResponseSchema.from_dict(event_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


