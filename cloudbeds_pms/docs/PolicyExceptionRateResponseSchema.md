# PolicyExceptionRateResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_id** | **str** | Package/rate plan ID. 0 &#x3D; base rate. | [optional] 
**room_type_id** | **str** | Room type ID. | [optional] 

## Example

```python
from cloudbeds_pms.models.policy_exception_rate_response_schema import PolicyExceptionRateResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyExceptionRateResponseSchema from a JSON string
policy_exception_rate_response_schema_instance = PolicyExceptionRateResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PolicyExceptionRateResponseSchema.to_json())

# convert the object into a dict
policy_exception_rate_response_schema_dict = policy_exception_rate_response_schema_instance.to_dict()
# create an instance of PolicyExceptionRateResponseSchema from a dict
policy_exception_rate_response_schema_from_dict = PolicyExceptionRateResponseSchema.from_dict(policy_exception_rate_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


