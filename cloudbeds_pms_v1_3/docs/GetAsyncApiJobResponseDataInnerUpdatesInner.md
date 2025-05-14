# GetAsyncApiJobResponseDataInnerUpdatesInner


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
**property_id** | **str** | Property ID associated to the allotment block | [optional] 
**allotment_block_code** | **str** | Allotment block code | [optional] 
**allotment_block_status** | **str** | Allotment block status | [optional] 
**allotment_block_name** | **str** | Allotment block name | [optional] 
**allotment_block_id** | **str** | Allotment block ID | [optional] 
**rate_type** | **str** | Rate type for the allotment block | [optional] 
**rate_plan_id** | **str** | Rate plan ID if applicable | [optional] 
**allotment_type** | **str** | the type of allotment block | [optional] 
**group_id** | **str** | Group profile ID associated to the allotment block | [optional] 
**groupcode** | **str** | Group profile code associated to the allotment block | [optional] 
**is_auto_release** | **bool** | If the allotment block is configured for auto-release | [optional] 
**auto_release** | [**GetAsyncApiJobResponseDataInnerUpdatesInnerAutoRelease**](GetAsyncApiJobResponseDataInnerUpdatesInnerAutoRelease.md) |  | [optional] 
**allotment_intervals** | [**List[GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInner]**](GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInner.md) | array of interval data by room type | [optional] 
**message** | **str** | Error message | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_async_api_job_response_data_inner_updates_inner import GetAsyncApiJobResponseDataInnerUpdatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAsyncApiJobResponseDataInnerUpdatesInner from a JSON string
get_async_api_job_response_data_inner_updates_inner_instance = GetAsyncApiJobResponseDataInnerUpdatesInner.from_json(json)
# print the JSON string representation of the object
print(GetAsyncApiJobResponseDataInnerUpdatesInner.to_json())

# convert the object into a dict
get_async_api_job_response_data_inner_updates_inner_dict = get_async_api_job_response_data_inner_updates_inner_instance.to_dict()
# create an instance of GetAsyncApiJobResponseDataInnerUpdatesInner from a dict
get_async_api_job_response_data_inner_updates_inner_from_dict = GetAsyncApiJobResponseDataInnerUpdatesInner.from_dict(get_async_api_job_response_data_inner_updates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


