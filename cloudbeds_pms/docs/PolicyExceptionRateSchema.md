# PolicyExceptionRateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**package_id** | **int** | Package/rate plan ID. Use 0 for base rate. | 
**room_type_id** | **int** | Room type ID. Required when packageId is 0 (base rate). | [optional] 

## Example

```python
from cloudbeds_pms.models.policy_exception_rate_schema import PolicyExceptionRateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyExceptionRateSchema from a JSON string
policy_exception_rate_schema_instance = PolicyExceptionRateSchema.from_json(json)
# print the JSON string representation of the object
print(PolicyExceptionRateSchema.to_json())

# convert the object into a dict
policy_exception_rate_schema_dict = policy_exception_rate_schema_instance.to_dict()
# create an instance of PolicyExceptionRateSchema from a dict
policy_exception_rate_schema_from_dict = PolicyExceptionRateSchema.from_dict(policy_exception_rate_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


