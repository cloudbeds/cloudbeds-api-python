# GetHotelDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**GetHotelDetailsResponseData**](GetHotelDetailsResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_hotel_details_response import GetHotelDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetHotelDetailsResponse from a JSON string
get_hotel_details_response_instance = GetHotelDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(GetHotelDetailsResponse.to_json())

# convert the object into a dict
get_hotel_details_response_dict = get_hotel_details_response_instance.to_dict()
# create an instance of GetHotelDetailsResponse from a dict
get_hotel_details_response_from_dict = GetHotelDetailsResponse.from_dict(get_hotel_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


