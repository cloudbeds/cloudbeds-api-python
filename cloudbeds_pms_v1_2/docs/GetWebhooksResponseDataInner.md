# GetWebhooksResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Subscription ID | [optional] 
**key** | [**GetWebhooksResponseDataInnerKey**](GetWebhooksResponseDataInnerKey.md) |  | [optional] 
**event** | [**GetWebhooksResponseDataInnerEvent**](GetWebhooksResponseDataInnerEvent.md) |  | [optional] 
**owner** | [**GetWebhooksResponseDataInnerOwner**](GetWebhooksResponseDataInnerOwner.md) |  | [optional] 
**subscription_type** | **str** | Subscription Type (Webhook) | [optional] 
**subscription_data** | [**GetWebhooksResponseDataInnerSubscriptionData**](GetWebhooksResponseDataInnerSubscriptionData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_webhooks_response_data_inner import GetWebhooksResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhooksResponseDataInner from a JSON string
get_webhooks_response_data_inner_instance = GetWebhooksResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetWebhooksResponseDataInner.to_json())

# convert the object into a dict
get_webhooks_response_data_inner_dict = get_webhooks_response_data_inner_instance.to_dict()
# create an instance of GetWebhooksResponseDataInner from a dict
get_webhooks_response_data_inner_from_dict = GetWebhooksResponseDataInner.from_dict(get_webhooks_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


