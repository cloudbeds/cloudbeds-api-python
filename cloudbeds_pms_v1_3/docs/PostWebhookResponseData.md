# PostWebhookResponseData

Subscription details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription_id** | **str** | Subscription ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_webhook_response_data import PostWebhookResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostWebhookResponseData from a JSON string
post_webhook_response_data_instance = PostWebhookResponseData.from_json(json)
# print the JSON string representation of the object
print(PostWebhookResponseData.to_json())

# convert the object into a dict
post_webhook_response_data_dict = post_webhook_response_data_instance.to_dict()
# create an instance of PostWebhookResponseData from a dict
post_webhook_response_data_from_dict = PostWebhookResponseData.from_dict(post_webhook_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


