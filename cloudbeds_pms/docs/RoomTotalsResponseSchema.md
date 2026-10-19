# RoomTotalsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_without_taxes** | [**MoneySchema**](MoneySchema.md) |  | 
**total_first_night_without_taxes** | [**MoneySchema**](MoneySchema.md) |  | 
**taxes_and_fees** | [**MoneySchema**](MoneySchema.md) |  | 
**taxes_and_fees_first_night** | [**MoneySchema**](MoneySchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.room_totals_response_schema import RoomTotalsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of RoomTotalsResponseSchema from a JSON string
room_totals_response_schema_instance = RoomTotalsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(RoomTotalsResponseSchema.to_json())

# convert the object into a dict
room_totals_response_schema_dict = room_totals_response_schema_instance.to_dict()
# create an instance of RoomTotalsResponseSchema from a dict
room_totals_response_schema_from_dict = RoomTotalsResponseSchema.from_dict(room_totals_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


