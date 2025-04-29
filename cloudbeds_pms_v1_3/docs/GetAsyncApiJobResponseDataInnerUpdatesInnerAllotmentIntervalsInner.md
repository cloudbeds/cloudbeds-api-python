# GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_type_id** | **str** | Room type ID | [optional] 
**start_date** | **date** | Interval start date | [optional] 
**end_date** | **date** | Interval end date | [optional] 
**availability** | [**GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerAvailability**](GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerAvailability.md) |  | [optional] 
**restrictions** | [**GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerRestrictions**](GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerRestrictions.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner import GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInner from a JSON string
get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner_instance = GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInner.from_json(json)
# print the JSON string representation of the object
print(GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInner.to_json())

# convert the object into a dict
get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner_dict = get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner_instance.to_dict()
# create an instance of GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInner from a dict
get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner_from_dict = GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInner.from_dict(get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


