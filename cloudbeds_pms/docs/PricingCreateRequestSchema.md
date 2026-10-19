# PricingCreateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Rate ID. | 
**pricing** | [**List[PricingCreateRequestSchemaPricingInner]**](PricingCreateRequestSchemaPricingInner.md) | List of pricing items to create. | 

## Example

```python
from cloudbeds_pms.models.pricing_create_request_schema import PricingCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PricingCreateRequestSchema from a JSON string
pricing_create_request_schema_instance = PricingCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PricingCreateRequestSchema.to_json())

# convert the object into a dict
pricing_create_request_schema_dict = pricing_create_request_schema_instance.to_dict()
# create an instance of PricingCreateRequestSchema from a dict
pricing_create_request_schema_from_dict = PricingCreateRequestSchema.from_dict(pricing_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


