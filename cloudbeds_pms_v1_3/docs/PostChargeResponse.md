# PostChargeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Returns if the request was completed | [optional] 
**data** | [**PostChargeResponseData**](PostChargeResponseData.md) |  | [optional] 

## Example

```python
from cloudbeds_pms_v1_3.models.post_charge_response import PostChargeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PostChargeResponse from a JSON string
post_charge_response_instance = PostChargeResponse.from_json(json)
# print the JSON string representation of the object
print(PostChargeResponse.to_json())

# convert the object into a dict
post_charge_response_dict = post_charge_response_instance.to_dict()
# create an instance of PostChargeResponse from a dict
post_charge_response_from_dict = PostChargeResponse.from_dict(post_charge_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


