# PricingResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Pricing ID. | 
**age_group_id** | **str** | Age group ID. | 
**rate_interval_id** | **str** | Rate interval ID. | 
**is_extra_guests_pricing** | **bool** | Whether this is extra guests pricing. | 
**extra_guests_type** | **str** | Extra guests pricing type. | [optional] 
**extra_guests_number** | **int** | Guest number for per-guest pricing. | [optional] 
**days** | [**List[PricingDayResponseSchema]**](PricingDayResponseSchema.md) | Day pricing data. | 

## Example

```python
from cloudbeds_pms.models.pricing_response_schema import PricingResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PricingResponseSchema from a JSON string
pricing_response_schema_instance = PricingResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PricingResponseSchema.to_json())

# convert the object into a dict
pricing_response_schema_dict = pricing_response_schema_instance.to_dict()
# create an instance of PricingResponseSchema from a dict
pricing_response_schema_from_dict = PricingResponseSchema.from_dict(pricing_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


