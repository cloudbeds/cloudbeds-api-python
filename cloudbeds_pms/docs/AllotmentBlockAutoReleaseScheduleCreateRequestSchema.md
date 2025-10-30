# AllotmentBlockAutoReleaseScheduleCreateRequestSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**release_date** | **str** |  | 
**allotment_block_id** | **str** |  | 
**room_type_id** | **str** |  | 
**start_date** | **str** |  | 
**end_date** | **str** |  | 
**release_value_type** | **str** |  | 
**release_value** | **int** |  | 
**release_units** | **str** |  | [optional] 

## Example

```python
from cloudbeds_pms.models.allotment_block_auto_release_schedule_create_request_schema import AllotmentBlockAutoReleaseScheduleCreateRequestSchema

# TODO update the JSON string below
json = "{}"
# create an instance of AllotmentBlockAutoReleaseScheduleCreateRequestSchema from a JSON string
allotment_block_auto_release_schedule_create_request_schema_instance = AllotmentBlockAutoReleaseScheduleCreateRequestSchema.from_json(json)
# print the JSON string representation of the object
print(AllotmentBlockAutoReleaseScheduleCreateRequestSchema.to_json())

# convert the object into a dict
allotment_block_auto_release_schedule_create_request_schema_dict = allotment_block_auto_release_schedule_create_request_schema_instance.to_dict()
# create an instance of AllotmentBlockAutoReleaseScheduleCreateRequestSchema from a dict
allotment_block_auto_release_schedule_create_request_schema_from_dict = AllotmentBlockAutoReleaseScheduleCreateRequestSchema.from_dict(allotment_block_auto_release_schedule_create_request_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


