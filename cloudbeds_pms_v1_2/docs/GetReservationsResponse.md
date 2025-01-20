# GetReservationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetReservationsResponseDataInner]**](GetReservationsResponseDataInner.md) | Details for the reservation queried | [optional] 
**count** | **int** | Number of results returned | [optional] 
**total** | **int** | Total number of results | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservations_response import GetReservationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationsResponse from a JSON string
get_reservations_response_instance = GetReservationsResponse.from_json(json)
# print the JSON string representation of the object
print(GetReservationsResponse.to_json())

# convert the object into a dict
get_reservations_response_dict = get_reservations_response_instance.to_dict()
# create an instance of GetReservationsResponse from a dict
get_reservations_response_from_dict = GetReservationsResponse.from_dict(get_reservations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


