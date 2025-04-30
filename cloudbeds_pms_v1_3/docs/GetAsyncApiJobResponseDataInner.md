# GetAsyncApiJobResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_reference_id** | **str** | Reference ID for the job created for this update.  This can be used to track success of the batch for this rate update. See getRateJobs or the rate:batch_job | [optional] 
**date_created** | **date** | Rate Job creation datetime | [optional] 
**status** | **str** | Status of the Rate Job. in_progress - job is processing. completed - job has completed successfully. error - there was an error with 1 or more updates requested in this job. Allowed values: in_progressgu, completed, error | [optional] 
**updates** | [**List[GetAsyncApiJobResponseDataInnerUpdatesInner]**](GetAsyncApiJobResponseDataInnerUpdatesInner.md) | Array of actions produced from this job | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_async_api_job_response_data_inner import GetAsyncApiJobResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAsyncApiJobResponseDataInner from a JSON string
get_async_api_job_response_data_inner_instance = GetAsyncApiJobResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetAsyncApiJobResponseDataInner.to_json())

# convert the object into a dict
get_async_api_job_response_data_inner_dict = get_async_api_job_response_data_inner_instance.to_dict()
# create an instance of GetAsyncApiJobResponseDataInner from a dict
get_async_api_job_response_data_inner_from_dict = GetAsyncApiJobResponseDataInner.from_dict(get_async_api_job_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


