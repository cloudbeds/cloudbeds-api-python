# GetHotelDetailsResponseDataPropertyPolicy



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_check_in_time** | **str** |  | [optional] 
**property_check_out_time** | **str** |  | [optional] 
**property_late_check_out_allowed** | **bool** |  | [optional] 
**property_late_check_out_type** | **str** | If the property accepts late check-out, defines if the value is fixed, or a percentage of the daily rate | [optional] 
**property_late_check_out_value** | **str** | The fixed value, or percentage of the daily rate, to be charged on a late check-out | [optional] 
**property_terms_and_conditions** | **str** | Text describing the terms and conditions to be displayed to guest | [optional] 
**property_full_payment_before_checkin** | **bool** | If the property requires the full payment amount of the reservation to be collected prior to check-in | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_hotel_details_response_data_property_policy import GetHotelDetailsResponseDataPropertyPolicy

# TODO update the JSON string below
json = "{}"
# create an instance of GetHotelDetailsResponseDataPropertyPolicy from a JSON string
get_hotel_details_response_data_property_policy_instance = GetHotelDetailsResponseDataPropertyPolicy.from_json(json)
# print the JSON string representation of the object
print(GetHotelDetailsResponseDataPropertyPolicy.to_json())

# convert the object into a dict
get_hotel_details_response_data_property_policy_dict = get_hotel_details_response_data_property_policy_instance.to_dict()
# create an instance of GetHotelDetailsResponseDataPropertyPolicy from a dict
get_hotel_details_response_data_property_policy_from_dict = GetHotelDetailsResponseDataPropertyPolicy.from_dict(get_hotel_details_response_data_property_policy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


