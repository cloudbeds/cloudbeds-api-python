# SegmentCreateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_id** | **str** | Group ID. | 
**name** | **str** | Segment name. | 
**code** | **str** | Segment code. | 
**description** | **str** | Segment description. | 
**is_enabled** | **bool** | Is Segment enabled?. | 
**rate_plan_ids** | **List[str]** | List of Rate Plan IDs. | 

## Example

```python
from cloudbeds_pms.models.segment_create_request_schema import SegmentCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentCreateRequestSchema from a JSON string
segment_create_request_schema_instance = SegmentCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(SegmentCreateRequestSchema.to_json())

# convert the object into a dict
segment_create_request_schema_dict = segment_create_request_schema_instance.to_dict()
# create an instance of SegmentCreateRequestSchema from a dict
segment_create_request_schema_from_dict = SegmentCreateRequestSchema.from_dict(segment_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


