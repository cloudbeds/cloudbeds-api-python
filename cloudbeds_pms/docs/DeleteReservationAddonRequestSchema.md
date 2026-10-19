# DeleteReservationAddonRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | The reservation ID, as returned by getReservation. | 
**sold_addon_id** | **str** | The add-on&#39;s soldProductID from reservationAddOnProducts in getReservation. | 

## Example

```python
from cloudbeds_pms.models.delete_reservation_addon_request_schema import DeleteReservationAddonRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteReservationAddonRequestSchema from a JSON string
delete_reservation_addon_request_schema_instance = DeleteReservationAddonRequestSchema.from_json(json)
# print the JSON string representation of the object
print(DeleteReservationAddonRequestSchema.to_json())

# convert the object into a dict
delete_reservation_addon_request_schema_dict = delete_reservation_addon_request_schema_instance.to_dict()
# create an instance of DeleteReservationAddonRequestSchema from a dict
delete_reservation_addon_request_schema_from_dict = DeleteReservationAddonRequestSchema.from_dict(delete_reservation_addon_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


