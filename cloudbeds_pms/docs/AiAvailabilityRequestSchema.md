# AiAvailabilityRequestSchema

Query string of the AI availability search. Dates are ISO-8601 calendar dates (YYYY-MM-DD) and the departure day is not charged.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**DynamicFilterSchema**](DynamicFilterSchema.md) |  | [optional] 
**property_code** | **str** | Opaque alphanumeric property short code, as published in the &#x60;@id&#x60; URL returned by the property metadata endpoint. | 
**check_in** | **date** | Arrival date in YYYY-MM-DD format. Today or later in the property&#39;s time zone. | 
**check_out** | **date** | Departure date in YYYY-MM-DD format. Exclusive: the departure day is not charged. Must fall after checkIn, at most 730 nights later. | 
**adults** | **int** | Number of adults. Omitted, the offer is priced at the base occupancy of each room type. | [optional] 
**children** | **int** | Number of children. Omitted, the offer is priced without children. | [optional] 
**currency_code** | **str** | ISO 4217 code to price the response in. Omitted, prices are returned in the property&#39;s own currency. | [optional] 
**lang** | **str** | Preferred language. A hint, not a filter: translatable fields always carry the property&#39;s default language and English, and add this language when a translation exists. | [optional] 

## Example

```python
from cloudbeds_pms.models.ai_availability_request_schema import AiAvailabilityRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AiAvailabilityRequestSchema from a JSON string
ai_availability_request_schema_instance = AiAvailabilityRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AiAvailabilityRequestSchema.to_json())

# convert the object into a dict
ai_availability_request_schema_dict = ai_availability_request_schema_instance.to_dict()
# create an instance of AiAvailabilityRequestSchema from a dict
ai_availability_request_schema_from_dict = AiAvailabilityRequestSchema.from_dict(ai_availability_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


