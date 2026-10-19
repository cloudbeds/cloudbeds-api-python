# FeeExternalIdResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requested_fee_id** | **str** | Fee id as sent in the request. | 
**fee_id** | **str** | Current version of the fee the External ID was written to. Differs from requestedFeeId when the requested fee has since been edited. | 
**external_id** | **str** | External ID now assigned; null when cleared. | 

## Example

```python
from cloudbeds_pms.models.fee_external_id_response_schema import FeeExternalIdResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FeeExternalIdResponseSchema from a JSON string
fee_external_id_response_schema_instance = FeeExternalIdResponseSchema.from_json(json)
# print the JSON string representation of the object
print(FeeExternalIdResponseSchema.to_json())

# convert the object into a dict
fee_external_id_response_schema_dict = fee_external_id_response_schema_instance.to_dict()
# create an instance of FeeExternalIdResponseSchema from a dict
fee_external_id_response_schema_from_dict = FeeExternalIdResponseSchema.from_dict(fee_external_id_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


