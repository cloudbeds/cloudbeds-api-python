# PricingRateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rate ID. | 

## Example

```python
from cloudbeds_pms.models.pricing_rate_request_schema import PricingRateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PricingRateRequestSchema from a JSON string
pricing_rate_request_schema_instance = PricingRateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PricingRateRequestSchema.to_json())

# convert the object into a dict
pricing_rate_request_schema_dict = pricing_rate_request_schema_instance.to_dict()
# create an instance of PricingRateRequestSchema from a dict
pricing_rate_request_schema_from_dict = PricingRateRequestSchema.from_dict(pricing_rate_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


