# PostedCheckResponseSchema

Result of a postCheck call. checkId is the public, partner-addressable handle for the posted check — use it for downstream void/reversal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_number** | **str** | Resolved receipt-visible check number — either the partner-supplied value from the request, or a server-minted Cloudbeds reference (cb-&lt;id&gt;) when the partner omitted it. Always returned so the partner can echo it back. | 
**check_id** | **str** | Public, partner-addressable check identifier (accept-or-generate): the value the partner supplied, or a Cloudbeds-generated handle when omitted. Use it to address the check for void via DELETE /folio/v1/checks/{checkId}. Always returned. | 
**items** | [**List[PostedCheckItemResponseSchema]**](PostedCheckItemResponseSchema.md) | Per-line echo of the accepted items[], position-matched to the request items[] (entry i describes request line i) — each entry carries back the partner-supplied externalLineId, or null where the line supplied none, so the caller can correlate posted lines to its own POS line ids without storing any Cloudbeds identifier. Empty for totals-only postings. | 
**notice** | **str** | Set when this request replayed an earlier one: the same Idempotency-Key was sent with the same body. When present, no new posting was created and the original response is returned. | [optional] 

## Example

```python
from cloudbeds_pms.models.posted_check_response_schema import PostedCheckResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostedCheckResponseSchema from a JSON string
posted_check_response_schema_instance = PostedCheckResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PostedCheckResponseSchema.to_json())

# convert the object into a dict
posted_check_response_schema_dict = posted_check_response_schema_instance.to_dict()
# create an instance of PostedCheckResponseSchema from a dict
posted_check_response_schema_from_dict = PostedCheckResponseSchema.from_dict(posted_check_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


