# ReservationCommissionResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**property_id** | **str** |  | 
**reservation_id** | **str** |  | 
**effective_commission** | [**MoneySchema**](MoneySchema.md) |  | 
**effective_commission_type** | **str** |  | 
**estimated_commission_from_source** | [**ReservationCommissionResponseSchemaEstimatedCommissionFromSource**](ReservationCommissionResponseSchemaEstimatedCommissionFromSource.md) |  | [optional] 
**estimated_commissionable_revenue** | [**ReservationCommissionResponseSchemaEstimatedCommissionFromSource**](ReservationCommissionResponseSchemaEstimatedCommissionFromSource.md) |  | [optional] 
**channel_commission** | [**ReservationCommissionResponseSchemaEstimatedCommissionFromSource**](ReservationCommissionResponseSchemaEstimatedCommissionFromSource.md) |  | [optional] 
**channel_commission_type** | **str** |  | [optional] 
**source_commission_percentage** | **float** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.reservation_commission_response_schema import ReservationCommissionResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationCommissionResponseSchema from a JSON string
reservation_commission_response_schema_instance = ReservationCommissionResponseSchema.from_json(json)
# print the JSON string representation of the object
print(ReservationCommissionResponseSchema.to_json())

# convert the object into a dict
reservation_commission_response_schema_dict = reservation_commission_response_schema_instance.to_dict()
# create an instance of ReservationCommissionResponseSchema from a dict
reservation_commission_response_schema_from_dict = ReservationCommissionResponseSchema.from_dict(reservation_commission_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


