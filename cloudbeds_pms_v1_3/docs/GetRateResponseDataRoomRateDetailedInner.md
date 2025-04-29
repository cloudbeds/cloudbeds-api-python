# GetRateResponseDataRoomRateDetailedInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | [optional] 
**rate** | **float** | Base rate for the selected date | [optional] 
**total_rate** | **float** | Total rate for the selected date | [optional] 
**rooms_available** | **int** | Number of rooms available for the selected date | [optional] 
**closed_to_arrival** | **bool** |  | [optional] 
**closed_to_departure** | **bool** |  | [optional] 
**min_los** | **int** | Minimum Length Of Stay | [optional] 
**max_los** | **int** | Maximum Length Of Stay | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_rate_response_data_room_rate_detailed_inner import GetRateResponseDataRoomRateDetailedInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateResponseDataRoomRateDetailedInner from a JSON string
get_rate_response_data_room_rate_detailed_inner_instance = GetRateResponseDataRoomRateDetailedInner.from_json(json)
# print the JSON string representation of the object
print(GetRateResponseDataRoomRateDetailedInner.to_json())

# convert the object into a dict
get_rate_response_data_room_rate_detailed_inner_dict = get_rate_response_data_room_rate_detailed_inner_instance.to_dict()
# create an instance of GetRateResponseDataRoomRateDetailedInner from a dict
get_rate_response_data_room_rate_detailed_inner_from_dict = GetRateResponseDataRoomRateDetailedInner.from_dict(get_rate_response_data_room_rate_detailed_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


