# AddonResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the add-on | 
**name** | **str** | Display name of the add-on, localized based on the Accept-Language header | 
**description** | **str** | Human-readable description, localized based on the Accept-Language header | 
**product_id** | **str** | Identifier of the underlying product this add-on is based on | 
**price** | [**MoneySchema**](MoneySchema.md) |  | 

## Example

```python
from cloudbeds_pms.models.addon_response_schema import AddonResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AddonResponseSchema from a JSON string
addon_response_schema_instance = AddonResponseSchema.from_json(json)
# print the JSON string representation of the object
print(AddonResponseSchema.to_json())

# convert the object into a dict
addon_response_schema_dict = addon_response_schema_instance.to_dict()
# create an instance of AddonResponseSchema from a dict
addon_response_schema_from_dict = AddonResponseSchema.from_dict(addon_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


