# AiAvailabilityResponseSchema

A schema.org `LodgingBusiness` whose `containsPlace` lists every room type that can host the stay, each with one tax-inclusive `Offer`. Room types with no unit left are omitted rather than marked out of stock. Money is expressed as schema.org `price` (a decimal number) plus `priceCurrency`, not as the Public API minor-unit `amount` object: the document has to validate against the vocabulary AI agents already parse. Decimal places follow the currency (JPY 0, USD 2, BHD 3).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | JSON-LD vocabulary the document is expressed in. | 
**type** | **str** |  | 
**id** | **str** | Same URL the property metadata endpoint publishes for the property. | 
**name** | **str** |  | 
**availability_search** | [**AiAvailabilityResponseSchemaAvailabilitySearch**](AiAvailabilityResponseSchemaAvailabilitySearch.md) |  | 
**contains_place** | [**List[AiAvailabilityHotelRoomSchema]**](AiAvailabilityHotelRoomSchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.ai_availability_response_schema import AiAvailabilityResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AiAvailabilityResponseSchema from a JSON string
ai_availability_response_schema_instance = AiAvailabilityResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AiAvailabilityResponseSchema.to_json())

# convert the object into a dict
ai_availability_response_schema_dict = ai_availability_response_schema_instance.to_dict()
# create an instance of AiAvailabilityResponseSchema from a dict
ai_availability_response_schema_from_dict = AiAvailabilityResponseSchema.from_dict(ai_availability_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


