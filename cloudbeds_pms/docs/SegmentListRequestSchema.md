# SegmentListRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **int** | The limit for the number of items to return (max 500) | [optional] [default to 100]
**offset** | **int** | The offset for the current page of results | [optional] [default to 0]
**filters** | [**QueryParameterDynamicFilterSchemaFilters**](QueryParameterDynamicFilterSchemaFilters.md) |  | [optional] 
**enabled** | **bool** | List only enabled segments. | [optional] [default to False]

## Example

```python
from cloudbeds_pms.models.segment_list_request_schema import SegmentListRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentListRequestSchema from a JSON string
segment_list_request_schema_instance = SegmentListRequestSchema.from_json(json)
# print the JSON string representation of the object
print(SegmentListRequestSchema.to_json())

# convert the object into a dict
segment_list_request_schema_dict = segment_list_request_schema_instance.to_dict()
# create an instance of SegmentListRequestSchema from a dict
segment_list_request_schema_from_dict = SegmentListRequestSchema.from_dict(segment_list_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


