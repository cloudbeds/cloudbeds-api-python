# AmountsForSalePutRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**availability** | [**List[AvailabilityUpdatePutRequestSchema]**](AvailabilityUpdatePutRequestSchema.md) | Availability updates per room type. | 
**test_request** | **bool** | Mark as test request (honored in non-production only). | [optional] 

## Example

```python
from cloudbeds_pms.models.amounts_for_sale_put_request_schema import AmountsForSalePutRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AmountsForSalePutRequestSchema from a JSON string
amounts_for_sale_put_request_schema_instance = AmountsForSalePutRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AmountsForSalePutRequestSchema.to_json())

# convert the object into a dict
amounts_for_sale_put_request_schema_dict = amounts_for_sale_put_request_schema_instance.to_dict()
# create an instance of AmountsForSalePutRequestSchema from a dict
amounts_for_sale_put_request_schema_from_dict = AmountsForSalePutRequestSchema.from_dict(amounts_for_sale_put_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


