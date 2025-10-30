# GetAmenityCategoryCatalogResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**List[GetAmenityCategoryCatalogResponseSchemaCategoriesInner]**](GetAmenityCategoryCatalogResponseSchemaCategoriesInner.md) | List of amenity categories in the catalog | 

## Example

```python
from cloudbeds_pms.models.get_amenity_category_catalog_response_schema import GetAmenityCategoryCatalogResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of GetAmenityCategoryCatalogResponseSchema from a JSON string
get_amenity_category_catalog_response_schema_instance = GetAmenityCategoryCatalogResponseSchema.from_json(json)
# print the JSON string representation of the object
print(GetAmenityCategoryCatalogResponseSchema.to_json())

# convert the object into a dict
get_amenity_category_catalog_response_schema_dict = get_amenity_category_catalog_response_schema_instance.to_dict()
# create an instance of GetAmenityCategoryCatalogResponseSchema from a dict
get_amenity_category_catalog_response_schema_from_dict = GetAmenityCategoryCatalogResponseSchema.from_dict(get_amenity_category_catalog_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


