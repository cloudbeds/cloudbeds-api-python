# PropertySummaryResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_id** | **int** |  | 
**property_name** | **str** |  | 
**property_type** | **str** |  | 
**city** | **str** |  | 
**state** | **str** |  | 
**country** | **str** |  | 
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**currency_code** | **str** |  | 
**timezone** | **str** |  | 
**distance_km** | **float** | Distance from search coordinates in km | [optional] 

## Example

```python
from cloudbeds_pms.models.property_summary_response_schema import PropertySummaryResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PropertySummaryResponseSchema from a JSON string
property_summary_response_schema_instance = PropertySummaryResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PropertySummaryResponseSchema.to_json())

# convert the object into a dict
property_summary_response_schema_dict = property_summary_response_schema_instance.to_dict()
# create an instance of PropertySummaryResponseSchema from a dict
property_summary_response_schema_from_dict = PropertySummaryResponseSchema.from_dict(property_summary_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


