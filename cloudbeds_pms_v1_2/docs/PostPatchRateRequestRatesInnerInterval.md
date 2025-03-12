# PostPatchRateRequestRatesInnerInterval

Rate update details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Interval Start date. Format: YYYY-MM-DD | [optional] 
**end_date** | **date** | Interval End date. Format: YYYY-MM-DD | [optional] 
**rate** | **float** | Base rate for the selected date | [optional] 
**max_los** | **int** | Maximum length of stay for the selected date. | [optional] 
**min_los** | **int** | Minimum length of stay for the selected date. | [optional] 
**closed_to_arrival** | **bool** | Whether it is closed to arrival. | [optional] 
**closed_to_departure** | **bool** | Whether it is closed to departure. | [optional] 
**cut_off** | **int** | Cut off time for the selected date. | [optional] 
**last_minute_booking** | **int** | Last minute bookings. | [optional] 
**guest_pricing** | [**PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing**](PostCreateAllotmentBlockRequestAllotmentIntervalsInnerAvailabilityInnerGuestPricing.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_patch_rate_request_rates_inner_interval import PostPatchRateRequestRatesInnerInterval

# TODO update the JSON string below
json = "{}"
# create an instance of PostPatchRateRequestRatesInnerInterval from a JSON string
post_patch_rate_request_rates_inner_interval_instance = PostPatchRateRequestRatesInnerInterval.from_json(json)
# print the JSON string representation of the object
print(PostPatchRateRequestRatesInnerInterval.to_json())

# convert the object into a dict
post_patch_rate_request_rates_inner_interval_dict = post_patch_rate_request_rates_inner_interval_instance.to_dict()
# create an instance of PostPatchRateRequestRatesInnerInterval from a dict
post_patch_rate_request_rates_inner_interval_from_dict = PostPatchRateRequestRatesInnerInterval.from_dict(post_patch_rate_request_rates_inner_interval_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


