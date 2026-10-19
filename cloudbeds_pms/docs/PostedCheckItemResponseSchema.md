# PostedCheckItemResponseSchema

A posted check line echo — position-matched to the request items[] entry so the caller can correlate each accepted line to its own POS-side identity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_line_id** | **str** | The partner-supplied line reference accepted on items[].externalLineId, echoed verbatim — null when the line was posted without one. Address this value (with the check&#39;s checkId) in any future line-scoped operation such as a partial refund or partial void. | 

## Example

```python
from cloudbeds_pms.models.posted_check_item_response_schema import PostedCheckItemResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of PostedCheckItemResponseSchema from a JSON string
posted_check_item_response_schema_instance = PostedCheckItemResponseSchema.from_json(json)
# print the JSON string representation of the object
print(PostedCheckItemResponseSchema.to_json())

# convert the object into a dict
posted_check_item_response_schema_dict = posted_check_item_response_schema_instance.to_dict()
# create an instance of PostedCheckItemResponseSchema from a dict
posted_check_item_response_schema_from_dict = PostedCheckItemResponseSchema.from_dict(posted_check_item_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


