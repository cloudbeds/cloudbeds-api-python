# GetWebhooksResponseDataInnerEvent

Event for which the subscription was created

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | **str** | Entity which the event belongs to | [optional] 
**action** | **str** | Action which the event represents | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.get_webhooks_response_data_inner_event import GetWebhooksResponseDataInnerEvent

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebhooksResponseDataInnerEvent from a JSON string
get_webhooks_response_data_inner_event_instance = GetWebhooksResponseDataInnerEvent.from_json(json)
# print the JSON string representation of the object
print(GetWebhooksResponseDataInnerEvent.to_json())

# convert the object into a dict
get_webhooks_response_data_inner_event_dict = get_webhooks_response_data_inner_event_instance.to_dict()
# create an instance of GetWebhooksResponseDataInnerEvent from a dict
get_webhooks_response_data_inner_event_from_dict = GetWebhooksResponseDataInnerEvent.from_dict(get_webhooks_response_data_inner_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


