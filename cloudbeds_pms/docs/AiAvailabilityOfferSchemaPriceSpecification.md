# AiAvailabilityOfferSchemaPriceSpecification

Tax-inclusive total for the whole stay, itemized in `priceComponent`. Components always sum to `price`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**price** | **float** |  | 
**price_currency** | **str** |  | 
**unit_text** | **str** |  | 
**reference_quantity** | [**AiAvailabilityOfferSchemaPriceSpecificationReferenceQuantity**](AiAvailabilityOfferSchemaPriceSpecificationReferenceQuantity.md) |  | 
**price_component** | [**List[AiAvailabilityOfferSchemaPriceSpecificationPriceComponentInner]**](AiAvailabilityOfferSchemaPriceSpecificationPriceComponentInner.md) |  | 

## Example

```python
from cloudbeds_pms.models.ai_availability_offer_schema_price_specification import AiAvailabilityOfferSchemaPriceSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of AiAvailabilityOfferSchemaPriceSpecification from a JSON string
ai_availability_offer_schema_price_specification_instance = AiAvailabilityOfferSchemaPriceSpecification.from_json(json)
# print the JSON string representation of the object
print(AiAvailabilityOfferSchemaPriceSpecification.to_json())

# convert the object into a dict
ai_availability_offer_schema_price_specification_dict = ai_availability_offer_schema_price_specification_instance.to_dict()
# create an instance of AiAvailabilityOfferSchemaPriceSpecification from a dict
ai_availability_offer_schema_price_specification_from_dict = AiAvailabilityOfferSchemaPriceSpecification.from_dict(ai_availability_offer_schema_price_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


