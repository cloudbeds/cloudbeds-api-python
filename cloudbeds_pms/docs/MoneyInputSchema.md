# MoneyInputSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** | Amount in the smallest representable units of the currency (e.g., cents for USD) | 
**currency_code** | **str** | ISO 4217 currency code | 

## Example

```python
from cloudbeds_pms.models.money_input_schema import MoneyInputSchema

# TODO update the JSON string below
json = "{}"
# create an instance of MoneyInputSchema from a JSON string
money_input_schema_instance = MoneyInputSchema.from_json(json)
# print the JSON string representation of the object
print(MoneyInputSchema.to_json())

# convert the object into a dict
money_input_schema_dict = money_input_schema_instance.to_dict()
# create an instance of MoneyInputSchema from a dict
money_input_schema_from_dict = MoneyInputSchema.from_dict(money_input_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


