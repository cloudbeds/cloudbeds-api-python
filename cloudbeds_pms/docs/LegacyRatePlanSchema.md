# LegacyRatePlanSchema

An earlier, narrower assignable-rooms rate-plan shape: rateId is an integer, rateTotal is a raw float, and detailedRates is not present. See RatePlanSchema for the current shape.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rate_id** | **int** |  | 
**rate_type** | **str** | Rate plan type. | 
**name** | **str** |  | 
**rate_total** | **float** | Total for the stay (sum of nightly rates). | 
**package_id** | **int** |  | [optional] 
**package_name** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.legacy_rate_plan_schema import LegacyRatePlanSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyRatePlanSchema from a JSON string
legacy_rate_plan_schema_instance = LegacyRatePlanSchema.from_json(json)
# print the JSON string representation of the object
print(LegacyRatePlanSchema.to_json())

# convert the object into a dict
legacy_rate_plan_schema_dict = legacy_rate_plan_schema_instance.to_dict()
# create an instance of LegacyRatePlanSchema from a dict
legacy_rate_plan_schema_from_dict = LegacyRatePlanSchema.from_dict(legacy_rate_plan_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


