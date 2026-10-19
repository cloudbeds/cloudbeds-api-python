# GetWebhooksResponseDataInnerAuthHeader

Present only when the subscription was registered with an auth header.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Header name. The value is never returned. | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.get_webhooks_response_data_inner_auth_header import GetWebhooksResponseDataInnerAuthHeader

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhooksResponseDataInnerAuthHeader from a JSON string
get_webhooks_response_data_inner_auth_header_instance = GetWebhooksResponseDataInnerAuthHeader.from_json(json)
# print the JSON string representation of the object
print(GetWebhooksResponseDataInnerAuthHeader.to_json())

# convert the object into a dict
get_webhooks_response_data_inner_auth_header_dict = get_webhooks_response_data_inner_auth_header_instance.to_dict()
# create an instance of GetWebhooksResponseDataInnerAuthHeader from a dict
get_webhooks_response_data_inner_auth_header_from_dict = GetWebhooksResponseDataInnerAuthHeader.from_dict(get_webhooks_response_data_inner_auth_header_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


