# GetPropertyAmenitiesResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenities** | [**List[AmenityItemSchema]**](AmenityItemSchema.md) | List of active property amenities | 
**custom_amenities** | **List[str]** | List of custom property amenities | 

## Example

```python
from cloudbeds_pms.models.get_property_amenities_response_schema import GetPropertyAmenitiesResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetPropertyAmenitiesResponseSchema from a JSON string
get_property_amenities_response_schema_instance = GetPropertyAmenitiesResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GetPropertyAmenitiesResponseSchema.to_json())

# convert the object into a dict
get_property_amenities_response_schema_dict = get_property_amenities_response_schema_instance.to_dict()
# create an instance of GetPropertyAmenitiesResponseSchema from a dict
get_property_amenities_response_schema_from_dict = GetPropertyAmenitiesResponseSchema.from_dict(get_property_amenities_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


