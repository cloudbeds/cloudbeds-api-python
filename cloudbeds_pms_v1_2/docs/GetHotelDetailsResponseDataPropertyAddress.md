# GetHotelDetailsResponseDataPropertyAddress



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_address1** | **str** |  | [optional] 
**property_address2** | **str** |  | [optional] 
**property_city** | **str** |  | [optional] 
**property_state** | **str** |  | [optional] 
**property_zip** | **str** |  | [optional] 
**property_country** | **str** |  | [optional] 
**property_latitude** | **str** |  | [optional] 
**property_longitude** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_hotel_details_response_data_property_address import GetHotelDetailsResponseDataPropertyAddress

# TODO update the JSON string below
json = "{}"
# create an instance of GetHotelDetailsResponseDataPropertyAddress from a JSON string
get_hotel_details_response_data_property_address_instance = GetHotelDetailsResponseDataPropertyAddress.from_json(json)
# print the JSON string representation of the object
print(GetHotelDetailsResponseDataPropertyAddress.to_json())

# convert the object into a dict
get_hotel_details_response_data_property_address_dict = get_hotel_details_response_data_property_address_instance.to_dict()
# create an instance of GetHotelDetailsResponseDataPropertyAddress from a dict
get_hotel_details_response_data_property_address_from_dict = GetHotelDetailsResponseDataPropertyAddress.from_dict(get_hotel_details_response_data_property_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


