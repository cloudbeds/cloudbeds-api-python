# SegmentSingleRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Segment ID. | 

## Example

```python
from cloudbeds_pms.models.segment_single_request_schema import SegmentSingleRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentSingleRequestSchema from a JSON string
segment_single_request_schema_instance = SegmentSingleRequestSchema.from_json(json)
# print the JSON string representation of the object
print(SegmentSingleRequestSchema.to_json())

# convert the object into a dict
segment_single_request_schema_dict = segment_single_request_schema_instance.to_dict()
# create an instance of SegmentSingleRequestSchema from a dict
segment_single_request_schema_from_dict = SegmentSingleRequestSchema.from_dict(segment_single_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


