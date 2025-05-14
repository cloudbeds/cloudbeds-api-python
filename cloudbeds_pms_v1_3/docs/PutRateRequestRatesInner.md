# PutRateRequestRatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_id** | **str** | Rate ID | [optional] 
**interval** | [**List[PutRateRequestRatesInnerIntervalInner]**](PutRateRequestRatesInnerIntervalInner.md) | Rate update details | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.put_rate_request_rates_inner import PutRateRequestRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PutRateRequestRatesInner from a JSON string
put_rate_request_rates_inner_instance = PutRateRequestRatesInner.from_json(json)
# print the JSON string representation of the object
print(PutRateRequestRatesInner.to_json())

# convert the object into a dict
put_rate_request_rates_inner_dict = put_rate_request_rates_inner_instance.to_dict()
# create an instance of PutRateRequestRatesInner from a dict
put_rate_request_rates_inner_from_dict = PutRateRequestRatesInner.from_dict(put_rate_request_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


