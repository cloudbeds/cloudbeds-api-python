# ReservationCommissionRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.reservation_commission_request_schema import ReservationCommissionRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ReservationCommissionRequestSchema from a JSON string
reservation_commission_request_schema_instance = ReservationCommissionRequestSchema.from_json(json)
# print the JSON string representation of the object
print(ReservationCommissionRequestSchema.to_json())

# convert the object into a dict
reservation_commission_request_schema_dict = reservation_commission_request_schema_instance.to_dict()
# create an instance of ReservationCommissionRequestSchema from a dict
reservation_commission_request_schema_from_dict = ReservationCommissionRequestSchema.from_dict(reservation_commission_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


