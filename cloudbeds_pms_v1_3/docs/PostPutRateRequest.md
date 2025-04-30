# PostPutRateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rates** | [**List[PostPutRateRequestRatesInner]**](PostPutRateRequestRatesInner.md) | Array of rates to update | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_put_rate_request import PostPutRateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPutRateRequest from a JSON string
post_put_rate_request_instance = PostPutRateRequest.from_json(json)
# print the JSON string representation of the object
print(PostPutRateRequest.to_json())

# convert the object into a dict
post_put_rate_request_dict = post_put_rate_request_instance.to_dict()
# create an instance of PostPutRateRequest from a dict
post_put_rate_request_from_dict = PostPutRateRequest.from_dict(post_put_rate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


