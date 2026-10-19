# LastRoomValueDecisionSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **int** | Room Type ID. | 
**occupancy_date** | **str** | Occupancy date (YYYY-MM-DD). | 
**last_room_value** | **str** | Last room value as sent by IDeaS. May be negative; a negative value is flagged as an anomaly downstream rather than rejected here. | 
**ceiling_value** | **str** | Ceiling value as sent by IDeaS, kept for context/audit. | [optional] 
**delta_value** | **str** | Delta value as sent by IDeaS, kept for context/audit. | [optional] 
**max_solds** | **int** | Maximum number of units sold as sent by IDeaS, kept for context/audit. | [optional] 
**currency_code** | **str** | ISO 4217 currency code. | [optional] 

## Example

```python
from cloudbeds_pms.models.last_room_value_decision_schema import LastRoomValueDecisionSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LastRoomValueDecisionSchema from a JSON string
last_room_value_decision_schema_instance = LastRoomValueDecisionSchema.from_json(json)
# print the JSON string representation of the object
print(LastRoomValueDecisionSchema.to_json())

# convert the object into a dict
last_room_value_decision_schema_dict = last_room_value_decision_schema_instance.to_dict()
# create an instance of LastRoomValueDecisionSchema from a dict
last_room_value_decision_schema_from_dict = LastRoomValueDecisionSchema.from_dict(last_room_value_decision_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


