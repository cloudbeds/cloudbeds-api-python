# SegmentEnableRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Segment ID. | 

## Example

```python
from cloudbeds_pms.models.segment_enable_request_schema import SegmentEnableRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentEnableRequestSchema from a JSON string
segment_enable_request_schema_instance = SegmentEnableRequestSchema.from_json(json)
# print the JSON string representation of the object
print(SegmentEnableRequestSchema.to_json())

# convert the object into a dict
segment_enable_request_schema_dict = segment_enable_request_schema_instance.to_dict()
# create an instance of SegmentEnableRequestSchema from a dict
segment_enable_request_schema_from_dict = SegmentEnableRequestSchema.from_dict(segment_enable_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


