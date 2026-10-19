# BathroomItemResponseSchema

Room type bathroom in response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bathroom ID | 
**type** | **str** | Bathroom type | 
**location** | **str** | Bathroom location | 
**position** | **int** | Display position (0-indexed) | 
**privacy** | **str** | Bathroom privacy. Set only for private accommodations; null for shared accommodations. | [optional] 

## Example

```python
from cloudbeds_pms.models.bathroom_item_response_schema import BathroomItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BathroomItemResponseSchema from a JSON string
bathroom_item_response_schema_instance = BathroomItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(BathroomItemResponseSchema.to_json())

# convert the object into a dict
bathroom_item_response_schema_dict = bathroom_item_response_schema_instance.to_dict()
# create an instance of BathroomItemResponseSchema from a dict
bathroom_item_response_schema_from_dict = BathroomItemResponseSchema.from_dict(bathroom_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


