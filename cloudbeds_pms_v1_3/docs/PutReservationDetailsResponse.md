# PutReservationDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**message** | **str** | To be used in case any error occurs. | [optional] 
**data** | **object** | Returns the reservation data as defined by getReservation call. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.put_reservation_details_response import PutReservationDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PutReservationDetailsResponse from a JSON string
put_reservation_details_response_instance = PutReservationDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(PutReservationDetailsResponse.to_json())

# convert the object into a dict
put_reservation_details_response_dict = put_reservation_details_response_instance.to_dict()
# create an instance of PutReservationDetailsResponse from a dict
put_reservation_details_response_from_dict = PutReservationDetailsResponse.from_dict(put_reservation_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


