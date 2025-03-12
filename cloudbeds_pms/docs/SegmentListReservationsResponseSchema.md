# SegmentListReservationsResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**reservation_ids** | **List[str]** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.segment_list_reservations_response_schema import SegmentListReservationsResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of SegmentListReservationsResponseSchema from a JSON string
segment_list_reservations_response_schema_instance = SegmentListReservationsResponseSchema.from_json(json)
# print the JSON string representation of the object
print(SegmentListReservationsResponseSchema.to_json())

# convert the object into a dict
segment_list_reservations_response_schema_dict = segment_list_reservations_response_schema_instance.to_dict()
# create an instance of SegmentListReservationsResponseSchema from a dict
segment_list_reservations_response_schema_from_dict = SegmentListReservationsResponseSchema.from_dict(segment_list_reservations_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


