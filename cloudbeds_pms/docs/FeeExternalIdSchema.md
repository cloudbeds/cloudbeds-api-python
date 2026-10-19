# FeeExternalIdSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fee_id** | **str** | Cloudbeds fee id, as returned in &#x60;feeID&#x60; by getTaxesAndFees: a positive integer without leading zeros, at most 9223372036854775807. An id replaced by a later edit of the fee is accepted and resolved to the fee&#39;s current version. | 
**external_id** | **str** | External ID to assign, at most 64 characters after leading and trailing whitespace is trimmed. Null, an empty value or an omitted field clears the mapping. | [optional] 

## Example

```python
from cloudbeds_pms.models.fee_external_id_schema import FeeExternalIdSchema

# TODO update the JSON string below
json = "{}"
# create an instance of FeeExternalIdSchema from a JSON string
fee_external_id_schema_instance = FeeExternalIdSchema.from_json(json)
# print the JSON string representation of the object
print(FeeExternalIdSchema.to_json())

# convert the object into a dict
fee_external_id_schema_dict = fee_external_id_schema_instance.to_dict()
# create an instance of FeeExternalIdSchema from a dict
fee_external_id_schema_from_dict = FeeExternalIdSchema.from_dict(fee_external_id_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


