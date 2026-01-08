# GetReservationsWithRateDetailsResponseDataInnerBalanceDetailed

Reservation balance detailed with the information available on MyFrontdesk, describing the financial items calculated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**suggested_deposit** | **str** | Suggested deposit value, calculated according to the hotel policies. Does not mean that it was effectively paid | [optional] 
**sub_total** | **float** | Sum of the room prices on the reservation | [optional] 
**additional_items** | **float** | Sum of the additional items recorded on the reservation | [optional] 
**taxes_fees** | **float** | Sum of the taxes and fees calculated on the reservation | [optional] 
**grand_total** | **float** | Sum of sub.Total + additionalItems + taxesFees | [optional] 
**paid** | **float** | Amount paid (reservation deposit + any other extra payment) | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservations_with_rate_details_response_data_inner_balance_detailed import GetReservationsWithRateDetailsResponseDataInnerBalanceDetailed

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationsWithRateDetailsResponseDataInnerBalanceDetailed from a JSON string
get_reservations_with_rate_details_response_data_inner_balance_detailed_instance = GetReservationsWithRateDetailsResponseDataInnerBalanceDetailed.from_json(json)
# print the JSON string representation of the object
print(GetReservationsWithRateDetailsResponseDataInnerBalanceDetailed.to_json())

# convert the object into a dict
get_reservations_with_rate_details_response_data_inner_balance_detailed_dict = get_reservations_with_rate_details_response_data_inner_balance_detailed_instance.to_dict()
# create an instance of GetReservationsWithRateDetailsResponseDataInnerBalanceDetailed from a dict
get_reservations_with_rate_details_response_data_inner_balance_detailed_from_dict = GetReservationsWithRateDetailsResponseDataInnerBalanceDetailed.from_dict(get_reservations_with_rate_details_response_data_inner_balance_detailed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


