# GetWebhooksResponseDataInnerOwner

Subscription Owner object (User, API Client, etc, and it's ID)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Subscription Owner type | [optional] 
**id** | **str** | Subscription Owner ID | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_webhooks_response_data_inner_owner import GetWebhooksResponseDataInnerOwner

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhooksResponseDataInnerOwner from a JSON string
get_webhooks_response_data_inner_owner_instance = GetWebhooksResponseDataInnerOwner.from_json(json)
# print the JSON string representation of the object
print(GetWebhooksResponseDataInnerOwner.to_json())

# convert the object into a dict
get_webhooks_response_data_inner_owner_dict = get_webhooks_response_data_inner_owner_instance.to_dict()
# create an instance of GetWebhooksResponseDataInnerOwner from a dict
get_webhooks_response_data_inner_owner_from_dict = GetWebhooksResponseDataInnerOwner.from_dict(get_webhooks_response_data_inner_owner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


