# PostChargeResponseDataNextActionDetails

The details of the next action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL to redirect the user to | [optional] 
**method** | **str** | The HTTP method to use when redirecting the user | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_charge_response_data_next_action_details import PostChargeResponseDataNextActionDetails

# TODO update the JSON string below
json = "{}"
# create an instance of PostChargeResponseDataNextActionDetails from a JSON string
post_charge_response_data_next_action_details_instance = PostChargeResponseDataNextActionDetails.from_json(json)
# print the JSON string representation of the object
print(PostChargeResponseDataNextActionDetails.to_json())

# convert the object into a dict
post_charge_response_data_next_action_details_dict = post_charge_response_data_next_action_details_instance.to_dict()
# create an instance of PostChargeResponseDataNextActionDetails from a dict
post_charge_response_data_next_action_details_from_dict = PostChargeResponseDataNextActionDetails.from_dict(post_charge_response_data_next_action_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


