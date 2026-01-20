# AmenityItemSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Unique amenity code | 
**name** | **str** | Translated amenity name | 
**category_code** | **str** | Category code | 
**is_top** | **bool** | Whether this is a top amenity | 

## Example

```python
from cloudbeds_pms.models.amenity_item_schema import AmenityItemSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AmenityItemSchema from a JSON string
amenity_item_schema_instance = AmenityItemSchema.from_json(json)
# print the JSON string representation of the object
print(AmenityItemSchema.to_json())

# convert the object into a dict
amenity_item_schema_dict = amenity_item_schema_instance.to_dict()
# create an instance of AmenityItemSchema from a dict
amenity_item_schema_from_dict = AmenityItemSchema.from_dict(amenity_item_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


