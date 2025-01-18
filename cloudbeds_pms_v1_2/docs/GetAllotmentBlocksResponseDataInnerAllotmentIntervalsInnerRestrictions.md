# GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerRestrictions

Interval restrictions if applicable

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_los** | **int** | Minimum length of stay requirement | [optional] 
**max_los** | **int** | Maximum length of stay requirement | [optional] 
**cut_off_days** | **int** | How many days before arrival should guests be required to book | [optional] 
**last_minute_booking_days** | **int** | How many days before the arrival guests are allowed to book | [optional] 
**closed_to_arrival** | **int** | If the interval dates are closed for arrival | [optional] 
**closed_to_departure** | **int** | If the interval dates are closed for departure | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_allotment_blocks_response_data_inner_allotment_intervals_inner_restrictions import GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerRestrictions from a JSON string
get_allotment_blocks_response_data_inner_allotment_intervals_inner_restrictions_instance = GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerRestrictions.from_json(json)
# print the JSON string representation of the object
print(GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerRestrictions.to_json())

# convert the object into a dict
get_allotment_blocks_response_data_inner_allotment_intervals_inner_restrictions_dict = get_allotment_blocks_response_data_inner_allotment_intervals_inner_restrictions_instance.to_dict()
# create an instance of GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerRestrictions from a dict
get_allotment_blocks_response_data_inner_allotment_intervals_inner_restrictions_from_dict = GetAllotmentBlocksResponseDataInnerAllotmentIntervalsInnerRestrictions.from_dict(get_allotment_blocks_response_data_inner_allotment_intervals_inner_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


