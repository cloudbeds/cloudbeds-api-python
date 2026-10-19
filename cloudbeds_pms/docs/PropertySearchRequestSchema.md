# PropertySearchRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**city** | **str** | City name to search for (partial match) | [optional] 
**latitude** | **float** | Latitude for geo-based search | [optional] 
**longitude** | **float** | Longitude for geo-based search | [optional] 
**radius_km** | **float** | Search radius in kilometers (requires latitude/longitude) | [optional] 
**limit** | **int** | Maximum number of results (max 20) | [optional] 
**offset** | **int** | Number of results to skip | [optional] 

## Example

```python
from cloudbeds_pms.models.property_search_request_schema import PropertySearchRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PropertySearchRequestSchema from a JSON string
property_search_request_schema_instance = PropertySearchRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PropertySearchRequestSchema.to_json())

# convert the object into a dict
property_search_request_schema_dict = property_search_request_schema_instance.to_dict()
# create an instance of PropertySearchRequestSchema from a dict
property_search_request_schema_from_dict = PropertySearchRequestSchema.from_dict(property_search_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


