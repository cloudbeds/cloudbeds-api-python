# SegmentResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**group_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_enabled** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**rate_plan_ids** | **List[str]** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**can_edit** | **List[str]** |  | [optional] 
**can_delete** | **bool** |  | [optional] 
**can_disable** | **bool** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.segment_response_schema import SegmentResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentResponseSchema from a JSON string
segment_response_schema_instance = SegmentResponseSchema.from_json(json)
# print the JSON string representation of the object
print(SegmentResponseSchema.to_json())

# convert the object into a dict
segment_response_schema_dict = segment_response_schema_instance.to_dict()
# create an instance of SegmentResponseSchema from a dict
segment_response_schema_from_dict = SegmentResponseSchema.from_dict(segment_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


