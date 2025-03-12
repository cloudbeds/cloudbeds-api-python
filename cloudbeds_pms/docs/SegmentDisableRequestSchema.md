# SegmentDisableRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Segment ID. | 

## Example

```python
from cloudbeds_pms.models.segment_disable_request_schema import SegmentDisableRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentDisableRequestSchema from a JSON string
segment_disable_request_schema_instance = SegmentDisableRequestSchema.from_json(json)
# print the JSON string representation of the object
print(SegmentDisableRequestSchema.to_json())

# convert the object into a dict
segment_disable_request_schema_dict = segment_disable_request_schema_instance.to_dict()
# create an instance of SegmentDisableRequestSchema from a dict
segment_disable_request_schema_from_dict = SegmentDisableRequestSchema.from_dict(segment_disable_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


