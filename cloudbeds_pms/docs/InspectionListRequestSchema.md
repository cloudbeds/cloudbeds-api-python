# InspectionListRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return (max 500) | [optional] [default to 100]
**offset** | **int** | The offset for the current page of results | [optional] [default to 0]
**filters** | [**QueryParameterDynamicFilterSchemaFilters**](QueryParameterDynamicFilterSchemaFilters.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.inspection_list_request_schema import InspectionListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionListRequestSchema from a JSON string
inspection_list_request_schema_instance = InspectionListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(InspectionListRequestSchema.to_json())

# convert the object into a dict
inspection_list_request_schema_dict = inspection_list_request_schema_instance.to_dict()
# create an instance of InspectionListRequestSchema from a dict
inspection_list_request_schema_from_dict = InspectionListRequestSchema.from_dict(inspection_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


