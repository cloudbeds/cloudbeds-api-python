# GetRateJobsResponseDataInnerUpdatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_id** | **str** | Rate ID for which action was taken | [optional] 
**action** | **str** | Action taken for this interval as part of this job. in_progress - interval wait for it turn. updated - interval was updated. created - new interval was created with the new date range. error - there was an error when attempting this update. Allowed values: in_progress, updated, created, error | [optional] 
**start_date** | **date** | Interval start date | [optional] 
**end_date** | **date** | Interval end date | [optional] 
**rate** | **float** | Value of rate which was updated | [optional] 
**max_los** | **int** | Maximum length of stay for this rate | [optional] 
**min_los** | **int** | Minimum length of stay for this rate | [optional] 
**closed_to_arrival** | **bool** | If this rate is closed to arrival | [optional] 
**closed_to_departure** | **bool** | If this rate is closed to departure | [optional] 
**cut_off** | **int** | Cutoff for this rate | [optional] 
**last_minute_booking** | **int** | Last minute booking for this rate | [optional] 
**message** | **str** | Error message | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_rate_jobs_response_data_inner_updates_inner import GetRateJobsResponseDataInnerUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateJobsResponseDataInnerUpdatesInner from a JSON string
get_rate_jobs_response_data_inner_updates_inner_instance = GetRateJobsResponseDataInnerUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(GetRateJobsResponseDataInnerUpdatesInner.to_json())

# convert the object into a dict
get_rate_jobs_response_data_inner_updates_inner_dict = get_rate_jobs_response_data_inner_updates_inner_instance.to_dict()
# create an instance of GetRateJobsResponseDataInnerUpdatesInner from a dict
get_rate_jobs_response_data_inner_updates_inner_from_dict = GetRateJobsResponseDataInnerUpdatesInner.from_dict(get_rate_jobs_response_data_inner_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


