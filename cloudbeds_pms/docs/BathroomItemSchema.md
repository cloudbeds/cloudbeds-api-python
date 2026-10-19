# BathroomItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Bathroom type. | 
**location** | **str** | Bathroom location. | 
**privacy** | **str** | Bathroom privacy. Required for private accommodations, must be omitted for shared accommodations. | [optional] 

## Example

```python
from cloudbeds_pms.models.bathroom_item_schema import BathroomItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of BathroomItemSchema from a JSON string
bathroom_item_schema_instance = BathroomItemSchema.from_json(json)
# print the JSON string representation of the object
print(BathroomItemSchema.to_json())

# convert the object into a dict
bathroom_item_schema_dict = bathroom_item_schema_instance.to_dict()
# create an instance of BathroomItemSchema from a dict
bathroom_item_schema_from_dict = BathroomItemSchema.from_dict(bathroom_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


