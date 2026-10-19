# AvailabilitySearchRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_ids** | **List[int]** | Property IDs to check availability for (max 20) | 
**start_date** | **str** | Check-in date (YYYY-MM-DD) | 
**end_date** | **str** | Check-out date (YYYY-MM-DD) | 
**adults** | **int** | Number of adults | [optional] 
**children** | **int** | Number of children | [optional] 

## Example

```python
from cloudbeds_pms.models.availability_search_request_schema import AvailabilitySearchRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilitySearchRequestSchema from a JSON string
availability_search_request_schema_instance = AvailabilitySearchRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AvailabilitySearchRequestSchema.to_json())

# convert the object into a dict
availability_search_request_schema_dict = availability_search_request_schema_instance.to_dict()
# create an instance of AvailabilitySearchRequestSchema from a dict
availability_search_request_schema_from_dict = AvailabilitySearchRequestSchema.from_dict(availability_search_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


