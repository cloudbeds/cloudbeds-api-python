# PricingCollectionResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | [**List[PricingResponseSchema]**](PricingResponseSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.pricing_collection_response_schema import PricingCollectionResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PricingCollectionResponseSchema from a JSON string
pricing_collection_response_schema_instance = PricingCollectionResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PricingCollectionResponseSchema.to_json())

# convert the object into a dict
pricing_collection_response_schema_dict = pricing_collection_response_schema_instance.to_dict()
# create an instance of PricingCollectionResponseSchema from a dict
pricing_collection_response_schema_from_dict = PricingCollectionResponseSchema.from_dict(pricing_collection_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


