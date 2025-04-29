# GetReservationInHouseResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**List[GetReservationInHouseResponseDataInner]**](GetReservationInHouseResponseDataInner.md) | Details for the arrivals scheduled for today | [optional] 
**message** | **str** | To be used in case any error occurs (if success &#x3D; false). If success &#x3D; true, it does not exist. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_in_house_response import GetReservationInHouseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationInHouseResponse from a JSON string
get_reservation_in_house_response_instance = GetReservationInHouseResponse.from_json(json)
# print the JSON string representation of the object
print(GetReservationInHouseResponse.to_json())

# convert the object into a dict
get_reservation_in_house_response_dict = get_reservation_in_house_response_instance.to_dict()
# create an instance of GetReservationInHouseResponse from a dict
get_reservation_in_house_response_from_dict = GetReservationInHouseResponse.from_dict(get_reservation_in_house_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


