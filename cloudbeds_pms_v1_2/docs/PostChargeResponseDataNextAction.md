# PostChargeResponseDataNextAction

not set if no next action is required

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of next action required. Ex: &#39;redirect&#39; | [optional] 
**details** | [**PostChargeResponseDataNextActionDetails**](PostChargeResponseDataNextActionDetails.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_2.models.post_charge_response_data_next_action import PostChargeResponseDataNextAction

# TODO update the JSON string below
json = "{}"
# create an instance of PostChargeResponseDataNextAction from a JSON string
post_charge_response_data_next_action_instance = PostChargeResponseDataNextAction.from_json(json)
# print the JSON string representation of the object
print(PostChargeResponseDataNextAction.to_json())

# convert the object into a dict
post_charge_response_data_next_action_dict = post_charge_response_data_next_action_instance.to_dict()
# create an instance of PostChargeResponseDataNextAction from a dict
post_charge_response_data_next_action_from_dict = PostChargeResponseDataNextAction.from_dict(post_charge_response_data_next_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


