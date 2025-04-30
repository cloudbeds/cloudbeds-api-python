# GetReservationResponseDataCardsOnFileInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_id** | **str** | Credit Card ID, used for card operations | [optional] 
**card_number** | **str** | Ending digits of the credit card | [optional] 
**card_type** | **str** | Abbreviated name of credit card type | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservation_response_data_cards_on_file_inner import GetReservationResponseDataCardsOnFileInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationResponseDataCardsOnFileInner from a JSON string
get_reservation_response_data_cards_on_file_inner_instance = GetReservationResponseDataCardsOnFileInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationResponseDataCardsOnFileInner.to_json())

# convert the object into a dict
get_reservation_response_data_cards_on_file_inner_dict = get_reservation_response_data_cards_on_file_inner_instance.to_dict()
# create an instance of GetReservationResponseDataCardsOnFileInner from a dict
get_reservation_response_data_cards_on_file_inner_from_dict = GetReservationResponseDataCardsOnFileInner.from_dict(get_reservation_response_data_cards_on_file_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


