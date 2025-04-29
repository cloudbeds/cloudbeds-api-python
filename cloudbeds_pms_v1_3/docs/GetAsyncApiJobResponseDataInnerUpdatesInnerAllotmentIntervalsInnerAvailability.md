# GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerAvailability

Interval availability data by day in interval

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** | Day within interval | [optional] 
**block_remaining** | **int** | Number of units remaining for the room type for this day | [optional] 
**block_allotted** | **int** | Total number of units available for the room type for this day | [optional] 
**block_confirmed** | **int** | Number of units booked for the room type for this day | [optional] 
**rate** | **str** | the price | [optional] 
**guest_pricing** | [**GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerAvailabilityGuestPricing**](GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerAvailabilityGuestPricing.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner_availability import GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerAvailability from a JSON string
get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner_availability_instance = GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerAvailability.from_json(json)
# print the JSON string representation of the object
print(GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerAvailability.to_json())

# convert the object into a dict
get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner_availability_dict = get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner_availability_instance.to_dict()
# create an instance of GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerAvailability from a dict
get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner_availability_from_dict = GetAsyncApiJobResponseDataInnerUpdatesInnerAllotmentIntervalsInnerAvailability.from_dict(get_async_api_job_response_data_inner_updates_inner_allotment_intervals_inner_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


