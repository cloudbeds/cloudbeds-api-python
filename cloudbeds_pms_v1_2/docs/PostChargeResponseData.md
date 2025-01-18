# PostChargeResponseData

Payment details

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_id** | **str** | Payment ID | [optional] 
**transaction_id** | **str** | Transaction ID | [optional] 
**payment_status** | **str** | the status of the payment, could be &#39;pending&#39; if the payment requires a next action | [optional] 
**payment_type** | **str** | detected payment type. Ex: &#39;cards&#39;, &#39;oxxo&#39; | [optional] 
**next_action** | [**PostChargeResponseDataNextAction**](PostChargeResponseDataNextAction.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_charge_response_data import PostChargeResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of PostChargeResponseData from a JSON string
post_charge_response_data_instance = PostChargeResponseData.from_json(json)
# print the JSON string representation of the object
print(PostChargeResponseData.to_json())

# convert the object into a dict
post_charge_response_data_dict = post_charge_response_data_instance.to_dict()
# create an instance of PostChargeResponseData from a dict
post_charge_response_data_from_dict = PostChargeResponseData.from_dict(post_charge_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


