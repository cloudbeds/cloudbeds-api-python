# GetWebhooksResponseDataInnerSubscriptionData

Data used on the subscription. For webhooks, just the endpoint URL.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | The endpoint | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_webhooks_response_data_inner_subscription_data import GetWebhooksResponseDataInnerSubscriptionData

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhooksResponseDataInnerSubscriptionData from a JSON string
get_webhooks_response_data_inner_subscription_data_instance = GetWebhooksResponseDataInnerSubscriptionData.from_json(json)
# print the JSON string representation of the object
print(GetWebhooksResponseDataInnerSubscriptionData.to_json())

# convert the object into a dict
get_webhooks_response_data_inner_subscription_data_dict = get_webhooks_response_data_inner_subscription_data_instance.to_dict()
# create an instance of GetWebhooksResponseDataInnerSubscriptionData from a dict
get_webhooks_response_data_inner_subscription_data_from_dict = GetWebhooksResponseDataInnerSubscriptionData.from_dict(get_webhooks_response_data_inner_subscription_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


