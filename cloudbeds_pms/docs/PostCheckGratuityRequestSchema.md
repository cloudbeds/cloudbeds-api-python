# PostCheckGratuityRequestSchema

Request body for posting tips onto an existing check. The check is identified by the `checkId` path parameter, so the body carries only the gratuity entries — a `checkId` sent in the body is ignored. The tips inherit the check's folio target and check number; POS context stays an attribute of the check and is not copied onto them. Retry-safety is the required Idempotency-Key header. For a tip with no associated check, use POST /folio/v1/gratuities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gratuities** | [**List[GratuitySchema]**](GratuitySchema.md) | Gratuity entries to post to the check. At least one entry required. Each entry becomes its own folio line item and its own Accounting Service transaction. | 

## Example

```python
from cloudbeds_pms.models.post_check_gratuity_request_schema import PostCheckGratuityRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostCheckGratuityRequestSchema from a JSON string
post_check_gratuity_request_schema_instance = PostCheckGratuityRequestSchema.from_json(json)
# print the JSON string representation of the object
print(PostCheckGratuityRequestSchema.to_json())

# convert the object into a dict
post_check_gratuity_request_schema_dict = post_check_gratuity_request_schema_instance.to_dict()
# create an instance of PostCheckGratuityRequestSchema from a dict
post_check_gratuity_request_schema_from_dict = PostCheckGratuityRequestSchema.from_dict(post_check_gratuity_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


