# GetReservationsWithRateDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetReservationsWithRateDetailsResponseDataInner]**](GetReservationsWithRateDetailsResponseDataInner.md) | Details for the reservations returned | [optional] 
**count** | **int** | Number of results returned | [optional] 
**total** | **int** | Total number of results | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_reservations_with_rate_details_response import GetReservationsWithRateDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationsWithRateDetailsResponse from a JSON string
get_reservations_with_rate_details_response_instance = GetReservationsWithRateDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetReservationsWithRateDetailsResponse.to_json())

# convert the object into a dict
get_reservations_with_rate_details_response_dict = get_reservations_with_rate_details_response_instance.to_dict()
# create an instance of GetReservationsWithRateDetailsResponse from a dict
get_reservations_with_rate_details_response_from_dict = GetReservationsWithRateDetailsResponse.from_dict(get_reservations_with_rate_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


