# NightlyRateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **date** |  | 
**rate** | [**MoneySchema**](MoneySchema.md) |  | 
**adults** | [**MoneySchema**](MoneySchema.md) |  | 
**kids** | [**MoneySchema**](MoneySchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.nightly_rate_schema import NightlyRateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of NightlyRateSchema from a JSON string
nightly_rate_schema_instance = NightlyRateSchema.from_json(json)
# print the JSON string representation of the object
print(NightlyRateSchema.to_json())

# convert the object into a dict
nightly_rate_schema_dict = nightly_rate_schema_instance.to_dict()
# create an instance of NightlyRateSchema from a dict
nightly_rate_schema_from_dict = NightlyRateSchema.from_dict(nightly_rate_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


