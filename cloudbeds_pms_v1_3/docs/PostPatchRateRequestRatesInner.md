# PostPatchRateRequestRatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_id** | **str** | Rate ID | [optional] 
**interval** | [**PostPatchRateRequestRatesInnerInterval**](PostPatchRateRequestRatesInnerInterval.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_patch_rate_request_rates_inner import PostPatchRateRequestRatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of PostPatchRateRequestRatesInner from a JSON string
post_patch_rate_request_rates_inner_instance = PostPatchRateRequestRatesInner.from_json(json)
# print the JSON string representation of the object
print(PostPatchRateRequestRatesInner.to_json())

# convert the object into a dict
post_patch_rate_request_rates_inner_dict = post_patch_rate_request_rates_inner_instance.to_dict()
# create an instance of PostPatchRateRequestRatesInner from a dict
post_patch_rate_request_rates_inner_from_dict = PostPatchRateRequestRatesInner.from_dict(post_patch_rate_request_rates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


