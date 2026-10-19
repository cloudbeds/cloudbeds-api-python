# AiAvailabilityResponseSchemaAvailabilitySearch

The search as it was answered, with defaults filled in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_code** | **str** |  | 
**check_in** | **date** |  | 
**check_out** | **date** |  | 
**nights** | **int** |  | 
**adults** | **int** | Null when the request left it out and each offer is priced at its room type&#39;s base occupancy. | 
**children** | **int** |  | 
**currency_code** | **str** |  | 

## Example

```python
from cloudbeds_pms.models.ai_availability_response_schema_availability_search import AiAvailabilityResponseSchemaAvailabilitySearch

# TODO update the JSON string below
json = "{}"
# create an instance of AiAvailabilityResponseSchemaAvailabilitySearch from a JSON string
ai_availability_response_schema_availability_search_instance = AiAvailabilityResponseSchemaAvailabilitySearch.from_json(json)
# print the JSON string representation of the object
print(AiAvailabilityResponseSchemaAvailabilitySearch.to_json())

# convert the object into a dict
ai_availability_response_schema_availability_search_dict = ai_availability_response_schema_availability_search_instance.to_dict()
# create an instance of AiAvailabilityResponseSchemaAvailabilitySearch from a dict
ai_availability_response_schema_availability_search_from_dict = AiAvailabilityResponseSchemaAvailabilitySearch.from_dict(ai_availability_response_schema_availability_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


