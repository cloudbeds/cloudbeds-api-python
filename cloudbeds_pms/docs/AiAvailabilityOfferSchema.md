# AiAvailabilityOfferSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**availability** | **str** |  | 
**price_specification** | [**AiAvailabilityOfferSchemaPriceSpecification**](AiAvailabilityOfferSchemaPriceSpecification.md) |  | 
**valid_from** | **date** |  | 
**valid_through** | **date** |  | 
**url** | **str** | Deep link into the booking engine with the stay pre-filled. | 

## Example

```python
from cloudbeds_pms.models.ai_availability_offer_schema import AiAvailabilityOfferSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AiAvailabilityOfferSchema from a JSON string
ai_availability_offer_schema_instance = AiAvailabilityOfferSchema.from_json(json)
# print the JSON string representation of the object
print(AiAvailabilityOfferSchema.to_json())

# convert the object into a dict
ai_availability_offer_schema_dict = ai_availability_offer_schema_instance.to_dict()
# create an instance of AiAvailabilityOfferSchema from a dict
ai_availability_offer_schema_from_dict = AiAvailabilityOfferSchema.from_dict(ai_availability_offer_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


