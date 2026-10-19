# DisableSmartPolicyResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**matched** | **int** | Count of booking room-policy rows found for the reservation. | 
**modified** | **int** | Count of rows whose state actually flipped. 0 with a non-zero \&quot;matched\&quot; means Smart Policy was already off for the reservation (the call is idempotent). | 

## Example

```python
from cloudbeds_pms.models.disable_smart_policy_response_schema import DisableSmartPolicyResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DisableSmartPolicyResponseSchema from a JSON string
disable_smart_policy_response_schema_instance = DisableSmartPolicyResponseSchema.from_json(json)
# print the JSON string representation of the object
print(DisableSmartPolicyResponseSchema.to_json())

# convert the object into a dict
disable_smart_policy_response_schema_dict = disable_smart_policy_response_schema_instance.to_dict()
# create an instance of DisableSmartPolicyResponseSchema from a dict
disable_smart_policy_response_schema_from_dict = DisableSmartPolicyResponseSchema.from_dict(disable_smart_policy_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


