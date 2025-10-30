# MoneySchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **str** |  | 
**currency_code** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.money_schema import MoneySchema

# TODO update the JSON string below
json = "{}"
# create an instance of MoneySchema from a JSON string
money_schema_instance = MoneySchema.from_json(json)
# print the JSON string representation of the object
print(MoneySchema.to_json())

# convert the object into a dict
money_schema_dict = money_schema_instance.to_dict()
# create an instance of MoneySchema from a dict
money_schema_from_dict = MoneySchema.from_dict(money_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


