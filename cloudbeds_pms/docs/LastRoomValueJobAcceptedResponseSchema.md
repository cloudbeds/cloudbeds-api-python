# LastRoomValueJobAcceptedResponseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_reference_id** | **int** | Reference ID for tracking via getAsyncApiJob. | 

## Example

```python
from cloudbeds_pms.models.last_room_value_job_accepted_response_schema import LastRoomValueJobAcceptedResponseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of LastRoomValueJobAcceptedResponseSchema from a JSON string
last_room_value_job_accepted_response_schema_instance = LastRoomValueJobAcceptedResponseSchema.from_json(json)
# print the JSON string representation of the object
print(LastRoomValueJobAcceptedResponseSchema.to_json())

# convert the object into a dict
last_room_value_job_accepted_response_schema_dict = last_room_value_job_accepted_response_schema_instance.to_dict()
# create an instance of LastRoomValueJobAcceptedResponseSchema from a dict
last_room_value_job_accepted_response_schema_from_dict = LastRoomValueJobAcceptedResponseSchema.from_dict(last_room_value_job_accepted_response_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


