# GetDashboardResponseData

Data to be displayed on dashboard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rooms_occupied** | **int** | Number of rooms occupied at the moment | [optional] 
**percentage_occupied** | **int** | Percentage of rooms occupied (rooms occupied/rooms total) for the current day | [optional] 
**arrivals** | **int** | Number of arrivals (check-ins) expected for the current day | [optional] 
**departures** | **int** | Number of departures (check-outs) expected for the current day | [optional] 
**in_house** | **int** | Number of rooms occupied, and not expected to have a check-out for the current day | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_dashboard_response_data import GetDashboardResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetDashboardResponseData from a JSON string
get_dashboard_response_data_instance = GetDashboardResponseData.from_json(json)
# print the JSON string representation of the object
print(GetDashboardResponseData.to_json())

# convert the object into a dict
get_dashboard_response_data_dict = get_dashboard_response_data_instance.to_dict()
# create an instance of GetDashboardResponseData from a dict
get_dashboard_response_data_from_dict = GetDashboardResponseData.from_dict(get_dashboard_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


