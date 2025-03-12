# SegmentDeleteRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Segment ID. | 

## Example

```python
from cloudbeds_pms.models.segment_delete_request_schema import SegmentDeleteRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentDeleteRequestSchema from a JSON string
segment_delete_request_schema_instance = SegmentDeleteRequestSchema.from_json(json)
# print the JSON string representation of the object
print(SegmentDeleteRequestSchema.to_json())

# convert the object into a dict
segment_delete_request_schema_dict = segment_delete_request_schema_instance.to_dict()
# create an instance of SegmentDeleteRequestSchema from a dict
segment_delete_request_schema_from_dict = SegmentDeleteRequestSchema.from_dict(segment_delete_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


