# BedItemResponseSchema

Bed item in response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Bed ID | 
**type_code** | **str** | Bed type code | 
**capacity** | **int** | Bed capacity | 
**quantity** | **int** | Quantity of this bed type | 

## Example

```python
from cloudbeds_pms.models.bed_item_response_schema import BedItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BedItemResponseSchema from a JSON string
bed_item_response_schema_instance = BedItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(BedItemResponseSchema.to_json())

# convert the object into a dict
bed_item_response_schema_dict = bed_item_response_schema_instance.to_dict()
# create an instance of BedItemResponseSchema from a dict
bed_item_response_schema_from_dict = BedItemResponseSchema.from_dict(bed_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


