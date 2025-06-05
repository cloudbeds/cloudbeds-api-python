# GetHotelDetailsResponseDataPropertyCurrency

Currency used by the property

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_code** | **str** | Currency code | [optional] 
**currency_symbol** | **str** | Currency symbol | [optional] 
**currency_position** | **str** | Currency position | [optional] 
**currency_decimal_separator** | **str** | Currency decimal separator | [optional] 
**currency_thousands_separator** | **str** | Currency thousands separator | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_hotel_details_response_data_property_currency import GetHotelDetailsResponseDataPropertyCurrency

# TODO update the JSON string below
json = "{}"
# create an instance of GetHotelDetailsResponseDataPropertyCurrency from a JSON string
get_hotel_details_response_data_property_currency_instance = GetHotelDetailsResponseDataPropertyCurrency.from_json(json)
# print the JSON string representation of the object
print(GetHotelDetailsResponseDataPropertyCurrency.to_json())

# convert the object into a dict
get_hotel_details_response_data_property_currency_dict = get_hotel_details_response_data_property_currency_instance.to_dict()
# create an instance of GetHotelDetailsResponseDataPropertyCurrency from a dict
get_hotel_details_response_data_property_currency_from_dict = GetHotelDetailsResponseDataPropertyCurrency.from_dict(get_hotel_details_response_data_property_currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


