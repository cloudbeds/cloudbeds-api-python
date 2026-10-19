# AiAvailabilityOfferSchemaPriceSpecificationPriceComponentInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**name** | **str** |  | 
**price** | **float** |  | 
**price_currency** | **str** |  | 
**price_component_type** | **str** | Absent on the base rate. | [optional] 

## Example

```python
from cloudbeds_pms.models.ai_availability_offer_schema_price_specification_price_component_inner import AiAvailabilityOfferSchemaPriceSpecificationPriceComponentInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiAvailabilityOfferSchemaPriceSpecificationPriceComponentInner from a JSON string
ai_availability_offer_schema_price_specification_price_component_inner_instance = AiAvailabilityOfferSchemaPriceSpecificationPriceComponentInner.from_json(json)
# print the JSON string representation of the object
print(AiAvailabilityOfferSchemaPriceSpecificationPriceComponentInner.to_json())

# convert the object into a dict
ai_availability_offer_schema_price_specification_price_component_inner_dict = ai_availability_offer_schema_price_specification_price_component_inner_instance.to_dict()
# create an instance of AiAvailabilityOfferSchemaPriceSpecificationPriceComponentInner from a dict
ai_availability_offer_schema_price_specification_price_component_inner_from_dict = AiAvailabilityOfferSchemaPriceSpecificationPriceComponentInner.from_dict(ai_availability_offer_schema_price_specification_price_component_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


