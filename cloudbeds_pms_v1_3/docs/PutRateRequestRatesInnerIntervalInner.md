# PutRateRequestRatesInnerIntervalInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **date** | Interval Start date. Format: YYYY-MM-DD | [optional] 
**end_date** | **date** | Interval End date. Format: YYYY-MM-DD | [optional] 
**rate** | **float** | Base rate for the selected date | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.put_rate_request_rates_inner_interval_inner import PutRateRequestRatesInnerIntervalInner

# TODO update the JSON string below
json = "{}"
# create an instance of PutRateRequestRatesInnerIntervalInner from a JSON string
put_rate_request_rates_inner_interval_inner_instance = PutRateRequestRatesInnerIntervalInner.from_json(json)
# print the JSON string representation of the object
print(PutRateRequestRatesInnerIntervalInner.to_json())

# convert the object into a dict
put_rate_request_rates_inner_interval_inner_dict = put_rate_request_rates_inner_interval_inner_instance.to_dict()
# create an instance of PutRateRequestRatesInnerIntervalInner from a dict
put_rate_request_rates_inner_interval_inner_from_dict = PutRateRequestRatesInnerIntervalInner.from_dict(put_rate_request_rates_inner_interval_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


