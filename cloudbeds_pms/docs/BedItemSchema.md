# BedItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type_code** | **str** | Bed type code (e.g., KING_SIZE_BED, SINGLE_BED) | 
**capacity** | **int** | Bed capacity (number of people) | 
**quantity** | **int** | Quantity of this bed type | 

## Example

```python
from cloudbeds_pms.models.bed_item_schema import BedItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BedItemSchema from a JSON string
bed_item_schema_instance = BedItemSchema.from_json(json)
# print the JSON string representation of the object
print(BedItemSchema.to_json())

# convert the object into a dict
bed_item_schema_dict = bed_item_schema_instance.to_dict()
# create an instance of BedItemSchema from a dict
bed_item_schema_from_dict = BedItemSchema.from_dict(bed_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


