# GetAmenityCatalogResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amenities** | [**List[GetAmenityCatalogResponseSchemaAmenitiesInner]**](GetAmenityCatalogResponseSchemaAmenitiesInner.md) | List of amenities in the catalog | 

## Example

```python
from cloudbeds_pms.models.get_amenity_catalog_response_schema import GetAmenityCatalogResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetAmenityCatalogResponseSchema from a JSON string
get_amenity_catalog_response_schema_instance = GetAmenityCatalogResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GetAmenityCatalogResponseSchema.to_json())

# convert the object into a dict
get_amenity_catalog_response_schema_dict = get_amenity_catalog_response_schema_instance.to_dict()
# create an instance of GetAmenityCatalogResponseSchema from a dict
get_amenity_catalog_response_schema_from_dict = GetAmenityCatalogResponseSchema.from_dict(get_amenity_catalog_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


