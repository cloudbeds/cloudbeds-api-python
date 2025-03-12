# SegmentListResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**data** | [**List[SegmentResponseSchema]**](SegmentResponseSchema.md) |  | [optional] 

## Example

```python
from cloudbeds_pms.models.segment_list_response_schema import SegmentListResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentListResponseSchema from a JSON string
segment_list_response_schema_instance = SegmentListResponseSchema.from_json(json)
# print the JSON string representation of the object
print(SegmentListResponseSchema.to_json())

# convert the object into a dict
segment_list_response_schema_dict = segment_list_response_schema_instance.to_dict()
# create an instance of SegmentListResponseSchema from a dict
segment_list_response_schema_from_dict = SegmentListResponseSchema.from_dict(segment_list_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


