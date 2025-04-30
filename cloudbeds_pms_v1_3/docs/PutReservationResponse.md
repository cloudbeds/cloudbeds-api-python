# PutReservationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs. | [optional] 
**data** | **object** | Returns the reservation data as defined by getReservation call. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.put_reservation_response import PutReservationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutReservationResponse from a JSON string
put_reservation_response_instance = PutReservationResponse.from_json(json)
# print the JSON string representation of the object
print(PutReservationResponse.to_json())

# convert the object into a dict
put_reservation_response_dict = put_reservation_response_instance.to_dict()
# create an instance of PutReservationResponse from a dict
put_reservation_response_from_dict = PutReservationResponse.from_dict(put_reservation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


