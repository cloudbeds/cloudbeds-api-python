# DeleteItemFromReservationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.delete_item_from_reservation_response import DeleteItemFromReservationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteItemFromReservationResponse from a JSON string
delete_item_from_reservation_response_instance = DeleteItemFromReservationResponse.from_json(json)
# print the JSON string representation of the object
print(DeleteItemFromReservationResponse.to_json())

# convert the object into a dict
delete_item_from_reservation_response_dict = delete_item_from_reservation_response_instance.to_dict()
# create an instance of DeleteItemFromReservationResponse from a dict
delete_item_from_reservation_response_from_dict = DeleteItemFromReservationResponse.from_dict(delete_item_from_reservation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


