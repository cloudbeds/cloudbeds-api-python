# PricingCreateRequestSchemaPricingInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_group_id** | **int** | Age group ID. | 
**interval_id** | **int** | Rate interval ID. | 
**is_extra_guests_pricing** | **bool** | Whether this is extra guests pricing. Only the adult age group can have base pricing (false); child and infant age groups take extra guests pricing only, and a base pricing entry for one is ignored. | 
**extra_guests_type** | **str** | Extra guests pricing type. | [optional] 
**guest_number** | **int** | Guest number for per-guest pricing. | [optional] 
**days** | [**List[PricingCreateRequestSchemaPricingInnerDaysInner]**](PricingCreateRequestSchemaPricingInnerDaysInner.md) |  | 

## Example

```python
from cloudbeds_pms.models.pricing_create_request_schema_pricing_inner import PricingCreateRequestSchemaPricingInner

# TODO update the JSON string below
json = "{}"
# create an instance of PricingCreateRequestSchemaPricingInner from a JSON string
pricing_create_request_schema_pricing_inner_instance = PricingCreateRequestSchemaPricingInner.from_json(json)
# print the JSON string representation of the object
print(PricingCreateRequestSchemaPricingInner.to_json())

# convert the object into a dict
pricing_create_request_schema_pricing_inner_dict = pricing_create_request_schema_pricing_inner_instance.to_dict()
# create an instance of PricingCreateRequestSchemaPricingInner from a dict
pricing_create_request_schema_pricing_inner_from_dict = PricingCreateRequestSchemaPricingInner.from_dict(pricing_create_request_schema_pricing_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


