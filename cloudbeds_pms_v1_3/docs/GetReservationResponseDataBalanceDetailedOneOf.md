# GetReservationResponseDataBalanceDetailedOneOf


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
from cloudbeds_pms_v1_3.models.get_reservation_response_data_balance_detailed_one_of import GetReservationResponseDataBalanceDetailedOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationResponseDataBalanceDetailedOneOf from a JSON string
get_reservation_response_data_balance_detailed_one_of_instance = GetReservationResponseDataBalanceDetailedOneOf.from_json(json)
# print the JSON string representation of the object
print(GetReservationResponseDataBalanceDetailedOneOf.to_json())

# convert the object into a dict
get_reservation_response_data_balance_detailed_one_of_dict = get_reservation_response_data_balance_detailed_one_of_instance.to_dict()
# create an instance of GetReservationResponseDataBalanceDetailedOneOf from a dict
get_reservation_response_data_balance_detailed_one_of_from_dict = GetReservationResponseDataBalanceDetailedOneOf.from_dict(get_reservation_response_data_balance_detailed_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


