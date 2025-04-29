# GetReservationsWithRateDetailsResponseDataInnerSourceInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Reservation source | [optional] 
**payment_collect** | **str** | Reservation payment collect source | [optional] 
**source_id** | **str** | Booking source unique id | [optional] 
**category** | **str** | Reservation source category | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_reservations_with_rate_details_response_data_inner_source_inner import GetReservationsWithRateDetailsResponseDataInnerSourceInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetReservationsWithRateDetailsResponseDataInnerSourceInner from a JSON string
get_reservations_with_rate_details_response_data_inner_source_inner_instance = GetReservationsWithRateDetailsResponseDataInnerSourceInner.from_json(json)
# print the JSON string representation of the object
print(GetReservationsWithRateDetailsResponseDataInnerSourceInner.to_json())

# convert the object into a dict
get_reservations_with_rate_details_response_data_inner_source_inner_dict = get_reservations_with_rate_details_response_data_inner_source_inner_instance.to_dict()
# create an instance of GetReservationsWithRateDetailsResponseDataInnerSourceInner from a dict
get_reservations_with_rate_details_response_data_inner_source_inner_from_dict = GetReservationsWithRateDetailsResponseDataInnerSourceInner.from_dict(get_reservations_with_rate_details_response_data_inner_source_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


