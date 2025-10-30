# GetAmenityCatalogResponseSchemaAmenitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Unique amenity code | 
**name** | **str** | Translated amenity name | 
**category_code** | **str** | Category code | 
**is_top** | **bool** | Whether this is a top amenity | 

## Example

```python
from cloudbeds_pms.models.get_amenity_catalog_response_schema_amenities_inner import GetAmenityCatalogResponseSchemaAmenitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAmenityCatalogResponseSchemaAmenitiesInner from a JSON string
get_amenity_catalog_response_schema_amenities_inner_instance = GetAmenityCatalogResponseSchemaAmenitiesInner.from_json(json)
# print the JSON string representation of the object
print(GetAmenityCatalogResponseSchemaAmenitiesInner.to_json())

# convert the object into a dict
get_amenity_catalog_response_schema_amenities_inner_dict = get_amenity_catalog_response_schema_amenities_inner_instance.to_dict()
# create an instance of GetAmenityCatalogResponseSchemaAmenitiesInner from a dict
get_amenity_catalog_response_schema_amenities_inner_from_dict = GetAmenityCatalogResponseSchemaAmenitiesInner.from_dict(get_amenity_catalog_response_schema_amenities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


