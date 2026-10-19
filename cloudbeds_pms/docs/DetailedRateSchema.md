# DetailedRateSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | Night date (YYYY-MM-DD) | 
**rate** | **str** | Base room rate for this night in minor currency units (e.g. 15000 &#x3D; $150.00) | 
**adults** | **str** | Adult surcharge for this night in minor currency units (e.g. 2500 &#x3D; $25.00) | [optional] 
**children** | **str** | Child surcharge for this night in minor currency units (e.g. 1000 &#x3D; $10.00) | [optional] 

## Example

```python
from cloudbeds_pms.models.detailed_rate_schema import DetailedRateSchema

# TODO update the JSON string below
json = "{}"
# create an instance of DetailedRateSchema from a JSON string
detailed_rate_schema_instance = DetailedRateSchema.from_json(json)
# print the JSON string representation of the object
print(DetailedRateSchema.to_json())

# convert the object into a dict
detailed_rate_schema_dict = detailed_rate_schema_instance.to_dict()
# create an instance of DetailedRateSchema from a dict
detailed_rate_schema_from_dict = DetailedRateSchema.from_dict(detailed_rate_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


