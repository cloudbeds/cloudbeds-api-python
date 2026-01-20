# UpdatePropertyAmenitiesResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenities** | [**List[AmenityItemSchema]**](AmenityItemSchema.md) | Updated list of property amenities | 

## Example

```python
from cloudbeds_pms.models.update_property_amenities_response_schema import UpdatePropertyAmenitiesResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePropertyAmenitiesResponseSchema from a JSON string
update_property_amenities_response_schema_instance = UpdatePropertyAmenitiesResponseSchema.from_json(json)
# print the JSON string representation of the object
print(UpdatePropertyAmenitiesResponseSchema.to_json())

# convert the object into a dict
update_property_amenities_response_schema_dict = update_property_amenities_response_schema_instance.to_dict()
# create an instance of UpdatePropertyAmenitiesResponseSchema from a dict
update_property_amenities_response_schema_from_dict = UpdatePropertyAmenitiesResponseSchema.from_dict(update_property_amenities_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


