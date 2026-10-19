# AvailabilitySearchResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PropertyAvailabilityResponseSchema]**](PropertyAvailabilityResponseSchema.md) | Properties with available room types | 

## Example

```python
from cloudbeds_pms.models.availability_search_response_schema import AvailabilitySearchResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AvailabilitySearchResponseSchema from a JSON string
availability_search_response_schema_instance = AvailabilitySearchResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AvailabilitySearchResponseSchema.to_json())

# convert the object into a dict
availability_search_response_schema_dict = availability_search_response_schema_instance.to_dict()
# create an instance of AvailabilitySearchResponseSchema from a dict
availability_search_response_schema_from_dict = AvailabilitySearchResponseSchema.from_dict(availability_search_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


