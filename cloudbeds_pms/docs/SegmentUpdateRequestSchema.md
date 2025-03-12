# SegmentUpdateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Segment ID. | 
**group_id** | **str** | Group ID. | 
**name** | **str** | Segment name. | 
**code** | **str** | Segment code. | 
**description** | **str** | Segment description. | 
**is_enabled** | **bool** | Is Segment enabled?. | 
**rate_plan_ids** | **List[str]** | List of Rate Plan IDs. | 

## Example

```python
from cloudbeds_pms.models.segment_update_request_schema import SegmentUpdateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentUpdateRequestSchema from a JSON string
segment_update_request_schema_instance = SegmentUpdateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(SegmentUpdateRequestSchema.to_json())

# convert the object into a dict
segment_update_request_schema_dict = segment_update_request_schema_instance.to_dict()
# create an instance of SegmentUpdateRequestSchema from a dict
segment_update_request_schema_from_dict = SegmentUpdateRequestSchema.from_dict(segment_update_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


