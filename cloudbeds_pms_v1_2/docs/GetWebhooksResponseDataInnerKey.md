# GetWebhooksResponseDataInnerKey

Subscription Key object (User, Property or Association and it's ID)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Subscription Key type | [optional] 
**id** | **str** | Subscription Key ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_webhooks_response_data_inner_key import GetWebhooksResponseDataInnerKey

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhooksResponseDataInnerKey from a JSON string
get_webhooks_response_data_inner_key_instance = GetWebhooksResponseDataInnerKey.from_json(json)
# print the JSON string representation of the object
print(GetWebhooksResponseDataInnerKey.to_json())

# convert the object into a dict
get_webhooks_response_data_inner_key_dict = get_webhooks_response_data_inner_key_instance.to_dict()
# create an instance of GetWebhooksResponseDataInnerKey from a dict
get_webhooks_response_data_inner_key_from_dict = GetWebhooksResponseDataInnerKey.from_dict(get_webhooks_response_data_inner_key_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


