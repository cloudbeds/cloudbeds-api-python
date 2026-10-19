# DepositConfigSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | How deposit is calculated | 
**value** | **str** | Deposit value in minor currency units. Required for percentage and fixed types. For percentage: \&quot;5000\&quot; &#x3D; 50.00%. For fixed: \&quot;5000\&quot; &#x3D; $50.00. | [optional] 

## Example

```python
from cloudbeds_pms.models.deposit_config_schema import DepositConfigSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DepositConfigSchema from a JSON string
deposit_config_schema_instance = DepositConfigSchema.from_json(json)
# print the JSON string representation of the object
print(DepositConfigSchema.to_json())

# convert the object into a dict
deposit_config_schema_dict = deposit_config_schema_instance.to_dict()
# create an instance of DepositConfigSchema from a dict
deposit_config_schema_from_dict = DepositConfigSchema.from_dict(deposit_config_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


