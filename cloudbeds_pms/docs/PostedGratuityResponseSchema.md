# PostedGratuityResponseSchema

Result of a postGratuity call. gratuityIds are the Cloudbeds-assigned public handles of the posted gratuities — one per gratuities[] entry — each addressable for void via DELETE /folio/v1/gratuities/{gratuityId}.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gratuity_ids** | **List[str]** | Public handles of the posted gratuities, one per gratuities[] entry. Each is addressable for void via DELETE /folio/v1/gratuities/{gratuityId}. | 
**notice** | **str** | Set when this request replayed an earlier one: the same Idempotency-Key was sent with the same body. When present, no new posting was created and the original response is returned. | [optional] 

## Example

```python
from cloudbeds_pms.models.posted_gratuity_response_schema import PostedGratuityResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostedGratuityResponseSchema from a JSON string
posted_gratuity_response_schema_instance = PostedGratuityResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PostedGratuityResponseSchema.to_json())

# convert the object into a dict
posted_gratuity_response_schema_dict = posted_gratuity_response_schema_instance.to_dict()
# create an instance of PostedGratuityResponseSchema from a dict
posted_gratuity_response_schema_from_dict = PostedGratuityResponseSchema.from_dict(posted_gratuity_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


