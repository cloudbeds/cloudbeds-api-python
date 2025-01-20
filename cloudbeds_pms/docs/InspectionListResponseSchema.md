# InspectionListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return | 
**offset** | **int** | The offset for the current page of results | 
**data** | [**List[InspectionItemSchema]**](InspectionItemSchema.md) | The list of data objects | 

## Example

```python
from cloudbeds_pms.models.inspection_list_response_schema import InspectionListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of InspectionListResponseSchema from a JSON string
inspection_list_response_schema_instance = InspectionListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(InspectionListResponseSchema.to_json())

# convert the object into a dict
inspection_list_response_schema_dict = inspection_list_response_schema_instance.to_dict()
# create an instance of InspectionListResponseSchema from a dict
inspection_list_response_schema_from_dict = InspectionListResponseSchema.from_dict(inspection_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


