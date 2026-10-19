# PropertySearchResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PropertySummaryResponseSchema]**](PropertySummaryResponseSchema.md) | List of matching properties | 
**total** | **int** | Total number of matching properties | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from cloudbeds_pms.models.property_search_response_schema import PropertySearchResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PropertySearchResponseSchema from a JSON string
property_search_response_schema_instance = PropertySearchResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PropertySearchResponseSchema.to_json())

# convert the object into a dict
property_search_response_schema_dict = property_search_response_schema_instance.to_dict()
# create an instance of PropertySearchResponseSchema from a dict
property_search_response_schema_from_dict = PropertySearchResponseSchema.from_dict(property_search_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


