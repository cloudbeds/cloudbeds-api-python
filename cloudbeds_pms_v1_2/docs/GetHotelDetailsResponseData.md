# GetHotelDetailsResponseData

Information about the hotel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **str** | Property ID | [optional] 
**organization_id** | **str** | Organization ID | [optional] 
**property_name** | **str** | Property name | [optional] 
**property_type** | **str** | The type of property | [optional] 
**property_image** | [**List[GetHotelDetailsResponseDataPropertyImageInner]**](GetHotelDetailsResponseDataPropertyImageInner.md) | Property images details | [optional] 
**property_description** | **str** | Property description | [optional] 
**property_currency** | [**GetHotelDetailsResponseDataPropertyCurrency**](GetHotelDetailsResponseDataPropertyCurrency.md) |  | [optional] 
**property_primary_language** | **str** | Property primary language | [optional] 
**property_additional_photos** | [**List[GetHotelDetailsResponseDataPropertyImageInner]**](GetHotelDetailsResponseDataPropertyImageInner.md) | Property additional photos | [optional] 
**property_phone** | **str** | Property phone number | [optional] 
**property_email** | **str** | Property main email address | [optional] 
**property_address** | [**GetHotelDetailsResponseDataPropertyAddress**](GetHotelDetailsResponseDataPropertyAddress.md) |  | [optional] 
**property_policy** | [**GetHotelDetailsResponseDataPropertyPolicy**](GetHotelDetailsResponseDataPropertyPolicy.md) |  | [optional] 
**property_amenities** | **List[str]** | List of property amenities | [optional] 
**tax_id** | **str** | Tax ID number | [optional] 
**tax_id2** | **str** | Second Tax ID number | [optional] 
**company_legal_name** | **str** | Legal company name | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_hotel_details_response_data import GetHotelDetailsResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetHotelDetailsResponseData from a JSON string
get_hotel_details_response_data_instance = GetHotelDetailsResponseData.from_json(json)
# print the JSON string representation of the object
print(GetHotelDetailsResponseData.to_json())

# convert the object into a dict
get_hotel_details_response_data_dict = get_hotel_details_response_data_instance.to_dict()
# create an instance of GetHotelDetailsResponseData from a dict
get_hotel_details_response_data_from_dict = GetHotelDetailsResponseData.from_dict(get_hotel_details_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


