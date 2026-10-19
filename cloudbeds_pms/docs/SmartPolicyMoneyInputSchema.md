# SmartPolicyMoneyInputSchema

Money input as per the REST API Modeling Specification: amount in the smallest representable units of the currency, paired with an ISO 4217 currency code.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount in the smallest representable units of the currency (e.g., cents for USD). | 
**currency_code** | **str** | ISO 4217 currency code. | 

## Example

```python
from cloudbeds_pms.models.smart_policy_money_input_schema import SmartPolicyMoneyInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SmartPolicyMoneyInputSchema from a JSON string
smart_policy_money_input_schema_instance = SmartPolicyMoneyInputSchema.from_json(json)
# print the JSON string representation of the object
print(SmartPolicyMoneyInputSchema.to_json())

# convert the object into a dict
smart_policy_money_input_schema_dict = smart_policy_money_input_schema_instance.to_dict()
# create an instance of SmartPolicyMoneyInputSchema from a dict
smart_policy_money_input_schema_from_dict = SmartPolicyMoneyInputSchema.from_dict(smart_policy_money_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


