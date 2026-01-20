# UpdatePropertyAmenitiesRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenities** | **List[str]** | List of amenity codes to set for the property | [optional] 

## Example

```python
from cloudbeds_pms.models.update_property_amenities_request_schema import UpdatePropertyAmenitiesRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePropertyAmenitiesRequestSchema from a JSON string
update_property_amenities_request_schema_instance = UpdatePropertyAmenitiesRequestSchema.from_json(json)
# print the JSON string representation of the object
print(UpdatePropertyAmenitiesRequestSchema.to_json())

# convert the object into a dict
update_property_amenities_request_schema_dict = update_property_amenities_request_schema_instance.to_dict()
# create an instance of UpdatePropertyAmenitiesRequestSchema from a dict
update_property_amenities_request_schema_from_dict = UpdatePropertyAmenitiesRequestSchema.from_dict(update_property_amenities_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


