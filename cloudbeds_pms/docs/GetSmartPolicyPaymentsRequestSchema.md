# GetSmartPolicyPaymentsRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reservation_id** | **str** | Reservation ID. | 

## Example

```python
from cloudbeds_pms.models.get_smart_policy_payments_request_schema import GetSmartPolicyPaymentsRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetSmartPolicyPaymentsRequestSchema from a JSON string
get_smart_policy_payments_request_schema_instance = GetSmartPolicyPaymentsRequestSchema.from_json(json)
# print the JSON string representation of the object
print(GetSmartPolicyPaymentsRequestSchema.to_json())

# convert the object into a dict
get_smart_policy_payments_request_schema_dict = get_smart_policy_payments_request_schema_instance.to_dict()
# create an instance of GetSmartPolicyPaymentsRequestSchema from a dict
get_smart_policy_payments_request_schema_from_dict = GetSmartPolicyPaymentsRequestSchema.from_dict(get_smart_policy_payments_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


