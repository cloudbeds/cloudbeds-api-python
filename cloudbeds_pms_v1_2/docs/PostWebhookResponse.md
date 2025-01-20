# PostWebhookResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request could be completed | [optional] 
**data** | [**PostWebhookResponseData**](PostWebhookResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_webhook_response import PostWebhookResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostWebhookResponse from a JSON string
post_webhook_response_instance = PostWebhookResponse.from_json(json)
# print the JSON string representation of the object
print(PostWebhookResponse.to_json())

# convert the object into a dict
post_webhook_response_dict = post_webhook_response_instance.to_dict()
# create an instance of PostWebhookResponse from a dict
post_webhook_response_from_dict = PostWebhookResponse.from_dict(post_webhook_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


