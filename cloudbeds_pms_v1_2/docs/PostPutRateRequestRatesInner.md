# PostPutRateRequestRatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_id** | **str** | Rate ID | [optional] 
**interval** | [**List[PostPutRateRequestRatesInnerIntervalInner]**](PostPutRateRequestRatesInnerIntervalInner.md) | Rate update details | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_put_rate_request_rates_inner import PostPutRateRequestRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostPutRateRequestRatesInner from a JSON string
post_put_rate_request_rates_inner_instance = PostPutRateRequestRatesInner.from_json(json)
# print the JSON string representation of the object
print(PostPutRateRequestRatesInner.to_json())

# convert the object into a dict
post_put_rate_request_rates_inner_dict = post_put_rate_request_rates_inner_instance.to_dict()
# create an instance of PostPutRateRequestRatesInner from a dict
post_put_rate_request_rates_inner_from_dict = PostPutRateRequestRatesInner.from_dict(post_put_rate_request_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


